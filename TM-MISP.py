import json
import requests

url_base = "https://api.xdr.trendmicro.com" # VisionOne URL
upload_threatIntelReport_path = '/v3.0/threatintel/intelligenceReports' # Endpoint to Upload STIX Format to TM
autosweep_path = '/v3.0/threatintel/intelligenceReports/sweep' #Endpoint to Autosweep MISP Data in Trendmicro ThreatIntel

#VisionOne API Token
token = "YOUR_Trend_Micro_Vision_One_API_Token"

filename = input("Enter file path with filename: ")
def say_mispSTIX():

    #filename = "misp.event.list.json"
    f = open(filename, "r")
    data = json.load(f)
    #print (data)
    
    x = data["objects"][1]["id"]
    #print(x)
    stixid = x
    return stixid    

##################### Upload to TrendMicro Threat Intelligence Report ###########################
def upload_TM():
    query_params = {}
    headers = {'Authorization': 'Bearer ' + token}
    data = {'reportName': 'C2C'}
    files = {'file': ('MISP', open(filename, 'rb'), 'application/stix+json')}

    r = requests.post(url_base + upload_threatIntelReport_path, params=query_params, headers=headers, data=data, files=files)

    print(r.status_code)
    if 'application/json' in r.headers.get('Content-Type', '') and len(r.content):
        #print(json.dumps(r.json(), indent=4))
        return "Sucessfully Uploaded to TrendMicro Threat Intelligence"
    else:
        #print(r.text)
        return "Unsucessfull"
        
    

##################### Autosweep uploaded Threat Intelligence Data Uploaded ###########################
def autosweep_TM():
    query_params = {}
    headers = {'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json;charset=utf-8'}
    body = [{'id': stix_report_id,
         'sweepType': 'manual',
         'description': 'Initiated by Script)'}]

    r = requests.post(url_base + autosweep_path, params=query_params, headers=headers, json=body)

    print(r.status_code)
    if 'application/json' in r.headers.get('Content-Type', '') and len(r.content):
        #print(json.dumps(r.json(), indent=4))
        return "Sucessfully initated sweeping task to find IoC related to feed in endpoints"
    else:
        #print(r.text)
        return "Unsucessfull"
 
# ThreatIntel REPORT ID in STIX Format 
stix_report_id = say_mispSTIX()

print (stix_report_id)

Upload_to_ThreatIntel = upload_TM()
print(Upload_to_ThreatIntel)

Autosweep_TM = autosweep_TM()
print(autosweep_TM)  
