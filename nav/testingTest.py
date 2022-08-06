from unittest import TestCase
import dispatch
import httplib
from urllib import urlencode
import json



class DispatchTest(TestCase):
    def setUp(self):
        self.nomOp = "adjust"
        self.nomTemperature = "72"
        self.nomHeight = "33"
        self.nomPressure = "1100"
        self.nomObservation = "13d51.6"
        
        self.inputDictionary = {}
        self.errorValue = "error"
        self.errorKey = "error"
        
        self.solutionKey = "altitude"
        
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'
        
    def tearDown(self):
        self.inputDictionary = {}
        
    def setOP(self,op):
        self.inputDictionary["op"] = op
    
    def setTemperature(self,temperature):
        self.inputDictionary["temperature"] = temperature
        
    def setHeight(self,height):
        self.inputDictionary["height"] =  height
        
    def setPressure(self,pressure):
        self.inputDictionary["pressure"] = pressure
    
    def setObservation(self,observation):
        self.inputDictionary["observation"] = observation
        
    def nav(self,url,parm):
        try:
            theParm = urlencode(parm)
            theConnection = httplib.HTTPConnection(url, self.BX_PORT)
            theConnection.request("GET", self.BX_PATH + theParm)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            
            return "error encountered during transaction"
        
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result

#===============================================================================
# #
#===============================================================================


def test100_010PassOrFail(self):
    self.setOP("adjust")
    self.setTemperature("72")
    self.setHeight("33")
    self.setPressure("1100")
    self.setObservation("13d51.6")
    result = self.nav(self.BX_URL, self.inputDictionary)
    resultDictionary = self.string2dict(result)
    self.assertEqual(resultDictionary[self.solutionKey], "13d42.3")






