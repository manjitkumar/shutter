
# Class Device to store your device arguments.

class Device:
    def __init__(self, args):
        '''
        (os, os_version, browser, browser_version, url)
        
        Define os, os_version, browser, browser_version and url on you want to 
        capture a shot.
        '''
        self.args = args       
        print 'Device arguments saved.'
        return
    
    def get_device_info(self):
        '''
        () -> {self.args}
        
        This method returns a dictionary consist of your desired  device info as 
        passed in Device object creation.
        '''
        return self.args
        