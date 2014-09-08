import requests                   # to make http requests to broswerstack's APIs
import json                       # to convert data into json format
from PIL import Image             
from StringIO import StringIO

class Shutter():
    def __init__(self, test_url, browsers_url, worker_url):
        '''
           (test_url, browsers_url, worker_url)
           This method creates a Shutter object and requires a test_url to 
           browserstack's api, another url to get all available browsers info
           and a worker_url which is used to make a worker.
        
        '''
        
        self.test_url = test_url
        self.browsers_url = browsers_url
        self.worker_url = worker_url
        self.worker_id = ''
        self.browsers = {}
        
    def test_connection(self, username, key):
        '''
        (username, key) -> prints HTTP response
        
        This method trying to connect to Browserstacks api ver 3
        and prints the response code on terminal.
        
        '''
        
        print 'testing connection...'
        make_connection_response = requests.get(self.test_url, auth=(username, key))
        print make_connection_response
        
    def get_browsers(self, username, key):
        '''
        (username, key) -> {available browsers information}
        
        This method is to get all the required information about available browsers
        with available platforms/OS. It returns a json object consist of all browsers
        information.
        
        '''
        print 'getting browsers list...'
        browser_list_response = requests.get(self.browsers_url, auth=(username, key))
        print browser_list_response
        self.broswers = json.loads(browser_list_response.text)
        return self.browsers
        
    def make_worker(self, username, key, args):
        '''
        (username, key, args) -> worker_id
        
        This method create a worker on your request with the device information you
        provide in args and returns a unique worker id.
        '''
        
        print 'making a worker for you...'
        worker_response = requests.post(self.worker_url, params=args, auth=(username, key))
        print worker_response
        worker_id = json.loads(worker_response.text)['id']
        self.worker_id = worker_id
        print 'Congratulation your worker is ready with id = '+str(worker_id)
        return self.worker_id
        
        
    def get_screenshot(self, username, key):
        '''
        (username, key) -> saves an image on your filesystem
        
        This method take username and authentication key as input and take a snapshot 
        of the webpage on a requested browser and plateform in the worker. This image 
        file will be saved into your file system.
        '''           
        print 'trying to capture screeenshot...'
        screenshot_url = 'http://api.browserstack.com/3/worker/'+str(self.worker_id)+'/screenshot.png'
        screenshot_response = requests.get(screenshot_url, auth=(username, key))
        print screenshot_response
        
        img = Image.open(StringIO(screenshot_response.content))  #open and save image object
        img.save('git404','png')
             
    def delete_worker(self, username, key):
        '''
        This method take username and authentication key as input and deletes the 
        worker from your browserstack's automate account. It is recomended to delete 
        the worker when it's job is done or use a timeout value which is by default 300s.
        '''
        print 'deleting a worker...'
        delete_worker_response = requests.delete("http://api.browserstack.com/3/worker/"+str(self.worker_id), auth=(username, key))
        print delete_worker_response
        