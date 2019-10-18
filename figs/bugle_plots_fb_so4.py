#!/usr/bin/python

# THIS SCRIPT IS ONLY PARTIALLY GENERATES THE FIGURE SHOWN. I CUT DOWN A LOT OF THE REPETITION.

import numpy as np
import csv
import math
from numpy import genfromtxt
import matplotlib
matplotlib.use('Agg')
from pylab import *
import sys

year2001 = '../11yr_2001'

CSN2001 = year2001+'/CSN_11yr_project.csv'
CASTNet2001 = year2001+'/CASTNET_11yr_project.csv'
IMPROVE2001 = year2001+'/IMPROVE_11yr_project.csv'

##### Python is base zero so, for column numbers, subtract 1
##### Skip first 6 rows of the csv file due to header
##### CSN order = SO4_ob,SO4_mod,NO3_ob,NO3_mod,NH4_ob,NH4_mod,TC_ob,TC_mod,PM25_ob,PM25_mod
##### CASTNet order = SO4_ob,SO4_mod,TNO3_ob,TNO3_mod,NH4_ob,NH4_mod
##### IMPROVE order = SO4_ob,SO4_mod,NO3_ob,NO3_mod,OC_ob,OC_mod,EC_ob,EC_mod,TC_ob,TC_mod,PM25_ob,PM25_mod
CSN2001_array = np.genfromtxt(CSN2001, delimiter=',', skip_header=6, usecols=(7,8,9,10,11,12,21,22,13,14)) 
CASTNet2001_array = np.genfromtxt(CASTNet2001, delimiter=',', skip_header=6, usecols=(7,8,13,14,11,12)) 
IMPROVE2001_array = np.genfromtxt(IMPROVE2001, delimiter=',', skip_header=6, usecols=(7,8,9,10,15,16,17,18,19,20,13,14)) 

##### The dates are delimited by /. So, extract single column with entire date
##### Then explode dates with / delimited
CSN_date_2001 = np.genfromtxt(CSN2001, delimiter=',', skip_header=6, dtype=np.object, usecols=(5)) 
CSN_date_explode_2001 = np.genfromtxt(CSN_date_2001, delimiter='/', dtype=int, usecols=(0,1,2))
CASTNet_date_2001 = np.genfromtxt(CASTNet2001, delimiter=',', skip_header=6, dtype=np.object, usecols=(5)) 
CASTNet_date_explode_2001 = np.genfromtxt(CASTNet_date_2001, delimiter='/', dtype=int, usecols=(0,1,2))
IMPROVE_date_2001 = np.genfromtxt(IMPROVE2001, delimiter=',', skip_header=6, dtype=np.object, usecols=(5)) 
IMPROVE_date_explode_2001 = np.genfromtxt(IMPROVE_date_2001, delimiter='/', dtype=int, usecols=(0,1,2))

##### Now append the exploded dates to the end of the appropriate array
CSN2001_array = concatenate((CSN2001_array,CSN_date_explode_2001),axis=1) 
CASTNet2001_array = concatenate((CASTNet2001_array,CASTNet_date_explode_2001),axis=1)
IMPROVE2001_array = concatenate((IMPROVE2001_array,IMPROVE_date_explode_2001),axis=1) 

##### If any of the obs values are invalid, skip row. USE APPROPRIATE COLUMNS!
##### If any of the mod values are invalid, skip row. USE APPROPRIATE COLUMNS!
CSN2001_array = CSN2001_array[CSN2001_array[:,0]>0] 
CSN2001_array = CSN2001_array[CSN2001_array[:,1]>0] 
CASTNet2001_array = CASTNet2001_array[CASTNet2001_array[:,0]>0] 
CASTNet2001_array = CASTNet2001_array[CASTNet2001_array[:,1]>0] 
IMPROVE2001_array = IMPROVE2001_array[IMPROVE2001_array[:,0]>0] 
IMPROVE2001_array = IMPROVE2001_array[IMPROVE2001_array[:,1]>0] 

