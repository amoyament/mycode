#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Python dict methods - Other methods exist to transform dictionaries. These too are available within Ansible.'''

def main():
    '''a short exploration of dictionaries'''

    # create a dictionary
    switch = {'hostname': 'sw-1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    print( "Dictionary - .keys()" )
    print( switch.keys() )  # displays all the keys

    print( "Dictionary - .values()" )
    print( switch.values() )   # displays all the values
    
# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

