#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Using Python to parse JSON - Network Engineers are very often tasked with work with JSON data, as it is a popular response type to API requests.'''

# standard library import
import json # working with JSON data

def main():
    '''open a file containing JSON with python'''
    
    # open the JSON file in read-mode with the handle jf
    with open("ciscoAPIC.json", "r") as jf:
        # transfrom JSON to python data structures
        fog = json.load(jf)
    
    # when we stop indenting, jf is auto-closed
    
    # display the length of fog['imdata']
    print("The number of instances: ", len(fog['imdata']))

    # loop across the data structure fog['imdata']
    for instance in fog['imdata']:
        # each time through the loop "get" the version and display it
        print("Firmware version running - ", instance.get('firmwareCtrlrRunning').get('attributes').get('version'))

# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