CSN2001_jan = CSN2001_array[CSN2001_array[:,10]==1]
CSN2001_feb = CSN2001_array[CSN2001_array[:,10]==2]
CSN2001_mar = CSN2001_array[CSN2001_array[:,10]==3]
CSN2001_apr = CSN2001_array[CSN2001_array[:,10]==4]
CSN2001_may = CSN2001_array[CSN2001_array[:,10]==5]
CSN2001_june = CSN2001_array[CSN2001_array[:,10]==6]
CSN2001_july = CSN2001_array[CSN2001_array[:,10]==7]
CSN2001_aug = CSN2001_array[CSN2001_array[:,10]==8]
CSN2001_sept = CSN2001_array[CSN2001_array[:,10]==9]
CSN2001_oct = CSN2001_array[CSN2001_array[:,10]==10]
CSN2001_nov = CSN2001_array[CSN2001_array[:,10]==11]
CSN2001_dec = CSN2001_array[CSN2001_array[:,10]==12]
CASTNet2001_jan = CASTNet2001_array[CASTNet2001_array[:,6]==1]
CASTNet2001_feb = CASTNet2001_array[CASTNet2001_array[:,6]==2]
CASTNet2001_mar = CASTNet2001_array[CASTNet2001_array[:,6]==3]
CASTNet2001_apr = CASTNet2001_array[CASTNet2001_array[:,6]==4]
CASTNet2001_may = CASTNet2001_array[CASTNet2001_array[:,6]==5]
CASTNet2001_june = CASTNet2001_array[CASTNet2001_array[:,6]==6]
CASTNet2001_july = CASTNet2001_array[CASTNet2001_array[:,6]==7]
CASTNet2001_aug = CASTNet2001_array[CASTNet2001_array[:,6]==8]
CASTNet2001_sept = CASTNet2001_array[CASTNet2001_array[:,6]==9]
CASTNet2001_oct = CASTNet2001_array[CASTNet2001_array[:,6]==10]
CASTNet2001_nov = CASTNet2001_array[CASTNet2001_array[:,6]==11]
CASTNet2001_dec = CASTNet2001_array[CASTNet2001_array[:,6]==12]
IMPROVE2001_jan = IMPROVE2001_array[IMPROVE2001_array[:,12]==1]
IMPROVE2001_feb = IMPROVE2001_array[IMPROVE2001_array[:,12]==2]
IMPROVE2001_mar = IMPROVE2001_array[IMPROVE2001_array[:,12]==3]
IMPROVE2001_apr = IMPROVE2001_array[IMPROVE2001_array[:,12]==4]
IMPROVE2001_may = IMPROVE2001_array[IMPROVE2001_array[:,12]==5]
IMPROVE2001_june = IMPROVE2001_array[IMPROVE2001_array[:,12]==6]
IMPROVE2001_july = IMPROVE2001_array[IMPROVE2001_array[:,12]==7]
IMPROVE2001_aug = IMPROVE2001_array[IMPROVE2001_array[:,12]==8]
IMPROVE2001_sept = IMPROVE2001_array[IMPROVE2001_array[:,12]==9]
IMPROVE2001_oct = IMPROVE2001_array[IMPROVE2001_array[:,12]==10]
IMPROVE2001_nov = IMPROVE2001_array[IMPROVE2001_array[:,12]==11]
IMPROVE2001_dec = IMPROVE2001_array[IMPROVE2001_array[:,12]==12]

