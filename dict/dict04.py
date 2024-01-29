#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Python dict methods - Other methods exist to transform dictionaries. These too are available within Ansible.'''

def main():
    '''a short exploration of dictionaries'''

    # create a dictionary
    switch = {'hostname': 'sw-1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}    

    print( "Dictionary - .pop()" )
    switch.pop('version') # removes this key (and value) pair
    print( switch.keys() )  # notice the value of version is gone
    print( switch.values() ) # notice the value 1.2

    print( "Dictionary - ADD a new value" )
    switch['adminlogin'] = 'karl08'
    print( switch.keys() )
    print( switch.values() )

    print( "Dictionary - ADD a new value" )
    switch['password'] = 'qwerty'
    print( switch.keys() )
    print( switch.values() )

# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

