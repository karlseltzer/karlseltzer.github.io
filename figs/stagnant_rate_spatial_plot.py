import matplotlib
matplotlib.use('Agg')
from netCDF4 import Dataset
from pylab import *
from mpl_toolkits.basemap import Basemap
import numpy as np
import math
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt

############################################################################################
#### THIS SCRIPT CALCULATES THE RATE OF CHANGE IN THE NUMBER OF 'STAGNANT DAYS' FOR A GIVEN 
#### GRID DOMAIN. THE METHODOLOGY USED TO CALCULATE A 'STAGNANT DAY' IS DERIVED FROM:
#### Wang, J. X. L. and Angell, J. K.: Air Stagnation Climatology for the United States, NOAA/Air Resource Laboratory ATLAS No. 1, 1999.
#### PLEASE DOUBLE CHECK YOUR WORK AND THIS SCRIPT. FEEL FREE TO CONTACT ME WITH QUESTIONS OR 
#### SUGGESTIONS. - KMS (KARL.SELTZER@DUKE.EDU)
############################################################################################

############################################################################################
#### USER INPUTS:
#### WHERE ARE THE MEAN SEA LEVEL PRESSURE FILES?
mslp_file_loc = '/scratch/lfs/seltzer/NCEP/NCEP_DOE/mslp_dailymean'
#### WHERE ARE THE U-WIND FILES?
uwind_file_loc = '/scratch/lfs/seltzer/NCEP/NCEP_DOE/u_winds_dailymean'
#### WHERE ARE THE V-WIND FILES?
vwind_file_loc = '/scratch/lfs/seltzer/NCEP/NCEP_DOE/v_winds_dailymean'
#### WHERE ARE THE PRECIPITATION RATE FILES?
prate_file_loc = '/scratch/lfs/seltzer/NCEP/NCEP_DOE/precip_rate_dailymean'
#### WHAT DOMAIN WILL THIS ANALYSIS FOCUS ON?
lat0 = 10.00    # southern lat of domain
lat1 = 50.00    # northern lat of domain
lon0 = 90.00   # western lon of domain
lon1 = 150.00   # eastern lon of domain
#### WHAT YEARS ARE YOU ANALYZING?
beginyear = '1979'
endyear   = '2014'
############################################################################################

#### CALCULATE DISTANCE BETWEEN TWO LAT/LON COORDINATES
def latlon_distance(latA,lonA,latB,lonB): 
    lonA, latA, lonB, latB = map(radians, [lonA, latA, lonB, latB])
    dlon = lonB - lonA 
    dlat = latB - latA 
    a = sin(dlat/2)**2 + cos(latA) * cos(latB) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    distance = 6367.0 * c * 1000
    return distance

#### CALCULATE THE LENGTH OF THE DEFINED DOMAIN; FILE IS ARBITRARY; ALL FILES NEED TO HAVE SAME GRID
temp_file      = 'mslp.'+beginyear+'.nc'
f1             = Dataset(mslp_file_loc+'/'+temp_file, 'r')
temp_lat       = f1.variables['lat'][:]
temp_lon       = f1.variables['lon'][:]
f1.close()
#### FIND LENGTH OF THE DEFINED DOMAIN
for j in range(len(temp_lat)):
    if lat1 <= temp_lat[j] and lat1 > temp_lat[j+1]:
       lat1_counter = j
       break
for j in range(len(temp_lat)):
    if lat0 <= temp_lat[j] and lat0 > temp_lat[j+1]:
       lat0_counter = j
       break           
for j in range(len(temp_lon)):
    if lon1 >= temp_lon[j] and lon1 < temp_lon[j+1]:
       lon1_counter = j
       break
for j in range(len(temp_lon)):
    if lon0 >= temp_lon[j] and lon0 < temp_lon[j+1]:
       lon0_counter = j
       break
lat_length = lat0_counter - lat1_counter + 1
lon_length = lon1_counter - lon0_counter + 1
#### INITIALIZE FINAL ARRAYS
numyears = int(endyear) - int(beginyear) + 1
final_year = np.zeros((numyears))
summary  = np.zeros((numyears,lat_length,lon_length))
final_lat    = np.zeros((lat_length))
final_lon    = np.zeros((lon_length))
for i in range(len(final_lat)):
    final_lat[i] = temp_lat[lat1_counter+i]
