import unittest
import nav.adjust as nav
import nav.dispatch as dis
import urllib

class adjustTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    
        
#     Observation: Angle of the sighting relative to a reference point.  This angle is referred to as the "observed altitude".  
#             It is a mandatory string in the form xdy. Where:
#             x is the degree portion of the altitude.  It is positive integer GE 0 and LT 90
#             d is the character "d" and is used to separate degrees from minutes
#             y is the minutes portion of the altitude. It is positive floating point value one digit to the right of the decimal point.
#                 and is in the range GE 0.0 and LT 60.0
# 
#     height= h = Height in feet at which the observation was made.  It is a string of numeric value.  GE 0.  Optional defaults to 0 is missing
# 
#     temperature = t = Temperature ( in degrees F) at the time of the observation.  It is a string of an integer in the range GE -20
#             and LE 120.  Optional defaults to 72 if missing
#             
#     pressure = p = Barometric pressure (in mbar) at the time of the observation.  It is a string of an integer in the 
#                 the range GE 100 and LE 1100.  Optional defaults to 1010 if missing
#                 
#     horizon = h = What the observed altitude is relative to.  It is one of the folowing case-insensitive strings: "artificial" or "natural". optional, 
#                defaults to "natural" if missing.                
        
    def test200_060CalculateAltitudeString(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["altitude"]
        expectedValue = "13d42.3"
        self.assertEqual(expectedValue,actualValue)
        
    def test200_070ReturnErrorMessageForSetAltitude(self):
        values ={
            "altitude": "13d42.3",
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "altitude already calculated"
        self.assertEqual(expectedValue,actualValue)  
        
    def test200_080ReturnErrorMessageForTemperatureOutOfRange(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "-25",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "temperature out of range"
        self.assertEqual(expectedValue,actualValue)         
        
    def test200_085ReturnErrorMessageForTemperatureOutOfRange(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "125",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "temperature out of range"
        self.assertEqual(expectedValue,actualValue) 
        
    def test200_090ReturnErrorMessageForTPressureOutOfRange(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1120"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "Pressure is out of range"
        self.assertEqual(expectedValue,actualValue) 

    def test200_095ReturnErrorMessageForTPressureOutOfRange(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "90"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "Pressure is out of range"
        self.assertEqual(expectedValue,actualValue)       

    def test200_100SetDefaultHorizon(self):
        values ={
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["horizon"]
        expectedValue = "natural"
        self.assertEqual(expectedValue,actualValue)
               
    def test200_105SetDefaultHorizon(self):
        values ={
            "horizon": "artificial",
            "observation":"13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = "artificial"
        expectedValue = values["horizon"]
        self.assertEqual(expectedValue,actualValue)      
        
    def test200_110CheckForOutOfRangeObservationValue(self):
        values ={
            "horizon": "artificial",
            "observation":"0d0.1",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "Observation Value is Not Present or Out of Range"
        self.assertEqual(expectedValue,actualValue)
        
    def test200_115CheckForOutOfRangeObservationValue(self):
        values ={
            "horizon": "artificial",
            "observation":"0d0.2",
            "height": "33",
            "temperature": "72",
            "pressure": "1010"
            }
        nav.adjust(values)
        actualValue = values["altitude"]
        expectedValue = "-266d12.2"
        self.assertEqual(expectedValue,actualValue)
        
    def test100_010TestWithAllVAluesinRange(self):
        values = {
            "observation": "30d1.5",
            "height": "19",
            "pressure": "1000",
            "horizon": "artificial",
            "op": "adjust",
            "temperature": "85"          
            }     
        nav.adjust(values)
        actualValue = values["altitude"]
        expectedValue = "29d59.9"
        self.assertEqual(expectedValue,actualValue)
                
    def test100_020TestWithAllVAluesinRange(self):
        values = {
            "observation": "45d15.2",
            "height": "6",
            "pressure": "1010",
            "horizon": "natural",
            "op": "adjust",
            "temperature": "71"           
            }     
        nav.adjust(values)
        actualValue = values["altitude"]
        expectedValue = "45d11.9"
        self.assertEqual(expectedValue,actualValue)

    def test100_030TestWithAllVAluesinRange(self):
        values = {
            "observation": "42d0.0"
            }     
        nav.adjust(values)
        actualValue = values["altitude"]
        expectedValue = "41d59.0"
        self.assertEqual(expectedValue,actualValue)
        
    def test100_030TestforMissingObservationValue(self):
        values = {
            "height": "33"
            }     
        nav.adjust(values)
        actualValue = values["error"]
        expectedValue = "Required Observation Value is Missing"
        self.assertEqual(expectedValue,actualValue)
        
        
    def test500_010TestDispatch(self):
        values = {
            "op": "adjust",
            "observation": "45d15.2",
            "height": "6",
            "pressure": "1010",
            "horizon": "natural",
            "temperature": "71"           
            }     
        dis.dispatch(values)
        actualValue = values["altitude"]
        expectedValue = "45d11.9"
        self.assertEqual(expectedValue,actualValue)
        
        