##### Calculate FB and FE. USE APPROPRIATE COLUMNS!
CSN2001_array_fb_jan = sum((CSN2001_jan[:,1] - CSN2001_jan[:,0]) / (CSN2001_jan[:,1] + CSN2001_jan[:,0])) * 2/len(CSN2001_jan) * 100
CSN2001_array_fb_feb = sum((CSN2001_feb[:,1] - CSN2001_feb[:,0]) / (CSN2001_feb[:,1] + CSN2001_feb[:,0])) * 2/len(CSN2001_feb) * 100
CSN2001_array_fb_mar = sum((CSN2001_mar[:,1] - CSN2001_mar[:,0]) / (CSN2001_mar[:,1] + CSN2001_mar[:,0])) * 2/len(CSN2001_mar) * 100
CSN2001_array_fb_apr = sum((CSN2001_apr[:,1] - CSN2001_apr[:,0]) / (CSN2001_apr[:,1] + CSN2001_apr[:,0])) * 2/len(CSN2001_apr) * 100
CSN2001_array_fb_may = sum((CSN2001_may[:,1] - CSN2001_may[:,0]) / (CSN2001_may[:,1] + CSN2001_may[:,0])) * 2/len(CSN2001_may) * 100
CSN2001_array_fb_june = sum((CSN2001_june[:,1] - CSN2001_june[:,0]) / (CSN2001_june[:,1] + CSN2001_june[:,0])) * 2/len(CSN2001_june) * 100
CSN2001_array_fb_july = sum((CSN2001_july[:,1] - CSN2001_july[:,0]) / (CSN2001_july[:,1] + CSN2001_july[:,0])) * 2/len(CSN2001_july) * 100
CSN2001_array_fb_aug = sum((CSN2001_aug[:,1] - CSN2001_aug[:,0]) / (CSN2001_aug[:,1] + CSN2001_aug[:,0])) * 2/len(CSN2001_aug) * 100
CSN2001_array_fb_sept = sum((CSN2001_sept[:,1] - CSN2001_sept[:,0]) / (CSN2001_sept[:,1] + CSN2001_sept[:,0])) * 2/len(CSN2001_sept) * 100
CSN2001_array_fb_oct = sum((CSN2001_oct[:,1] - CSN2001_oct[:,0]) / (CSN2001_oct[:,1] + CSN2001_oct[:,0])) * 2/len(CSN2001_oct) * 100
CSN2001_array_fb_nov = sum((CSN2001_nov[:,1] - CSN2001_nov[:,0]) / (CSN2001_nov[:,1] + CSN2001_nov[:,0])) * 2/len(CSN2001_nov) * 100
CSN2001_array_fb_dec = sum((CSN2001_dec[:,1] - CSN2001_dec[:,0]) / (CSN2001_dec[:,1] + CSN2001_dec[:,0])) * 2/len(CSN2001_dec) * 100
CASTNet2001_array_fb_jan = sum((CASTNet2001_jan[:,1] - CASTNet2001_jan[:,0]) / (CASTNet2001_jan[:,1] + CASTNet2001_jan[:,0])) * 2/len(CASTNet2001_jan) * 100
CASTNet2001_array_fb_feb = sum((CASTNet2001_feb[:,1] - CASTNet2001_feb[:,0]) / (CASTNet2001_feb[:,1] + CASTNet2001_feb[:,0])) * 2/len(CASTNet2001_feb) * 100
CASTNet2001_array_fb_mar = sum((CASTNet2001_mar[:,1] - CASTNet2001_mar[:,0]) / (CASTNet2001_mar[:,1] + CASTNet2001_mar[:,0])) * 2/len(CASTNet2001_mar) * 100
CASTNet2001_array_fb_apr = sum((CASTNet2001_apr[:,1] - CASTNet2001_apr[:,0]) / (CASTNet2001_apr[:,1] + CASTNet2001_apr[:,0])) * 2/len(CASTNet2001_apr) * 100
CASTNet2001_array_fb_may = sum((CASTNet2001_may[:,1] - CASTNet2001_may[:,0]) / (CASTNet2001_may[:,1] + CASTNet2001_may[:,0])) * 2/len(CASTNet2001_may) * 100
CASTNet2001_array_fb_june = sum((CASTNet2001_june[:,1] - CASTNet2001_june[:,0]) / (CASTNet2001_june[:,1] + CASTNet2001_june[:,0])) * 2/len(CASTNet2001_june) * 100
CASTNet2001_array_fb_july = sum((CASTNet2001_july[:,1] - CASTNet2001_july[:,0]) / (CASTNet2001_july[:,1] + CASTNet2001_july[:,0])) * 2/len(CASTNet2001_july) * 100
CASTNet2001_array_fb_aug = sum((CASTNet2001_aug[:,1] - CASTNet2001_aug[:,0]) / (CASTNet2001_aug[:,1] + CASTNet2001_aug[:,0])) * 2/len(CASTNet2001_aug) * 100
CASTNet2001_array_fb_sept = sum((CASTNet2001_sept[:,1] - CASTNet2001_sept[:,0]) / (CASTNet2001_sept[:,1] + CASTNet2001_sept[:,0])) * 2/len(CASTNet2001_sept) * 100
CASTNet2001_array_fb_oct = sum((CASTNet2001_oct[:,1] - CASTNet2001_oct[:,0]) / (CASTNet2001_oct[:,1] + CASTNet2001_oct[:,0])) * 2/len(CASTNet2001_oct) * 100
CASTNet2001_array_fb_nov = sum((CASTNet2001_nov[:,1] - CASTNet2001_nov[:,0]) / (CASTNet2001_nov[:,1] + CASTNet2001_nov[:,0])) * 2/len(CASTNet2001_nov) * 100
CASTNet2001_array_fb_dec = sum((CASTNet2001_dec[:,1] - CASTNet2001_dec[:,0]) / (CASTNet2001_dec[:,1] + CASTNet2001_dec[:,0])) * 2/len(CASTNet2001_dec) * 100
IMPROVE2001_array_fb_jan = sum((IMPROVE2001_jan[:,1] - IMPROVE2001_jan[:,0]) / (IMPROVE2001_jan[:,1] + IMPROVE2001_jan[:,0])) * 2/len(IMPROVE2001_jan) * 100
IMPROVE2001_array_fb_feb = sum((IMPROVE2001_feb[:,1] - IMPROVE2001_feb[:,0]) / (IMPROVE2001_feb[:,1] + IMPROVE2001_feb[:,0])) * 2/len(IMPROVE2001_feb) * 100
IMPROVE2001_array_fb_mar = sum((IMPROVE2001_mar[:,1] - IMPROVE2001_mar[:,0]) / (IMPROVE2001_mar[:,1] + IMPROVE2001_mar[:,0])) * 2/len(IMPROVE2001_mar) * 100
IMPROVE2001_array_fb_apr = sum((IMPROVE2001_apr[:,1] - IMPROVE2001_apr[:,0]) / (IMPROVE2001_apr[:,1] + IMPROVE2001_apr[:,0])) * 2/len(IMPROVE2001_apr) * 100
IMPROVE2001_array_fb_may = sum((IMPROVE2001_may[:,1] - IMPROVE2001_may[:,0]) / (IMPROVE2001_may[:,1] + IMPROVE2001_may[:,0])) * 2/len(IMPROVE2001_may) * 100
IMPROVE2001_array_fb_june = sum((IMPROVE2001_june[:,1] - IMPROVE2001_june[:,0]) / (IMPROVE2001_june[:,1] + IMPROVE2001_june[:,0])) * 2/len(IMPROVE2001_june) * 100
IMPROVE2001_array_fb_july = sum((IMPROVE2001_july[:,1] - IMPROVE2001_july[:,0]) / (IMPROVE2001_july[:,1] + IMPROVE2001_july[:,0])) * 2/len(IMPROVE2001_july) * 100
IMPROVE2001_array_fb_aug = sum((IMPROVE2001_aug[:,1] - IMPROVE2001_aug[:,0]) / (IMPROVE2001_aug[:,1] + IMPROVE2001_aug[:,0])) * 2/len(IMPROVE2001_aug) * 100
IMPROVE2001_array_fb_sept = sum((IMPROVE2001_sept[:,1] - IMPROVE2001_sept[:,0]) / (IMPROVE2001_sept[:,1] + IMPROVE2001_sept[:,0])) * 2/len(IMPROVE2001_sept) * 100
IMPROVE2001_array_fb_oct = sum((IMPROVE2001_oct[:,1] - IMPROVE2001_oct[:,0]) / (IMPROVE2001_oct[:,1] + IMPROVE2001_oct[:,0])) * 2/len(IMPROVE2001_oct) * 100
IMPROVE2001_array_fb_nov = sum((IMPROVE2001_nov[:,1] - IMPROVE2001_nov[:,0]) / (IMPROVE2001_nov[:,1] + IMPROVE2001_nov[:,0])) * 2/len(IMPROVE2001_nov) * 100
IMPROVE2001_array_fb_dec = sum((IMPROVE2001_dec[:,1] - IMPROVE2001_dec[:,0]) / (IMPROVE2001_dec[:,1] + IMPROVE2001_dec[:,0])) * 2/len(IMPROVE2001_dec) * 100

