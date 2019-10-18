import matplotlib
matplotlib.use('Agg')
from pylab import *
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

year = '../11yr_2001'
AQS = year+'/AQS_Daily_O3_11yr_project.csv'

##### EXTRACT THE COLUMNS OF INTEREST
O3_AQS = np.genfromtxt(AQS, delimiter=',', skip_header=10, usecols=(4,3,12,14)) 
O3_AQS_date = np.genfromtxt(AQS, delimiter=',', skip_header=10, dtype=np.object, usecols=(7)) 
O3_AQS_date_explode = np.genfromtxt(O3_AQS_date, delimiter='/', dtype=int, usecols=(0,1,2))
O3_AQS_date_explode = O3_AQS_date_explode[:,0:1]

##### CREATE NUMPY ARRAYS WITH EXPLODED DATE DATA
O3_AQS = concatenate((O3_AQS,O3_AQS_date_explode),axis=1) 

##### REMOVE ALL BAD DATA
O3_AQS = O3_AQS[O3_AQS[:,2]>0] 
O3_AQS = O3_AQS[O3_AQS[:,3]>0] 

O3_AQS_Jan = O3_AQS[O3_AQS[:,4]==1.]
O3_AQS_Feb = O3_AQS[O3_AQS[:,4]==2.]
O3_AQS_Mar = O3_AQS[O3_AQS[:,4]==3.]
O3_AQS_Apr = O3_AQS[O3_AQS[:,4]==4.]
O3_AQS_May = O3_AQS[O3_AQS[:,4]==5.]
O3_AQS_June = O3_AQS[O3_AQS[:,4]==6.]
O3_AQS_July = O3_AQS[O3_AQS[:,4]==7.]
O3_AQS_Aug = O3_AQS[O3_AQS[:,4]==8.]
O3_AQS_Sept = O3_AQS[O3_AQS[:,4]==9.]
O3_AQS_Oct = O3_AQS[O3_AQS[:,4]==10.]
O3_AQS_Nov = O3_AQS[O3_AQS[:,4]==11.]
O3_AQS_Dec = O3_AQS[O3_AQS[:,4]==12.]

O3_AQS_MAM = concatenate((O3_AQS_Mar,O3_AQS_Apr,O3_AQS_May),axis=0)
O3_AQS_JJA = concatenate((O3_AQS_June,O3_AQS_July,O3_AQS_Aug),axis=0)
O3_AQS_SON = concatenate((O3_AQS_Sept,O3_AQS_Oct,O3_AQS_Nov),axis=0)
O3_AQS_DJF = concatenate((O3_AQS_Dec,O3_AQS_Jan,O3_AQS_Feb),axis=0)

Final = [0,0,0,0,0]
for i in range(len(O3_AQS_MAM)): #generate pairs
    if O3_AQS_MAM[i,4] == -999: pass
    else:
        Temp = O3_AQS_MAM[i]
        for j in range(i+1,len(O3_AQS_MAM)):
    	    if np.array_equal(O3_AQS_MAM[i,0],O3_AQS_MAM[j,0]) and np.array_equal(O3_AQS_MAM[i,1],O3_AQS_MAM[j,1]): 
                Temp = vstack((Temp,O3_AQS_MAM[j]))
                O3_AQS_MAM[j,4] = -999
            else: pass
        if np.array(Temp).size>5:
            Temp = np.mean(Temp,axis=0)
        else: pass
        Final = vstack((Final,Temp))
Final = np.delete(Final,0,0)
O3_AQS_MAM = Final[:]

Final = [0,0,0,0,0]
for i in range(len(O3_AQS_JJA)): #generate pairs
    if O3_AQS_JJA[i,4] == -999: pass
    else:
        Temp = O3_AQS_JJA[i]
        for j in range(i+1,len(O3_AQS_JJA)):
    	    if np.array_equal(O3_AQS_JJA[i,0],O3_AQS_JJA[j,0]) and np.array_equal(O3_AQS_JJA[i,1],O3_AQS_JJA[j,1]): 
                Temp = vstack((Temp,O3_AQS_JJA[j]))
                O3_AQS_JJA[j,4] = -999
            else: pass
        if np.array(Temp).size>5:
            Temp = np.mean(Temp,axis=0)
        else: pass
        Final = vstack((Final,Temp))
Final = np.delete(Final,0,0)
O3_AQS_JJA = Final[:]

