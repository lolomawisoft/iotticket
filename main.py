import json
import sys
sys.path.insert(1, '/Home/pi/Project3/iotticket')
from models import device
from models import criteria
from models import deviceattribute
from models import datanodesvalue
from client import Client

data = json.load(open(sys.argv[1]))
username = data["student2"]
password = data["student2_Password"]
baseurl = data["https://my.iot-ticket.com/api/v1/"]

#create client object
c= Client(baseurl,username,password)
if(c!="404 URL NOT FOUND!!!"):
	#create device object and call set functions
	d = device()
	d.set_name("Raspi Light Sensor")
	d.set_manufacturer("EAA/Andreas")
	d.set_type("Sensor")
	d.set_description("Project3 light sensor")
	d.set_attributes(deviceattribute("Sensor model","NSL"))
	#call registerdevice function
	resp = c.registerdevice(d)
	#build the new json file for writing data process
	data={"username":username,"password":password,"deviceId":resp.get_deviceId(),"baseurl":baseurl}
	with open("write.json","w") as outfile:
		json.dump(data, outfile, sort_keys=True, indent=4)
	print(resp.get_deviceId())

else:
	print(c)