for i in range(len(final_lon)):
    final_lon[i] = temp_lon[lon0_counter+i]    
#### SUMMARY DIMENSIONS: YEARS,LAT,LON

yearindex = 0

for loopyears in range(0,numyears):
    yearindex = yearindex + 1
    latindex  = 0
    currentyear = str(int(beginyear)+loopyears)
    final_year[loopyears] = int(currentyear)
    
#### WHAT IS THE NAME OF THE FILES? 
    mslp_file = 'mslp.'+currentyear+'.nc'
    uwind_file = 'uwnd.'+currentyear+'.nc'
    vwind_file = 'vwnd.'+currentyear+'.nc'
    prate_file = 'prate.sfc.'+currentyear+'.nc'
#### IMPORT MSLP DATA
    f1 = Dataset(mslp_file_loc+'/'+mslp_file, 'r')
    mslp_time      = f1.variables['time'][:] # hours since 1800-1-1 00:00:0.0
    mslp_lat       = f1.variables['lat'][:]
    mslp_lon       = f1.variables['lon'][:]
    mslp           = f1.variables['mslp'][:,:,:]   # time, lat, lon; units = Pascals
    f1.close()
#### IMPORT U-WIND DATA
    f1 = Dataset(uwind_file_loc+'/'+uwind_file, 'r')
    uwind_time      = f1.variables['time'][:] # hours since 1800-1-1 00:00:0.0
    uwind_lat       = f1.variables['lat'][:]
    uwind_lon       = f1.variables['lon'][:]
    uwind_level     = f1.variables['level'][5]  # hPa
    uwind           = f1.variables['uwnd'][:,5,:,:]   # time, 500 mb level, lat, lon; units = m/s
    f1.close()
#### IMPORT V-WIND DATA
    f1 = Dataset(vwind_file_loc+'/'+vwind_file, 'r')
    vwind_time      = f1.variables['time'][:] # hours since 1800-1-1 00:00:0.0
    vwind_lat       = f1.variables['lat'][:]
    vwind_lon       = f1.variables['lon'][:]
    vwind_level     = f1.variables['level'][5]  # hPa
    vwind           = f1.variables['vwnd'][:,5,:,:]   # time, 500 mb level, lat, lon; units = m/s
    f1.close()
#### IMPORT PRATE DATA
    f1 = Dataset(prate_file_loc+'/'+prate_file, 'r')
    prate_time = f1.variables['time'][:] # hours since 1800-1-1 00:00:0.0
    prate_lat  = f1.variables['lat'][:]
    prate_lon  = f1.variables['lon'][:]
    prate      = f1.variables['prate'][:,:,:]   # time, lat, lon; units = m/s
    f1.close()

