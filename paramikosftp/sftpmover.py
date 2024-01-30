#!/usr/bin/env python3
'''Alta3 Research | RZFeeser
   Paramiko - Moving files via FTP over SSH using the paramiko library, a "pure python" solution.'''

# standard library
import os  # operating system agnostic operations

# 3rd party imports
import paramiko   # python3 -m pip install paramiko

CREDS = [{"ip": "10.10.2.3", "un": "bender"}, {"ip": "10.10.2.4", "un": "fry"}, {"ip": "10.10.2.5", "un": "zoidberg"}]

def main():
    '''Moving a file with the paramiko library'''

    # loop across the "CREDS" (list of dicts, containing IP and Username)
    for host in CREDS:

        # where to connect to; this is akin to opening a PuTTY
        #  terminal and filling out what you want to connect to
        t = paramiko.Transport(host.get('ip'), 22) # IP and port

        # connect using a username and password
        # in production, we would never want to hard code
        # credentials into our script!
        t.connect(username=host.get('un'), password="alta3") # connect!

        # Now that we have an SSH connection
        # we can lay an FTP conenction overtop of this secure channel
        sftp = paramiko.SFTPClient.from_transport(t)

        # iterate across the files within directory
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
          if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

        # close the connection
        sftp.close() # close the connection
        t.close()    # close SSH connection

# call the main function
if __name__ == "__main__":
    main()

