# import <package.module>
import json
import datetime

# from <package.module> import <class> as <alias>
from SEN2SOC import SEN2SOCApi

###################################################################
# This file contains usage examples for the SEN2SOC Python module #
###################################################################

########################### Static sensors ########################

# Get list of static sensors
response_list=SEN2SOCApi.getnodes()
print(json.dumps(response_list, sort_keys=True, indent=4))

# Get last values for environmental sensors
response_list=SEN2SOCApi.getlastenvironmentalvalues()
print(json.dumps(response_list, sort_keys=True, indent=4))

# Get last values for irrigation sensors
response_list=SEN2SOCApi.getlastirrigationvalues()
print(json.dumps(response_list, sort_keys=True, indent=4))

############################ Mobile sensors #######################

# Get list of mobile sensors
response_list=SEN2SOCApi.getmobilenodes()
print(json.dumps(response_list, sort_keys=True, indent=4))

# Get last values for mobile sensors
response_list=SEN2SOCApi.getlastmobilevalues()
print(json.dumps(response_list, sort_keys=True, indent=4))

################# Both static & mobile sensors #####################

# Get information of a specific sensor
response_list=SEN2SOCApi.getlastnodevalues(3180)
print(json.dumps(response_list, sort_keys=True, indent=4))

# Get historic values for the specified date interval
enddate = datetime.datetime.today()
startdate = enddate-datetime.timedelta(days=2)
response_list=SEN2SOCApi.gethistoricnodevalues(3180,startdate,enddate)
print(json.dumps(response_list, sort_keys=True, indent=4))