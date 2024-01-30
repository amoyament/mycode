#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Scripting API calls with Python"""

# 3rd party requests
import requests

# Define APOD 
URL = 'https://api.nasa.gov/planetary/apod?api_key='

def main():
    """Making call to APOD API"""
    
    # read key out of key file
    with open("/home/student/nasa.key", "r") as keyf:
        mykey = keyf.readline().strip()  # read top line from the file

    # Call the webservice
    apodurlobj = requests.get(URL + mykey)

    # read the response object & strip off json
    apodread = apodurlobj.json()

    # display our Pythonic data
    print("\n\nConverted Python data")
    print(apodread)
    
if __name__ == '__main__':
    main()

