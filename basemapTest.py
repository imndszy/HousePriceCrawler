# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(16,8))
m = Basemap(projection='stere', lat_0=29.70, lon_0=119.25,
              llcrnrlat=28.11, urcrnrlat=31.33,
              llcrnrlon=117.21, urcrnrlon=121.30,
              rsphere=6371200., resolution='l', area_thresh=10000)
m.readshapefile('./CHN_adm_shp/CHN_adm2', 'states', drawbounds=True)
m.drawcoastlines()
m.drawcountries(linewidth=1.5)
m.drawstates()

plt.savefig("a.png")