#### HAVE TO LOOP THE STAGNANT DAYS ITERATION PROCESS FOR EACH LAT/LON
    for looplat in range(lat1_counter,lat0_counter+1):
        latindex = latindex + 1
        lonindex = 0
        for looplon in range(lon0_counter,lon1_counter+1):
            lonindex = lonindex + 1

        #### INITIALIZE ARRAYS
            final_length = len(mslp_time)
            final_array  = np.zeros((final_length,3))
        #### COLUMNS: MSLP_STAGNANT,WIND_STAGNANT,PRECIPITATION_STAGNANT
        #### UNITS: BINARY,BINARY,BINARY
        #### *_STAGNANT ARE BINARY VARIABLES. (= 1 IF STAGNANT CONDITIONS EXIST FOR THAT VARIABLE)
        #### FOR THE GRID CELL TO BE 'STAGNANT' ON A GIVEN DAY, sum(final_array[:,0:3]) = 3
        
            air_den   = 1.2         # kg/m3
            cor_para  = 2 * 7.2921e-5 * math.sin(radians(mslp_lat[looplat]))
        
        #### SEE IF STAGNANT CONDITIONS EXIST FOR EACH INDIVIDUAL DAY IN YEAR
            for i in range(len(final_array)):
        
        #### STAGNATION VIA SEA LEVEL GEOSTROPHIC WIND SPEED LESS THAN 8 m/s?
                mslp_temp          = mslp[i,looplat,looplon]
                mslp_S             = mslp[i,looplat+1,looplon]
                mslp_N             = mslp[i,looplat-1,looplon]
                mslp_W             = mslp[i,looplat,looplon-1]
                mslp_E             = mslp[i,looplat,looplon+1]
                horiz_press_forceA = (mslp_temp - mslp_W) / latlon_distance(mslp_lat[looplat],mslp_lon[looplon],mslp_lat[looplat],mslp_lon[looplon-1])
                horiz_press_forceB = (mslp_temp - mslp_E) / latlon_distance(mslp_lat[looplat],mslp_lon[looplon],mslp_lat[looplat],mslp_lon[looplon+1])    
                horiz_press_force  = (abs(horiz_press_forceA) + abs(horiz_press_forceB)) / 2
                vert_press_forceA  = (mslp_temp - mslp_N) / latlon_distance(mslp_lat[looplat],mslp_lon[looplon],mslp_lat[looplat-1],mslp_lon[looplon])
                vert_press_forceB  = (mslp_temp - mslp_S) / latlon_distance(mslp_lat[looplat],mslp_lon[looplon],mslp_lat[looplat+1],mslp_lon[looplon])    
                vert_press_force   = (abs(vert_press_forceA) + abs(vert_press_forceB)) / 2
                horiz_mslp_wind    = -1 / air_den / cor_para * horiz_press_force
                vert_mslp_wind     = -1 / air_den / cor_para * vert_press_force   
                mslp_wind          = math.sqrt(horiz_mslp_wind**2 + vert_mslp_wind**2) 
                if mslp_wind < 8.0:
                   final_array[i,0] = 1
                else: final_array[i,0] = 0

        #### STAGNATION VIA MEAN WIND SPEED AT 500 mb LESS THAN 13 m/s?
                uwind_temp = uwind[i,looplat,looplon]
                vwind_temp = vwind[i,looplat,looplon]
                tot_wind   = math.sqrt(uwind_temp**2 + vwind_temp**2)
                if tot_wind < 13.0:
                   final_array[i,1] = 1
                else: final_array[i,1] = 0

        #### STAGNATION VIA NO PRECIPITATION?
                precip_rate_temp = prate[i,looplat,looplon]
                if precip_rate_temp > 9.99e-08:
                   final_array[i,2] = 0
                else: final_array[i,2] = 1

        #### COUNT STAGNANT DAYS
            num_stagnantdays = 0
            for i in range(len(final_array)):
                if sum(final_array[i,0:3]) == 3:
                   num_stagnantdays = num_stagnantdays + 1
                else: pass
            summary[yearindex-1,latindex-1,lonindex-1] = num_stagnantdays

#### INITIALIZE FINAL SLOPE ARRAY
slope  = np.zeros((lat_length,lon_length))

for looplat in range(lat_length):
    for looplon in range(lon_length):
        m,b = np.polyfit(final_year[:],summary[:,looplat,looplon],1)
        slope[looplat,looplon] = m

fig = plt.figure(figsize = (8, 5.5))
ax_topleft = fig.add_axes([.10, .14, .80, .82])
ax_colorbar = fig.add_axes([.10, .08, .80, .02])

m = Basemap(projection='cyl',llcrnrlat=10,urcrnrlat=50,llcrnrlon=90,urcrnrlon=150,resolution='c')
map = m.pcolor(final_lon,final_lat,slope[:,:],cmap=cm.RdBu_r,vmin=-1,vmax=1,ax=ax_topleft) 

m.drawcoastlines(ax=ax_topleft,linewidth=0.5)
m.drawcountries(ax=ax_topleft,linewidth=0.5)
m.drawstates(ax=ax_topleft,linewidth=0.5)

ax_topleft.set_yticks([20,30,40])
ax_topleft.set_xticks([95,105,115,125,135,145])
ax_topleft.tick_params(axis='x',which='both',bottom='off',top='off',labelbottom='on')
ax_topleft.tick_params(axis='y',which='both',left='off',right='off',labelleft='on',labelright='off')
ax_topleft.set_title('Annual Change in Number of Stagnant Days from '+beginyear+'-'+endyear)

plt.colorbar(map,cax=ax_colorbar,orientation='horizontal') #,ticks=[-1,,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],orientation='horizontal')

plt.savefig('stagnant_rate_spatial_plot.png')
