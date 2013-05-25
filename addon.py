#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xbmcgui
import xbmcplugin
import os
import xbmcaddon
import urllib2
import re
import calendar
import datetime

def addImageLink(name,url):
    addon = xbmcaddon.Addon(id='plugin.image.icm')
    iconimage=os.path.join(addon.getAddonInfo('path'),"icon.png")
    liz=xbmcgui.ListItem(unicode(name), iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo( type="Image", infoLabels={ "Title": name })
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
    return ok

addImageLink('Elbląg', 'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=352&col=222&lang=pl')
addImageLink('Gdańsk', 'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=346&col=210&lang=pl')
addImageLink('Chłapowo', 'http://new.meteo.pl/um/metco/mgram_pict.php?ntype=0u&row=334&col=206&lang=pl')

xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True, updateListing=False, cacheToDisc=True)
