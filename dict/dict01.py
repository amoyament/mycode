#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Exploring Python Dictionaries - The concepts explored in this example may be used within Ansible playbooks to access variable data.'''

def main():
    '''a short exploration of dictionaries'''

    # create a dictionary
    switch = {'hostname': 'sw-1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    # display parts of the dictionary
    print( switch['hostname'] )
    print( switch['ip'] )

    # request a 'fake' key
    print( switch['lynx'] )  # this will produce an error
    
# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

