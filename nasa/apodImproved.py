#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Scripting API calls with Python, and using pprint
   (or pretty print) to display results'''       

# standard library imports
from pprint import pprint as pp # part of the standard library
# import webbrowser

# 3rd party imports
import requests     # python3 -m pip install requests

# define the API
URL = 'https://api.nasa.gov/planetary/apod?api_key=' # this is our API to call

def main():
    """run-time code"""
    
    # read key out of key file
    with open("/home/student/nasa.key", "r") as keyf:
        mykey = keyf.readline().strip()  # read top line from the file
    
    nasaapiobj = requests.get(URL + mykey) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
    print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread.get('explanation')) # display the value for the key explanation
    
    # use .get() to return value associated with key 'hdurl'
    # if it is not avail, we will return "No HD URL for today!"
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    # if our script was running in a GUI environment, we could
    # un-comment this code to automate opening this webpage
    
    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread.get('hdurl')) # open in the default web browser if running in a OS with a GUI

if __name__ == "__main__":
    main()