Final = [0,0,0,0,0]
for i in range(len(O3_AQS_SON)): #generate pairs
    if O3_AQS_SON[i,4] == -999: pass
    else:
        Temp = O3_AQS_SON[i]
        for j in range(i+1,len(O3_AQS_SON)):
    	    if np.array_equal(O3_AQS_SON[i,0],O3_AQS_SON[j,0]) and np.array_equal(O3_AQS_SON[i,1],O3_AQS_SON[j,1]): 
                Temp = vstack((Temp,O3_AQS_SON[j]))
                O3_AQS_SON[j,4] = -999
            else: pass
        if np.array(Temp).size>5:
            Temp = np.mean(Temp,axis=0)
        else: pass
        Final = vstack((Final,Temp))
Final = np.delete(Final,0,0)
O3_AQS_SON = Final[:]

Final = [0,0,0,0,0]
for i in range(len(O3_AQS_DJF)): #generate pairs
    if O3_AQS_DJF[i,4] == -999: pass
    else:
        Temp = O3_AQS_DJF[i]
        for j in range(i+1,len(O3_AQS_DJF)):
    	    if np.array_equal(O3_AQS_DJF[i,0],O3_AQS_DJF[j,0]) and np.array_equal(O3_AQS_DJF[i,1],O3_AQS_DJF[j,1]): 
                Temp = vstack((Temp,O3_AQS_DJF[j]))
                O3_AQS_DJF[j,4] = -999
            else: pass
        if np.array(Temp).size>5:
            Temp = np.mean(Temp,axis=0)
        else: pass
        Final = vstack((Final,Temp))
Final = np.delete(Final,0,0)
O3_AQS_DJF = Final[:]

#####  CALCULATE BIAS
O3AQS_MAM = (O3_AQS_MAM[:,3] - O3_AQS_MAM[:,2])
O3AQS_JJA = (O3_AQS_JJA[:,3] - O3_AQS_JJA[:,2])
O3AQS_SON = (O3_AQS_SON[:,3] - O3_AQS_SON[:,2])
O3AQS_DJF = (O3_AQS_DJF[:,3] - O3_AQS_DJF[:,2])

lat_AQS_MAM = O3_AQS_MAM[:,0]
lon_AQS_MAM = O3_AQS_MAM[:,1]
lat_AQS_JJA = O3_AQS_JJA[:,0]
lon_AQS_JJA = O3_AQS_JJA[:,1]
lat_AQS_SON = O3_AQS_SON[:,0]
lon_AQS_SON = O3_AQS_SON[:,1]
lat_AQS_DJF = O3_AQS_DJF[:,0]
lon_AQS_DJF = O3_AQS_DJF[:,1]

fig = plt.figure(frameon=False)
map_MAM = fig.add_axes([0.0125,0.52,0.48,0.48])
map_JJA = fig.add_axes([0.5075,0.52,0.48,0.48])
map_SON = fig.add_axes([0.0125,0.055,0.48,0.48])
map_DJF = fig.add_axes([0.5075,0.055,0.48,0.48])
ax_colorbar = fig.add_axes([0.1,0.035,0.3,0.02])
ax_colorbar2 = fig.add_axes([0.6,0.035,0.3,0.02])

m = Basemap(width=5000000,height=3500000,rsphere=(6378137.00,6356752.3142),projection='lcc',
            resolution='l',lat_ts=40,lat_0=40,lon_0=-96.5,ax=map_MAM)
m.fillcontinents(color='#999999', lake_color='#999999', zorder=0)
m.drawcoastlines(color='#000000', linewidth=0.5)
m.drawmapboundary(fill_color='#999999')
m.drawcountries(color='#000000', linewidth=0.5)
m.drawstates(color='#000000', linewidth=0.5) 

n = Basemap(width=5000000,height=3500000,rsphere=(6378137.00,6356752.3142),projection='lcc',
            resolution='l',lat_ts=40,lat_0=40,lon_0=-96.5,ax=map_JJA)
n.fillcontinents(color='#999999', lake_color='#999999', zorder=0)
n.drawcoastlines(color='#000000', linewidth=0.5)
n.drawmapboundary(fill_color='#999999')
n.drawcountries(color='#000000', linewidth=0.5)
n.drawstates(color='#000000', linewidth=0.5) 

o = Basemap(width=5000000,height=3500000,rsphere=(6378137.00,6356752.3142),projection='lcc',
            resolution='l',lat_ts=40,lat_0=40,lon_0=-96.5,ax=map_SON)
