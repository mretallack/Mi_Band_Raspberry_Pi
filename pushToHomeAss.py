
import sys
from auth import MiBand3
from constants import ALERT_TYPES
import time
import os
import requests
import json
from datetime import datetime

def main():



    # load in the settings
    with open('settings.json', 'r') as cfgfilehandle:
        settings=json.load(cfgfilehandle)

    band = MiBand3(settings["macaddress"], debug=False)
    band.setSecurityLevel(level = "medium")

    band.authenticate()

    print("Starting from "+str(settings["lastsync"]))
    
    start_time = datetime.strptime(settings["lastsync"], "%d.%m.%Y %H:%M")


    print("hour "+str(start_time.hour))
    print("minute"+str(start_time.minute))

    print(start_time)
    print(type(start_time))


    band.start_get_previews_data(start_time)
    
    while band.active:
        print("Wait Active")
        band.waitForNotifications(0.1)
        
    print("Active cleared...")

    activity_data = band.get_activity_data()


    for dat in activity_data:
        

        # try to push to NextCloud
        headers = {'Content-Type': 'application/json'} 
        # 
        url = settings["nextcloud"]+"/apps/analytics/api/1.0/adddata/" + settings["nextcloudid"]

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        
        payload = {'dimension1': "steps", 'dimension2': dat["timestamp"], 'dimension3': dat["steps"]} 

        res = requests.post(url, json=payload, headers=headers, auth=(settings["nextclouduser"], settings["nextcloudpasswd"]))

        print(res)


        jsonData={
            "attributes": {
                "friendly_name": "Marks Steps Count",
                "unit_of_measurement": "steps"
            },
            "entity_id": "sensor.marks_miband_steps",
            "last_changed": dat["timestamp"],
            "last_updated": dat["timestamp"],
            "state": dat["steps"]
        }

        print(jsonData);

        headers={
            "Authorization": "Bearer "+settings["token"],
            "Content-Type": "application/json"
        }


        #res=requests.post('https://home.retallack.org.uk/api/states/sensor.marksmibandsteps', json=jsonData, headers=headers)

        #print(res)


    current_time = datetime.now() # time object

    settings["lastsync"]=current_time.strftime("%d.%m.%Y %H:%M")

    # save the settings back
    with open('settings.json', 'w') as cfgfilehandle:
        cfgfilehandle.write(json.dumps(settings))



    

if __name__ == "__main__":
    main()