##### Calculate Boylan numbers
var = np.arange(0.0, 20.0, 0.1)
boylan_bias_goal = (170 * (math.e**(-0.5*(var)/0.5)) + 30)
boylan_bias_criteria = (140 * (math.e**(-0.5*(var)/0.5)) + 60)

CSN2001_jan = sum(CSN2001_jan[:,0])/ len(CSN2001_jan) #### USE APPROPRIATE COLUMNS!
CSN2001_feb = sum(CSN2001_feb[:,0])/ len(CSN2001_feb) #### USE APPROPRIATE COLUMNS!
CSN2001_mar = sum(CSN2001_mar[:,0])/ len(CSN2001_mar) #### USE APPROPRIATE COLUMNS!
CSN2001_apr = sum(CSN2001_apr[:,0])/ len(CSN2001_apr) #### USE APPROPRIATE COLUMNS!
CSN2001_may = sum(CSN2001_may[:,0])/ len(CSN2001_may) #### USE APPROPRIATE COLUMNS!
CSN2001_june = sum(CSN2001_june[:,0])/ len(CSN2001_june) #### USE APPROPRIATE COLUMNS!
CSN2001_july = sum(CSN2001_july[:,0])/ len(CSN2001_july) #### USE APPROPRIATE COLUMNS!
CSN2001_aug = sum(CSN2001_aug[:,0])/ len(CSN2001_aug) #### USE APPROPRIATE COLUMNS!
CSN2001_sept = sum(CSN2001_sept[:,0])/ len(CSN2001_sept) #### USE APPROPRIATE COLUMNS!
CSN2001_oct = sum(CSN2001_oct[:,0])/ len(CSN2001_oct) #### USE APPROPRIATE COLUMNS!
CSN2001_nov = sum(CSN2001_nov[:,0])/ len(CSN2001_nov) #### USE APPROPRIATE COLUMNS!
CSN2001_dec = sum(CSN2001_dec[:,0])/ len(CSN2001_dec) #### USE APPROPRIATE COLUMNS!
CASTNet2001_jan = sum(CASTNet2001_jan[:,0])/ len(CASTNet2001_jan) #### USE APPROPRIATE COLUMNS!
CASTNet2001_feb = sum(CASTNet2001_feb[:,0])/ len(CASTNet2001_feb) #### USE APPROPRIATE COLUMNS!
CASTNet2001_mar = sum(CASTNet2001_mar[:,0])/ len(CASTNet2001_mar) #### USE APPROPRIATE COLUMNS!
CASTNet2001_apr = sum(CASTNet2001_apr[:,0])/ len(CASTNet2001_apr) #### USE APPROPRIATE COLUMNS!
CASTNet2001_may = sum(CASTNet2001_may[:,0])/ len(CASTNet2001_may) #### USE APPROPRIATE COLUMNS!
CASTNet2001_june = sum(CASTNet2001_june[:,0])/ len(CASTNet2001_june) #### USE APPROPRIATE COLUMNS!
CASTNet2001_july = sum(CASTNet2001_july[:,0])/ len(CASTNet2001_july) #### USE APPROPRIATE COLUMNS!
CASTNet2001_aug = sum(CASTNet2001_aug[:,0])/ len(CASTNet2001_aug) #### USE APPROPRIATE COLUMNS!
CASTNet2001_sept = sum(CASTNet2001_sept[:,0])/ len(CASTNet2001_sept) #### USE APPROPRIATE COLUMNS!
CASTNet2001_oct = sum(CASTNet2001_oct[:,0])/ len(CASTNet2001_oct) #### USE APPROPRIATE COLUMNS!
CASTNet2001_nov = sum(CASTNet2001_nov[:,0])/ len(CASTNet2001_nov) #### USE APPROPRIATE COLUMNS!
CASTNet2001_dec = sum(CASTNet2001_dec[:,0])/ len(CASTNet2001_dec) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_jan = sum(IMPROVE2001_jan[:,0])/ len(IMPROVE2001_jan) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_feb = sum(IMPROVE2001_feb[:,0])/ len(IMPROVE2001_feb) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_mar = sum(IMPROVE2001_mar[:,0])/ len(IMPROVE2001_mar) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_apr = sum(IMPROVE2001_apr[:,0])/ len(IMPROVE2001_apr) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_may = sum(IMPROVE2001_may[:,0])/ len(IMPROVE2001_may) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_june = sum(IMPROVE2001_june[:,0])/ len(IMPROVE2001_june) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_july = sum(IMPROVE2001_july[:,0])/ len(IMPROVE2001_july) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_aug = sum(IMPROVE2001_aug[:,0])/ len(IMPROVE2001_aug) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_sept = sum(IMPROVE2001_sept[:,0])/ len(IMPROVE2001_sept) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_oct = sum(IMPROVE2001_oct[:,0])/ len(IMPROVE2001_oct) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_nov = sum(IMPROVE2001_nov[:,0])/ len(IMPROVE2001_nov) #### USE APPROPRIATE COLUMNS!
IMPROVE2001_dec = sum(IMPROVE2001_dec[:,0])/ len(IMPROVE2001_dec) #### USE APPROPRIATE COLUMNS!

