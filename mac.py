

#!/usr/bin/python
# coding: utf-8
print "Made by Mo."

import urllib
import sys

if len(sys.argv) == 2:
	mac = sys.argv[1]
	link = "http://api.mylnikov.org/geolocation/wifi?v=1.1&data=wpa2,wpa,wep,open&bssid=%s" % (mac)
	data = urllib.urlopen(link)
	content = data.read()
        print content
else:
	print "Do ./maclook 00:00:00:00"
