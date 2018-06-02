#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Simple GPS Tracker
# 
# Author: Patrick Schmidt <patrick@ealp-net.at>
# License: Apache License, Version 2.0
#

from gps import *

import os
import time
import datetime
import threading

class GpsdPoller(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.running = True
		self.session = gps(mode=WATCH_ENABLE)

	def run(self):
		while self.running:
			self.session.next()
			
	def getSession(self):
		return self.session

if __name__ == '__main__':
	gpsd = GpsdPoller()
	
	date = datetime.datetime.utcnow()
	filePath = "/opt/simpletracker/log/" + date.strftime("%Y%m%d") + "_gps.log"
	
	try:
		gpsd.start()
		with open(filePath, 'a') as logFile:
			while True:

				logFile.write(str(gpsd.session.fix.time))
				logFile.write(";")
				
				logFile.write(str(round(gpsd.session.fix.longitude,7)))
				logFile.write(";")
				
				logFile.write(str(round(gpsd.session.fix.latitude,7)))
				logFile.write(";")
				
				logFile.write(str(round(gpsd.session.fix.altitude)))
				logFile.write(";")
				
				logFile.write(str(round(gpsd.session.fix.speed,4)))
				logFile.write('\n')
				
				time.sleep(1.0)
		 
	except (KeyboardInterrupt, SystemExit):
		gpsd.running = False
		gpsd.join() 
	
