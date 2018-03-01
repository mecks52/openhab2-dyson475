# openhab2-dyson475
Files to integrate Dyson Pure Cool Link (475) air purifier into openHAB 2.  
Tested with:
 - openHAB 2.2
 - Dyson SW-Ver. 21.03.08
 - Python 3.5

## Functionality
Through the Items it is possible to read out the current status of the air purifier. Additionally you can change some settings send commands to Items. Within the Rules file a cron job is defined which requests each 30 seconds the current state of the device.  
 - Temperature -> Shows the latest Temperature value
 - Humidity -> Shows the latest Humidity value
 - P-Value -> Shows the latest raw "P" value from the device. I assume it indicates the level of particle pollution.
 - V-Value -> Shows the latest raq "V" value from the device. I assume it indicates the level of gas pollution.
 - Mode -> Shows the current mode as Number. The mappings are 0 = OFF, 1 = FAN (Manual) and 2 = AUTO. By commanding the Item to a differten Number, you can switch the mode.
 - Contin. Measurement -> Shows if continous measurement of the environment is activated. If activated the sensors will measure temperature, humidity and pollution even if the device is in mode OFF. By commanding the Item you can switch it ON/OFF.
 - Fan Speed -> Shows the current fan speed as Number.  When the air purifier is in AUTO mode, it indicates also AUTO which is mapped to 11, the other numbers are indicating the current speed. If the device is in OFF mode, the Number indicates which speed would be set if switching to FAN mode. By commanding the Item you can change the fan speed in FAN mode.
 - Quality Target -> Shows the current set quality target as Number. The mappings are 1 = LOW, 3 = AVERAGE and 4 = HIGH. The lower the number, the lower the accepted pollution. By commanding the Item you can change the quality target. I haven't tested yet which values are accepted by the air purifier and adopted only the values set by the Smartphone App.
 - Turning -> Indicates if the turning of the fan output is turned On or Off. By commanding the Item you can switch it ON/OFF.
 - Night Mode -> Indicates if the night mode is turned On or Off. In night mode the fan only runs up to speed 4 and the built in display shuts down. By commanding the Item you can switch it ON/OFF.
 - Remaining Filter Hours -> Shows the hours until the filter of the air purifier should be changed.
 - Fan Activity -> Indicates if the Fan blows or not. Mappings are 0 = OFF and 1 = ON.

## Missing Functionality
Not all features from the smartphone app are implemented. Also there are missing features there. Some are listed below and get their own issue if I start implementing them.  
 - reset filter hours
 - set scheduled activities
If I forgot something, please write a message!  
 
## How to use
### Preparation
You will need the information from the sticker behind the filter inside your device. Also you need the ip address of the air purifier. The device needs to be already in your Network.
### Step 1)
Get the files from the repository to your PC.
### Step 2)
Run the python script "prepare.py". It asks you for the information from "Preparation" and prepares the files for usage with your device.
### Step 3)
Install the mqtt binding within your openHAB installation.
### Step 4)
Copy the content of mqtt.cfg file into services/mqtt.cfg.
### Step 5)
Copy dyson475.items into items/ and dyson475.rules into rules/ directory.
### Step 6)
Copy the sitemap with your preferred language into the sitemaps/ directory.

## Python Scripts
The scripts are only working with Python 3 and have been tested with Python 3.5.
### prepare.py
This script asks you for SSID, WiFi password and ip address of the air purifier and writes the created information into mqtt.cfg and dyson475.items.
### getPwdHash.py
If you only need the hash value of the password, you can use this script.

## Problems, Wishes, Experiences, Contribution
Feel free to write me a message or post into the related topic at the openHAB forum:  
https://community.openhab.org/t/integrate-dyson-pure-cool-link/40416  
There is also the possibility to open an issue here on github. If someone created an additional language sitemap, feel free to start a merge request or send a mail and I will integrate it into the repository.
