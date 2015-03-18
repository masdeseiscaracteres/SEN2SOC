# import <package.module>
import json
# from <package.module> import <class> as <alias>
from SEN2SOC import SEN2SOCApi

response_list=SEN2SOCApi.getlastnodevalues(4)
print(json.dumps(response_list, sort_keys=True, indent=4))