o.fillcontinents(color='#999999', lake_color='#999999', zorder=0)
o.drawcoastlines(color='#000000', linewidth=0.5)
o.drawmapboundary(fill_color='#999999')
o.drawcountries(color='#000000', linewidth=0.5)
o.drawstates(color='#000000', linewidth=0.5) 

p = Basemap(width=5000000,height=3500000,rsphere=(6378137.00,6356752.3142),projection='lcc',
            resolution='l',lat_ts=40,lat_0=40,lon_0=-96.5,ax=map_DJF)
p.fillcontinents(color='#999999', lake_color='#999999', zorder=0)
p.drawcoastlines(color='#000000', linewidth=0.5)
p.drawmapboundary(fill_color='#999999')
p.drawcountries(color='#000000', linewidth=0.5)
p.drawstates(color='#000000', linewidth=0.5) 

AQS_xpt_MAM,AQS_ypt_MAM = m(lon_AQS_MAM[:],lat_AQS_MAM[:])
AQS_xpt_JJA,AQS_ypt_JJA = n(lon_AQS_JJA[:],lat_AQS_JJA[:])
AQS_xpt_SON,AQS_ypt_SON = o(lon_AQS_SON[:],lat_AQS_SON[:])
AQS_xpt_DJF,AQS_ypt_DJF = p(lon_AQS_DJF[:],lat_AQS_DJF[:])
lonpt_MAM, latpt_MAM = m(AQS_xpt_MAM,AQS_ypt_MAM,inverse=True)
lonpt_JJA, latpt_JJA = n(AQS_xpt_JJA,AQS_ypt_JJA,inverse=True)
lonpt_SON, latpt_SON = o(AQS_xpt_SON,AQS_ypt_SON,inverse=True)
lonpt_DJF, latpt_DJF = p(AQS_xpt_DJF,AQS_ypt_DJF,inverse=True)

cs1 = m.scatter(AQS_xpt_MAM,AQS_ypt_MAM,c=O3AQS_MAM,edgecolor='none',cmap=cm.RdBu_r,vmin=-25.0,vmax=25.0,s=40) 
cs2 = n.scatter(AQS_xpt_JJA,AQS_ypt_JJA,c=O3AQS_JJA,edgecolor='none',cmap=cm.RdBu_r,vmin=-25.0,vmax=25.0,s=40) 
cs3 = o.scatter(AQS_xpt_SON,AQS_ypt_SON,c=O3AQS_SON,edgecolor='none',cmap=cm.RdBu_r,vmin=-25.0,vmax=25.0,s=40) 
cs4 = p.scatter(AQS_xpt_DJF,AQS_ypt_DJF,c=O3AQS_DJF,edgecolor='none',cmap=cm.RdBu_r,vmin=-25.0,vmax=25.0,s=40) 

meanMAM = np.mean(O3AQS_MAM,axis=0)
meanJJA = np.mean(O3AQS_JJA,axis=0)
meanSON = np.mean(O3AQS_SON,axis=0)
meanDJF = np.mean(O3AQS_DJF,axis=0)

boxlabel11 = 'MAM'
fig.text(.02, .545, boxlabel11, fontsize=14, fontweight='bold', color='w')
boxlabel12 = 'JJA'
fig.text(.515, .545, boxlabel12, fontsize=14, fontweight='bold', color='w')
boxlabel21 = 'SON'
fig.text(.02, .08, boxlabel21, fontsize=14, fontweight='bold', color='w')
boxlabel22 = 'DJF'
fig.text(.515, .08, boxlabel22, fontsize=14, fontweight='bold', color='w')
yearlabel = '2001'
fig.text(.465, .03, yearlabel, fontsize=16, fontweight='bold')

fig.text(.45, .545, format(meanMAM,'.1f'), fontsize=14, fontweight='bold', color='w')
fig.text(.945, .545, format(meanJJA,'.1f'), fontsize=14, fontweight='bold', color='w')
fig.text(.45, .08, format(meanSON,'.1f'), fontsize=14, fontweight='bold', color='w')
fig.text(.945, .08, format(meanDJF,'.1f'), fontsize=14, fontweight='bold', color='w')

plt.colorbar(cs1,cax=ax_colorbar,orientation='horizontal',ticks=[-25,-15,-5,5,15,25])
plt.colorbar(cs2,cax=ax_colorbar2,orientation='horizontal',ticks=[-25,-15,-5,5,15,25])

plt.savefig('aqs_byseason_spatial_2001.png')
