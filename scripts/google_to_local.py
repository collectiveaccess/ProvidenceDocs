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

googleKey = "" # This should be a Google API key that has been enabled to access
               # Google Sheets API. There was one here :( but its been removed
               # for security reasons

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
assetPath = os.path.join(curPath, "../_source/_static/csv/")

errors = []

for path, subdirs, files in os.walk(sphx):
    for name in files:
        if fnmatch(name, rstMatch):
            edit = False
            rst = os.path.join(path, name)
            print rst
            rstFile = open(rst, 'r')
            lines = rstFile.readlines()
            for i, line in enumerate(lines):
                if 'docs.google.com' in line:
                    edit = True
                    googleURL = line[9:].strip()
                    pattern =  re.compile("\/((?:(?!\/).)*)\/pub")
                    sheetID = re.search(pattern, googleURL).group(1)
                    csvInfo = getCSVInfo(sheetID, googleKey)
                    if "ERROR" in csvInfo:
                        errors.append(csvInfo)
                        continue
                    sheetName = csvInfo['properties']['title']

                    filename = sheetName.replace(' ', '_').lower() + ".csv"
                    filePath = assetPath + filename
                    csvFile = requests.get(googleURL)
                    with open(filePath, 'wb') as openCSV:
                        openCSV.write(csvFile.content)
                    relPath = os.path.relpath(filePath, path)
                    lines[i] = "   :file: " + relPath
                    print lines[i]
            rstFile.close()

            if edit == True:
                print "EDITING! " + rst
                rstNew = open(rst, 'w')
                rstNew.writelines(lines)
                rstNew.close()
