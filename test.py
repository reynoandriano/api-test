import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

headers = {
    "Authorization": "Bearer " + os.getenv("TOKEN"),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

source_file = open(os.getenv("SOURCE"), "r")

for aline in source_file:
    code = aline
    host_url = os.getenv("ENDPOINT") + code
    response_code = requests.get(host_url, headers=headers)
    print (response_code.elapsed, end ="\t")
    print (code, end ="")
    # print (response_code.json())

source_file.close()
