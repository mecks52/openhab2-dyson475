'''
Prepares the files for usage in openHAB.
Script asks for the SSID and password from sticker, transfers them to the
needed configuration information and stores it into th the openHAB files.
'''
import base64
import hashlib

# Ask for information from device
print("Type in the information from the sticker inside your\n")
print("Dyson Pure Cool Link air purifier:")
ssid = input("Product SSID (e.g.: DYSON-NN2-EU-ABC1234D-475):")
pwd = input("Product WiFi Password (e.g.: adgjsfhk):")
ip_addr = input("Type in the IP-Adress of the air purifier (e.g. 192.168.178.100):")

# Transfer ssid to device identification
dev_id = ssid[6:21]
# Transfer password to hash version
hash = hashlib.sha512()
hash.update(pwd.encode('utf-8'))
pwd_hash = base64.b64encode(hash.digest()).decode('utf-8')

# Read in configuration files
mqtt_cfg = open("./mqtt.cfg", 'r')
dyson475_items = open("./dyson475.items", 'r')
mqtt_cfg_str = mqtt_cfg.read()
dyson475_items_str = dyson475_items.read()
mqtt_cfg.close()
dyson475_items.close()

# Replace placeholder and write back information into files
mqtt_cfg_str = mqtt_cfg_str.replace("<dev-id>", dev_id)
dyson475_items_str = dyson475_items_str.replace("<dev-id>", dev_id)
mqtt_cfg_str = mqtt_cfg_str.replace("<pwd-hash>", pwd_hash)
mqtt_cfg_str = mqtt_cfg_str.replace("<ip-addr>", ip_addr)
mqtt_cfg = open("./mqtt.cfg", 'w')
dyson475_items = open("./dyson475.items", 'w')
mqtt_cfg.write(mqtt_cfg_str)
dyson475_items.write(dyson475_items_str)
mqtt_cfg.close()
dyson475_items.close()
