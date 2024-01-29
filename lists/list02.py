#!/usr/bin/env python3

'''Alta3 Research | RZFeeser
   Lists are 'mutable', that is to say, we can manipulate the state of a list after it has been created.
   
   A complex list is nothing more than a list that contains one or more lists (or other data structures) within itself.
   
   L.append(item) - adds an item to the end of the list
   L.pop(index) - remove the element at this index
   L.insert(index) - inserts an item at the specified index (does not replace the item already in this position)'''   


def main():
    '''Storing data about the local network within a list'''
    
    # servers is a list of network devices and their IP addresses
    servers = [['ios', '10.0.2.1'], ['ios', '10.0.55.1'], ['ios-xr', '10.0.3.1'], ['junos', '10.0.10.1'], ['eos', '10.0.14.1']]      
    
    # display information about the servers to standard out
    print(servers[0])     # display the first network device and IP
    print(servers[0][1])  # display JUST the IP address of the first host

    print(servers[2][1])  # display JUST the IP address of the third host
    
    print(servers[-1][0]) # display "eos"

    servers.pop(1)        # remove ['ios', '10.0.55.1'] from the list (position 1)
    
    print(servers)        # show that servers no longer contains ['ios', '10.0.55.1']

# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

