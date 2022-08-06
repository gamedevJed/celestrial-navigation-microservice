from urllib import urlencode

def prob(parmDictionary):
    ERROR_HEADER = "error: "
    ERROR_KEY = "error"
    SOLUTION_KEY = "altitude"
    resultDict = {}

values ={
    "height": "33",
    "temperature": "72",
    "pressure": "1100",
    "observation": "43d53.6",
    "horizon": "natural"
}

url = "https://ropajed.mybluemix.net/nav?op=adjust{}".format(urlencode(values))


print(url)