plt.figure(figsize=(6,5))

plt.plot(var/2,boylan_bias_goal,'-',color='#000000',linewidth=2.0)
plt.plot(var/2,-boylan_bias_goal,'-',color='#000000',linewidth=2.0)
plt.plot(var/2,boylan_bias_criteria,'-',color='#BDBDBD',linewidth=2.0)
plt.plot(var/2,-boylan_bias_criteria,'-',color='#BDBDBD',linewidth=2.0)
plt.plot(CSN2001_jan,CSN2001_array_fb_jan,marker='o',color='y',markersize=8)
plt.plot(CSN2001_feb,CSN2001_array_fb_feb,marker='o',color='y',markersize=8)
plt.plot(CSN2001_mar,CSN2001_array_fb_mar,marker='o',color='y',markersize=8)
plt.plot(CSN2001_apr,CSN2001_array_fb_apr,marker='o',color='y',markersize=8)
plt.plot(CSN2001_may,CSN2001_array_fb_may,marker='o',color='y',markersize=8)
plt.plot(CSN2001_june,CSN2001_array_fb_june,marker='o',color='y',markersize=8)
plt.plot(CSN2001_july,CSN2001_array_fb_july,marker='o',color='y',markersize=8)
plt.plot(CSN2001_aug,CSN2001_array_fb_aug,marker='o',color='y',markersize=8)
plt.plot(CSN2001_sept,CSN2001_array_fb_sept,marker='o',color='y',markersize=8)
plt.plot(CSN2001_oct,CSN2001_array_fb_oct,marker='o',color='y',markersize=8)
plt.plot(CSN2001_nov,CSN2001_array_fb_nov,marker='o',color='y',markersize=8)
plt.plot(CSN2001_dec,CSN2001_array_fb_dec,marker='o',color='y',markersize=8)
plt.plot(CASTNet2001_jan,CASTNet2001_array_fb_jan,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_feb,CASTNet2001_array_fb_feb,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_mar,CASTNet2001_array_fb_mar,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_apr,CASTNet2001_array_fb_apr,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_may,CASTNet2001_array_fb_may,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_june,CASTNet2001_array_fb_june,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_july,CASTNet2001_array_fb_july,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_aug,CASTNet2001_array_fb_aug,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_sept,CASTNet2001_array_fb_sept,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_oct,CASTNet2001_array_fb_oct,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_nov,CASTNet2001_array_fb_nov,marker='^',color='r',markersize=8)
plt.plot(CASTNet2001_dec,CASTNet2001_array_fb_dec,marker='^',color='r',markersize=8)
plt.plot(IMPROVE2001_jan,IMPROVE2001_array_fb_jan,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_feb,IMPROVE2001_array_fb_feb,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_mar,IMPROVE2001_array_fb_mar,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_apr,IMPROVE2001_array_fb_apr,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_may,IMPROVE2001_array_fb_may,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_june,IMPROVE2001_array_fb_june,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_july,IMPROVE2001_array_fb_july,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_aug,IMPROVE2001_array_fb_aug,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_sept,IMPROVE2001_array_fb_sept,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_oct,IMPROVE2001_array_fb_oct,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_nov,IMPROVE2001_array_fb_nov,marker='s',color='b',markersize=8)
plt.plot(IMPROVE2001_dec,IMPROVE2001_array_fb_dec,marker='s',color='b',markersize=8)

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 12}
plt.axis([0.0, 7.0, -150.0, 150.0])
#plt.xlabel('Avg. Observed Conc. [$\mu$g/m$^3$]',**font)
plt.ylabel('Mean Fractional Bias',**font)
plt.title('Sulfate',**font)
plt.xticks([1,2,3,4,5,6,7])

##### Make Legends
hgoal, = plot([1,1],color='#000000',marker='None',linewidth=2.0)
hcriteria, = plot([1,1],color='#BDBDBD',marker='None',linewidth=2.0)
first_legend = plt.legend((hgoal,hcriteria),('Goal','Criteria'),fontsize=12,loc=1)
hgoal.set_visible(False)
hcriteria.set_visible(False)
hCSN, = plot([0,0],color='y',marker='o',markersize=8,linestyle="None")
hCASTNet, = plot([0,0],color='r',marker='^',markersize=8,linestyle="None")
hIMPROVE, = plot([0,0],color='b',marker='s',markersize=8,linestyle="None")
plt.legend((hCSN,hCASTNet,hIMPROVE),('CSN','CASTNet','IMPROVE'),fontsize=12,loc=4,numpoints=1)
hCSN.set_visible(False)
hCASTNet.set_visible(False)
hIMPROVE.set_visible(False)
plt.gca().add_artist(first_legend)

plt.savefig("bugle_plots_fb_so4.png")