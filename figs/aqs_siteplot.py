import matplotlib
matplotlib.use('Agg')
from pylab import *
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

year = '../11yr_2003'
AQS = year+'/AQS_Daily_O3_11yr_project.csv'


##### EXTRACT THE COLUMNS OF INTEREST
lat_AQS = np.genfromtxt(AQS, delimiter=',', skip_header=10, usecols=(4)) 
lon_AQS = np.genfromtxt(AQS, delimiter=',', skip_header=10, usecols=(3)) 

fig = plt.figure(frameon=False)
map = fig.add_axes([0,0,1,1])
map.axis('off')

m = Basemap(width=5000000,height=3500000,rsphere=(6378137.00,6356752.3142),projection='lcc',
            resolution='l',lat_ts=40,lat_0=40,lon_0=-96.5,ax=map)
m.fillcontinents(color='white', lake_color='white', zorder=0)
m.drawcoastlines(color='#000000', linewidth=0.5)
m.drawcountries(color='#000000', linewidth=0.5)
m.drawstates(color='#000000', linewidth=0.5) 

AQS_xpt,AQS_ypt = m(lon_AQS[:],lat_AQS[:])
lonpt, latpt = m(AQS_xpt,AQS_ypt,inverse=True)
m.plot(AQS_xpt,AQS_ypt,linestyle='None',markeredgecolor='None',marker='o',color='r',markersize=5,label='AQS')  

plt.legend(fontsize=12,numpoints=1)
plt.savefig('aqs_siteplot.png')
