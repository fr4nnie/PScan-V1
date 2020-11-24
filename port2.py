import pyfiglet, sys, socket 
from datetime import datetime 
   
banner = pyfiglet.figlet_format("Python PScan") 
print(banner) 
print("Please enter an IPv4 , www, HTTP or a HTTPS address \n")

# Defining a target if we have the the py and an address as arguements 
# then translate hostname to IPv4 or just set it as a target
try:
    if len(sys.argv) == 2:                         
        if sys.argv[1].lower().startswith('https://'):   #remove the https://
             address = sys.argv[1][8:]

        if sys.argv[1].lower().startswith('http://'):    #remove the http://
            address = sys.argv[1][7:]

        if sys.argv[1].lower().startswith('www'):      #if its just a www.
            address = sys.argv[1]
        else:
            try:
                address = sys.argv[1]
            except:
                print("Not valid")
                
    target = socket.gethostbyname(address)
except: 
    print("Invalid arguements, please try again or see the Readme") 

  
# print what we are scanning, and when it started exactly
print("-" * 60) 
print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now().strftime("%d-%m-%y %H:%M:%S")))
print("-" * 60) 
   
try: 
    # will scan ports between 1 to 20,000 
    for port in range(1,20000): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
          
        # returns an error indicator 
        result = sock.connect_ex((target,port)) 
        if result == 0: 
            print("Port open : {}".format(port)) 
        sock.close()          
except KeyboardInterrupt: 
        print("Closing...") 
        sys.exit() 
except socket.gaierror: 
        print("Hostname can't be reached") 
        sys.exit() 
except socket.error: 
        print("Server isn't responding") 
        sys.exit() 


#to do, write functions to validate if the webaddress/IP is valid (for both IPV4 and IPV6)
#to do, add listener to this and select which is wanted at the start of the program
