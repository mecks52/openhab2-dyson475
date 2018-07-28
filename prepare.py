'''
Prepares the files for usage in openHAB.
Script asks for the SSID and password from sticker, transfers them to the
needed configuration information and stores it into th the openHAB files.
'''
import base64
import hashlib

# Ask for information from device
print("Which type of Dyson air purifier do you use?\n")
print(" 455 - Pure Hot + Cool Link\n")
print(" 475 - Pure Cool Link\n")
ap_type = input("type (e.g. 455):")
print("Type in the information from the sticker inside your\n")
print("Dyson air purifier:")
ssid = input("Product SSID (e.g.: DYSON-NN2-EU-ABC1234D-475):")
pwd = input("Product WiFi Password (e.g.: adgjsfhk):")
ip_addr = input("Type in the IP-Adress of the air purifier (e.g. 192.168.178.100):")

# Transfer ssid to device identification
dev_id = ssid[6:21]
# Transfer password to hash version
hash = hashlib.sha512()
hash.update(pwd.encode('utf-8'))
pwd_hash = base64.b64encode(hash.digest()).decode('utf-8')

if ap_type == "455":
    # Read in configuration files
    mqtt_cfg = open("./mqtt455.cfg", 'r')
    dyson455_items = open("./dyson455.items", 'r')
    mqtt_cfg_str = mqtt_cfg.read()
    dyson455_items_str = dyson455_items.read()
    mqtt_cfg.close()
    dyson455_items.close()

    # Replace placeholder and write back information into files
    mqtt_cfg_str = mqtt_cfg_str.replace("<dev-id>", dev_id)
    dyson455_items_str = dyson455_items_str.replace("<dev-id>", dev_id)
    mqtt_cfg_str = mqtt_cfg_str.replace("<pwd-hash>", pwd_hash)
    mqtt_cfg_str = mqtt_cfg_str.replace("<ip-addr>", ip_addr)
    mqtt_cfg = open("./mqtt.cfg", 'w')
    dyson455_items = open("./dyson455.items", 'w')
    mqtt_cfg.write(mqtt_cfg_str)
    dyson455_items.write(dyson455_items_str)
    mqtt_cfg.close()
    dyson455_items.close()

elif ap_type == "475":
    # Read in configuration files
    mqtt_cfg = open("./mqtt475.cfg", 'r')
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

else:
    print(ap_type + " is not supported!\nOnly 455 and 475 are supported!")

