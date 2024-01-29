#!/usr/bin/env python3

'''Alta3 Research | RZFeeser
   If a list is applied to a loop, the loop will run as many times as there are items in the loop. This process is known as "iterating".

   Each time through the loop offers the coder an opportunity to "use" the value currently returned by the process of iteration.'''   
   
def main():
    '''loop across a list of IP address'''
    
    # simple list of IP addresses
    network = ['10.0.2.1', '10.0.55.1', '10.0.3.1', '10.0.10.1', '10.0.14.1']
    
    # this is a basic "for" loop; each time through the loop
    # the variable ip will take the "next" value from the list, network
    for ip in network:
        print('DHCP has assigned', ip)   # display this string to standard out

# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run

