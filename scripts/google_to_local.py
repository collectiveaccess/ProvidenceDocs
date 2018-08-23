#
# This is a simple script to import CSV files from Google Sheets to a local
# directory
#
# by Mike Benowitz
#


import os
import re
from fnmatch import fnmatch
import mmap
import requests
import time
import fileinput

sphx = "../_source"
rstMatch = "*.rst"

googleKey = "AIzaSyDcnu9ldNl-uWRlNg2HPduZdNo_F7OB_c0"

def getCSVInfo(sheetID, googleKey):
    attempts = 3
    i = 0
    while i < attempts:
        time.sleep(2)
        sheetURL = "https://sheets.googleapis.com/v4/spreadsheets/" + sheetID + "?key=" + googleKey
        csvResp = requests.get(sheetURL)
        if csvResp.status_code != 200:
            errorMsg = csvResp.json()
            if errorMsg['error']['status'] == 'NOT_FOUND':
                return {"ERROR": "Missing " + sheetID}
            i += 1
            continue
        csvInfo = csvResp.json()
        return csvInfo

    return {"ERROR": "API Exceeded Retry Attempts"}

curPath = os.path.abspath(os.getcwd())
assetPath = os.path.join(curPath, "../_static/csv/")

errors = []

for path, subdirs, files in os.walk(sphx):
    for name in files:
        if fnmatch(name, rstMatch):
            rst = os.path.join(path, name)
            print rst
            for line in fileinput.input(rst, inplace=True):
                if 'docs.google.com' in line:
                    googleURL = line[9:].strip()
                    pattern =  re.compile("\/((?:(?!\/).)*)\/pub")
                    sheetID = re.search(pattern, googleURL).group(1)
                    csvInfo = getCSVInfo(sheetID, googleKey)
                    if "ERROR" in csvInfo:
                        errors.append(csvInfo)
                        print "%s" % (line)
                        continue
                    sheetName = csvInfo['properties']['title']

                    filename = sheetName.replace(' ', '_').lower() + ".csv"
                    filePath = assetPath + filename
                    print sheetName, filename, filePath
                    csvFile = requests.get(googleURL)
                    with open(filePath, 'wb') as openCSV:
                        openCSV.write(csvFile)
                    relPath = os.path.relpath(filePath, path)
                    print "%s" % ("   :file:" + relPath)
                else:
                    print "%s" % (line)
        break
