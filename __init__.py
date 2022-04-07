import logging
import datetime
import azure.functions as func
from flatten_json import flatten
import json
import requests
import os
from azure.storage.blob import ContainerClient

def list_blobs():
    connect_str=os.environ['mystorageconnectionappsetting']
    container = ContainerClient.from_connection_string(conn_str=connect_str, container_name="input")
    blob_list = container.list_blobs()
    blob_files=[]
    for x in blob_list:
        blob_files.append(x)
    blob_file_names = [ value['name'] for value in blob_files]
    return blob_file_names

#in the main function we need to include all the names that we specified in the function.json (in this case: req and outputblob)    
def main(req: func.HttpRequest, outputblob: func.Out[str]) -> func.HttpResponse:
    
#How to convert datetime objects: https://www.programiz.com/python-programming/datetime/strftime
    date = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
    logging.info('Python Http trigger processed a request at %s', date)
    
    try:
        api= requests.get('https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/296')
        api.raise_for_status()    
    #what happens in case of an error (source: https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions)
    except requests.exceptions.HTTPError:
        print ("Http Error:", api.status_code)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.RequestException as err:
        print ("An error has occured",err)
         
    else:
        api_json =api.json()
        flat=flatten (api_json)
        logging.info('The request has been processed successfully. The output will be displayed below:')
        print (flat)
        data = json.dumps(flat)
        outputblob.set(data) #outputblob.set can be used only if you have specified it in function.json 
        return func.HttpResponse (data, status_code=200)  
