
# Class User to store User credentials.

class User:
    def __init__(self, username, key):
        '''
        (username, key) -> returns nothing
        This object's creation requires a browserstack's automate username and 
        browserstack's automate pass-key key as input.
        '''
        self.username = username
        self.key = key
        
        print "User's credentials saved"
        return 