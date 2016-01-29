# Requires credentials with admin role on AGOL instance.
# Supply credentials in separate file outside of source control: ./credentials.py

import csv
import sys
import time

from agoTools.admin import Admin

# Obtain AGOL instance credentials from a non-repo file in this directory.
try:
    from credentials import *
except:
    print "./credentials.py missing"
    sys.exit(0)

# Generate AGOL instance URL from AGOL subdomain.
portalURL = 'https://' + agolSubdomain + '.maps.arcgis.com'

# Specify credit quota
creditQuota = 5000

# Get users
agolAdmin = Admin(username,portalURL,password) # Replace <username> with your admin username.
users = agolAdmin.getUsers()

# Look for users where assignedCredits is -1, and set a quota for them.
for user in users:

    # Does the user have an assignedCredits value assigned? If not, then there is a problem...
    if u'assignedCredits' in user:
        # Has no credit quota been set for the user? (-1 means no quota.)
        if user[u'assignedCredits'] = -1:
            # Set credit quota
            print u'Setting creit quota for' + user[u'username']
            
    else:
        print user[u'username'] + u'has no assignedCredits value!'
