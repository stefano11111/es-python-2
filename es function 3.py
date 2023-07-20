# to be able to use os functions
# import os then call getlogin method of the module
# then assign the output to user variable and print the user

import os 
user=os.getlogin()
print(user)
