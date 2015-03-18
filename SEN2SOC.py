# Proxy class for the web API of the SmartSantander SEN2SOC platform
#
# Official documentation:
# http://smartsantander.eu/wiki/index.php/Data/SEN2SOCSmartSantanderIntegration
#
# Following style guidelines in https://www.python.org/dev/peps/pep-0008/

from urllib.request import urlopen
from datetime import datetime
import json

# Constants
BASE_URL = 'http://data.smartsantander.eu/SENS2SOC'
GETNODES_SUFFIX = '/GetNodes'
GETMOBILENODES_SUFFIX = '/GetMobileNodes'
LASTVALUES_ENVIRONMENTAL_SUFFIX = '/GetEnvMonitoringLastValues'
LASTVALUES_IRRIGATION_SUFFIX = '/GetIrrigationLastValues'
LASTVALUES_MOBILE_SUFFIX = '/GetMobileSensingLastValues'
LASTVALUES_NODE_SUFFIX = '/GetLastValuesbyNodeID'
HISTORICVALUES_NODE_SUFFIX = '/GetHistoricbyNodeID'

class SEN2SOCApi():

    def __openandparse(url,parser=None):
        response = urlopen(url)
        response_str = response.read().decode('utf-8')
        response_list = json.loads(response_str, object_hook=parser)
        return response_list

    def __parser(dct):
        for (tag, value) in dct.items():
            if tag in ["latitude", "longitude", "battery",  "atmosphericPressure", "light",
                       "groundTemperature", "relativeHumidity", "soilMoistureTension", "temperature", "rainfall",
                       "solarRadiation", "windSpeed", "altitude", "odometer", "CO", "particles", "ozone", "NO2",
                        "speed"]: #some elements parsed as floats
                dct[tag]=float(dct[tag])
            if tag in ["nodeId", "course"]: #some elements parsed as integers
                dct[tag]=int(dct[tag])
            if tag in ["date"]: #some elements parsed as datetime objects
                dct[tag]=datetime.strptime(dct[tag],"%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d_%H:%M:%S") #JSON friendly
                #dct[tag]=datetime.strptime(dct[tag],"%Y-%m-%d %H:%M:%S") #MongoDB friendly
        return dct

    @staticmethod #static method (a.k.a. function) decoration since Python 2.2
    def getnodes():
        """
        Return a list of dictionaries with all static SmartSantander node IDs, positions and its types
        """
        url = BASE_URL + GETNODES_SUFFIX
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def getmobilenodes():
        """
        Return a list of dictionaries with all mobile SmartSantander node IDs and its types
        """
        url = BASE_URL + GETMOBILENODES_SUFFIX
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def getlastenvironmentalvalues():
        """
        Return the last measurements recorded by fixed sensors of type "light", "noise" and "temperature".
        """
        url = BASE_URL + LASTVALUES_ENVIRONMENTAL_SUFFIX
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def getlastirrigationvalues():
        """
        Return the last measurements recorded by fixed sensors of type "irrigation", "agriculture" and "env_station".
        """
        url = BASE_URL + LASTVALUES_IRRIGATION_SUFFIX
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def getlastmobilevalues():
        """
        Return the last environmental measurements recorded by mobile sensors of type "BUS", "MICROBUS", "TAXI"
        and "parquesyjardines".
        """
        url = BASE_URL + LASTVALUES_MOBILE_SUFFIX
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def getlastnodevalues(nodeId):
        """
        Return the last values measured by the sensor node identified by the identification number "nodeID".
        """
        url = BASE_URL + LASTVALUES_NODE_SUFFIX + "/" + str(nodeId)
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)

    @staticmethod
    def gethistoricnodevalues(nodeId,startdate,enddate):
        """
        Return historic sensor data for the sensor identified by "nodeID" between "startdate" and "enddate".
        """
        url = BASE_URL + HISTORICVALUES_NODE_SUFFIX + "/" + str(nodeId) + "/" + \
              startdate.strftime("%Y-%m-%dT%H:%M:%S") + "/" + enddate.strftime("%Y-%m-%dT%H:%M:%S")
        print(url)
        return SEN2SOCApi.__openandparse(url,parser=SEN2SOCApi.__parser)
