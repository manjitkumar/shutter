# Main script to test and execute our Shutter. Feel free to modify as per your requirements.

from Shutter import Shutter
from User import User
from Device import Device
from time import sleep            


test_url = 'http://api.browserstack.com/3'              #url to make and test connection
browsers_url = 'http://api.browserstack.com/3/browsers' #ur to get all (non-beta)browsers info
worker_url = 'http://api.browserstack.com/3/worker'     #url to make workers

username= '<*********>'      # replace <***> with your browserstack automate username
key =     '<*********>'      # replace <***> with your browserstack automate pass-key  

args = {"os_version":"Snow Leopard", "os":"OS X", "browser_version":"17.0", "url":"https://github.com/404", "browser":"firefox"}  # Put desired device info from where you want to take a snapshot

try:
    #make a user object
    u = User(username, key)
    
    #make a device object
    device = Device(args)
    
    #make a shutter object
    shutter = Shutter(test_url, browsers_url, worker_url)           
    shutter.test_connection(u.username, u.key)                         # test your connection with browserstack
    shutter.get_browsers(u.username, u.key)                            
    shutter.make_worker(u.username, u.key, device.get_device_info())   
    print "Waiting for worker to get a terminal access..."             # wait for 10-15 seconds as it takes time to get 
    sleep(15)                                                          # a terminal.
    shutter.get_screenshot(u.username, u.key)                          
except Exception as e:
    print "Something went wrong."
    print str(e)                                                       # this will help to understand if the program halts. 

finally:
    
    shutter.delete_worker(u.username, u.key)