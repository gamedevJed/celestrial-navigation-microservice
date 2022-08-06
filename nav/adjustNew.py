import math
import decimal
decimal.getcontext().rounding = 'ROUND_HALF_UP'



def adjust(values = None):
    
    ERROR_HEADER = "error: "
    ERROR_KEY = "error"
    SOLUTION_KEY = "adjustment"
    DEFAULT_TEMPERATURE = "72"
    DEFAULT_HEIGHT = "0"
    DEFAULT_PRESSURE =   "1010"
    DEFAULT_HORIZON = "natural"
    
    resultDict = values
    
    try:

    # Validate Temperature
        if (not ("temperature" in values)):
            temperature = DEFAULT_TEMPERATURE
        else:
            temperature = values["temperature"]
            if(temperature == " "):
                temperature = DEFAULT_TEMPERATURE
            if(temperature == ''):
                temperature = DEFAULT_TEMPERATURE
            else:
                try:
                    temperature = int(temperature)
                except:
                    raise ValueError("non-integer temperature")
                
                if (temperature >= -20 or temperature >= 120):
                    raise ValueError("out-of-bounds temperature")
                
                
    # Validate Height
        if (not ("height" in values)):
            height = DEFAULT_HEIGHT
        else:
            height = values["height"]
            if(height == " "):
                height = DEFAULT_HEIGHT
            if(height == ''):
                height = DEFAULT_HEIGHT
            else:
                try:
                    height = int(height)
                except:
                    raise ValueError("non-integer height")
                if (height < 0):
                    raise ValueError("out-of-bounds height")
                
                
                
    # Validate Pressure
        if (not ("pressure" in values)):
            pressure = DEFAULT_PRESSURE
        else:
            pressure = values["pressure"]
            if(pressure == " "):
                pressure = DEFAULT_PRESSURE
            if(pressure == ''):
                pressure = DEFAULT_PRESSURE
            else:
                try:
                    pressure = int(pressure)
                except:
                    raise ValueError("non-integer pressure")
                
                if (pressure < 100 and pressure > 1100):
                    raise ValueError("out-of-bounds pressure")
                
                
    # Set Default Horizon
        if (not ("horizon" in values)):
            horizon = DEFAULT_HORIZON
        else:
            horizon = values["horizon"]
            if(horizon == " "):
                horizon = DEFAULT_HORIZON
            if(horizon == ''):
                horizon = DEFAULT_HORIZON
            else:     
                if (horizon != "natural" or horizon != "artificial"):
                    raise ValueError("illegal horizon value")
            
                
    # Validate Observation Values
        if (not ("observation" in values)):
            raise ValueError("no observation value")
        else:
            observation = values["observation"]
            
            if(observation == " "):
                raise ValueError("no observation value")
            if(observation == ''):
                raise ValueError("no observation value")
            else:     
                try:
                    observation = str(observation)
                except:
                    raise ValueError("non-string observation")
            
                # determin range of observation
            
                degrees,minutes = observation.split("d")
                degrees = int(degrees)
                minutes = float(minutes)
                minutes = minutes/60
                observationConvert = minutes + degrees
            
                if (observationConvert < .00166667 ):
                    raise ValueError("Observation Out of Range")
        
           
    except Exception as e:
        result = ERROR_HEADER + e.args[0]
        resultDict[ERROR_KEY] = result
        return resultDict
    
    #calculate Altitude:
    
    refraction = calculateRefraction(temperature,pressure,observationConvert)
    
    dip = calculateDip(height,horizon)
    
    altitude = observationConvert + dip + refraction    
    
    altitudeStr = stringAltitude(altitude)
    
    def stringAltitude(strAlt):
    
        def rounded(n):
            number = decimal.Decimal(str(n))
            rounded = number.quantize(decimal.Decimal('.1'),rounding='ROUND_HALF_UP')
    
            return rounded
    
        altitude = strAlt
        degreesAlt,minutesAlt = divmod(altitude,1)
        degreesAlt = int(degreesAlt)
        degreesAlt = str(degreesAlt)
        minutesAlt = rounded(minutesAlt * 60)
        minutesAlt = str(minutesAlt)
        altitudeStr = degreesAlt+"d"+minutesAlt
        
        return altitudeStr
    
    resultDict[SOLUTION_KEY] = altitudeStr
    
        
        
    return resultDict




def calculateRefraction(x,y,z):
    temperature = int(x)
    pressure = int(y)
    observationConvert = float(z)
    convertCelcius = (temperature - 32) * 5.0/9.0
    refraction  = (-.00452 * pressure)/(273+convertCelcius)/math.tan(math.radians(observationConvert))
    
    return refraction

def calculateDip(a,p):
    horizon= p   
    if(horizon == "natural"):
        dip = (-0.97 * math.sqrt(a))/60
    else:
        dip = 0
        
    return dip





