#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import shutil
import datetime as dt
from datetime import datetime, timedelta
import time
import os


# In[ ]:


# Read time from system
x = dt.datetime.now().replace(second=0, microsecond=0)
#hour = x.hour
hour=6
day = x.day
#day=19
month = x.month
#month=8
year = x.year
pdate = datetime(year, month, day, 11, 00, 00).strftime("%Y%m%d")
direc = datetime(year, month, day, 11, 00, 00).strftime("%d-%m-%Y")

os.mkdir(direc)
os.chdir(direc)


# In[ ]:


# Historical data download day by day
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f003&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f003", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f006&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f006", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f009&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f009", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
        
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f012&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f012", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f015&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f015", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f018&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f018", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f021&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f021", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f024&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f024", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f027&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f027", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
        
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f030&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f030", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f033&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f033", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f036&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f036", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f039&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f039", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
	
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f042&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f042", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f045&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f045", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
        
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f048&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f048", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
	
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f051&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f051", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f054&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f054", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f057&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f057", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f060&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f060", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f063&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f063", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f066&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f066", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
	
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f069&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f069", 'wb') as f:
    shutil.copyfileobj(r.raw, f)

url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f072&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f072", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
    
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f072&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f075", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
    
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f072&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f078", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
    
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f072&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f081", 'wb') as f:
    shutil.copyfileobj(r.raw, f)
    
url="https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25_1hr.pl?dir=%2Fgfs."+pdate+"%2F"+str(hour).zfill(2)+"%2Fatmos&file=gfs.t"+str(hour).zfill(2)+"z.pgrb2.0p25.f072&var_PRATE=on&var_UGRD=on&var_VGRD=on&lev_10_m_above_ground=on&lev_surface=on&subregion=&toplat=20&leftlon=72&rightlon=74&bottomlat=18"  
#print(url)
r = requests.get(url, verify=False,stream=True)
r.raw.decode_content = True
with open(f"gfs.t0{hour}z.pgrb2.0p25.f084", 'wb') as f:
    shutil.copyfileobj(r.raw, f)


# In[ ]:


os.chdir('../')


# In[ ]:




