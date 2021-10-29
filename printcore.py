#!/usr/bin/env python3
#to send a file of gcode to the printer

from printrun.printcore import printcore
from printrun import gcoder
import time
p=printcore('/dev/ttyUSB0', 115200) # or p.printcore('COM3',115200) on Windows
gcode=[i.strip() for i in open('filename.gcode')] # or pass in your own array of gcode lines instead of reading from a file
gcode = gcoder.LightGCode(gcode)

# startprint silently exits if not connected yet
while not p.online:
  time.sleep(0.1)

p.startprint(gcode) # this will start a print

#If you need to interact with the printer:
p.send_now("M105") # this will send M105 immediately, ahead of the rest of the print
p.pause() # use these to pause/resume the current print
p.resume()
p.disconnect() # this is how you disconnect from the printer once you are done. This will also stop running prints.
