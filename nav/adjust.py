import math
import decimal
decimal.getcontext().rounding = 'ROUND_HALF_UP'

def adjust(values = None):
    
    if("observation" not in values):
        values["error"] = "Required Observation Value is Missing"
    
    # altitude already calculated    
    elif ("altitude" in values):
        values["error"] = "altitude already calculated"
        
    else:
        #convert observation to usable form for calculations & add to dictionary for testing    
        observation = values["observation"]
        degrees,minutes = observation.split("d")
        degrees = int(degrees)
        minutes = float(minutes)
        minutes = minutes/60
        observationConvert = minutes + degrees  
    
        if (observationConvert > .00166667 ):
        
        # height set default to zero
            if ("height" in values):
                height = int(values["height"])
            else:
                height = 0
                values["height"] = 0
            
            # temperature in or out of range
            if ("temperature" in values):
                temperature = int(values["temperature"])
                if(-20 <= temperature <= 120):
                    temperature = int(values["temperature"])
                else:
                    values["error"] = "temperature out of range"
                    return values["error"]
            else:
                temperature = 72
                        
            # pressure out of range
            if ("pressure" in values):
                pressure = int(values["pressure"])
                
                if(100 <= pressure <= 1100):
                    pressure = int(values["pressure"])
                else:
                    values["error"] =  "Pressure is out of range"
                    return values["error"]
            else:
                pressure = 1010    
            
            # check for value of horizon
            if ("horizon" in values):
                if (values["horizon"] == "natural"):
                    dip = (-0.97 * math.sqrt(height))/60
                    values["dip"] = dip
                else:
                    dip = 0
                    values["dip"] = dip
            else:
                values["horizon"] = "natural"
                dip = (-0.97 * math.sqrt(height))/60   
                values["dip"] = dip
                
            # calculate refraction & add to dictionary
            convertCelcius = (temperature - 32) * 5.0/9.0
            refraction  = (-.00452 * pressure)/(273+convertCelcius)/math.tan(math.radians(observationConvert))
                
            #calculate altitude & add to dictionary
            altitude = observationConvert + dip + refraction
            
            #add rounding function
            def rounded(n):
                number = decimal.Decimal(str(n))
                rounded = number.quantize(decimal.Decimal('.1'),rounding='ROUND_HALF_UP')
        
                return rounded    
            
            #convert altitude to string values
            degreesAlt,minutesAlt = divmod(altitude,1)
            degreesAlt = int(degreesAlt)
            degreesAlt = str(degreesAlt)
            minutesAlt = rounded(minutesAlt * 60)
            minutesAlt = str(minutesAlt)
            altitudeStr = degreesAlt+"d"+minutesAlt
            values["altitude"] = altitudeStr
            
        else:
            
            values["error"] = "Observation Value is Not Present or Out of Range"
  
    return values


