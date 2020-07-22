import sys
from auth import MiBand3
from constants import ALERT_TYPES
import time
import os
import json
from datetime import datetime

# Set MAC address of your band here
MAC_ADDR = "D4:32:70:F4:17:D6"
# need to initialize or not
INIT = False

# create object
band = MiBand3(MAC_ADDR, debug=False)
band.setSecurityLevel(level = "medium")
# Authenticate the MiBand
if(INIT):
    if band.initialize():
        print("Initialized...")
    band.disconnect()
    sys.exit(0)
else:
    band.authenticate()

def get_band_details():
    # put everything into pretty dictionary
    band_data = {
        "Soft revision":band.get_revision(),
        "Hardware revision":band.get_hrdw_revision(),
        "Serial":band.get_serial(),
        "Battery":band.get_battery_info(),
        "Time":band.get_current_time(),
        "Steps":band.get_steps()
    }
    return band_data

def accel_raw_callback(accel_raw):
    print("Accelerometer raw data: %s" % accel_raw)

def heart_beat_raw_callback(heart_raw):
    print("Heartbeat raw data: %s" % heart_raw)

def heart_beat_callback(beat):
    print("Heartbeat BPM: %s" % beat)


def other():
    # sending call alert demo
    band.send_alert(ALERT_TYPES.PHONE)
    print("one...")
    # sending message alert demo
    band.send_alert(ALERT_TYPES.MESSAGE)
    # sending custom message demo
    band.send_custom_alert(5,"Hello World")
    # sending custom call demo
    band.send_custom_alert(3,"Xiaomi calling")
    # sending custom missed call message
    band.send_custom_alert(4,"Missed call from Xiaomi")
    # change the watch to custom time and date
    band.change_date("10-07-2020 07:32:20")
    # get heart beat continuesly
    band.start_raw_data_realtime(heart_measure_callback=heart_beat_callback)
    # get raw heart monnitor data
    band.start_raw_data_realtime(heart_raw_callback=heart_beat_raw_callback)
    # get accelerometer raw data
    band.start_raw_data_realtime(accel_raw_callback=accel_raw_callback)
    # stop all realtime activity from the band
    band.stop_realtime()
    # update the band firmware
    #band.dfuUpdate("/full/firmware/location/goes/here/firmware.fw")


def main():
    print("Starting...")


    steps=band.get_steps()
    print("Steps: "+str(steps))

    start_time = datetime.strptime("22.07.2020 10:01", "%d.%m.%Y %H:%M")
    band.start_get_previews_data(start_time)
    
    while band.active:
        print("Wait Active")
        band.waitForNotifications(0.1)
        
    print("Active cleared...")

    activity_data = band.get_activity_data()
    with open('activity.json', 'w') as outfile:
        json.dump(activity_data, outfile)

if __name__ == "__main__":
    main()
