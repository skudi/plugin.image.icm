#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xbmcgui
import xbmcplugin
import os
import xbmcaddon
import sys
import datetime

def addImageLink(name,url):
    addon = xbmcaddon.Addon(id='plugin.image.icm')
    iconimage=os.path.join(addon.getAddonInfo('path'),"icon.png")
    liz=xbmcgui.ListItem(unicode(name), iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo( type="Image", infoLabels={ "Title": name })
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    return ok

addImageLink('Elbląg',   'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=352&col=222&lang=pl')
addImageLink('Gdańsk',   'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=346&col=210&lang=pl')
addImageLink('Chłapowo', 'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=334&col=206&lang=pl')
addImageLink('Borsk',    'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=360&col=199&lang=pl')
chour = datetime.datetime.now().hour
tzshift=2 #windifnder does'n respect summer time, always CET?
for xhour in range(chour, chour+18):
    hour = xhour % 24
    if (hour > 20 and hour < 9): continue
    addImageLink('windfinder %02d' % (hour), 'http://www.windfinder.com/grafiken/forecasts/superforecast_poland_baltic_sea%02d.png' % (xhour - tzshift))

print sys.builtin_module_names

xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True, updateListing=False, cacheToDisc=True)
