import os
from flask import Flask, request
import nav.dispatch as nav

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /nav
#
#  Parameters are passed as a URL query:
#        /nav?parm1=value1&parm2=value2
#
@app.route("/nav")
    
def server():
    try:
        parm = {}
        for key in request.args:
            parm[key] = str(request.args[key])
        result = nav.dispatch(parm)
        return str(result)
    except Exception as e:
        return e
        
#-----------------------------------
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(port))
