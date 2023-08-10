from utilities.configParser import getconfig

def getWeatherDetailsheader():
    header = {"Content-Type":"application/json"}
    return header

def getWeatherDetailsbody():
    body = {"unitGroup":"metric","key": getconfig()["APIKey"]["key"],"contentType":"json"}
    return body
    


