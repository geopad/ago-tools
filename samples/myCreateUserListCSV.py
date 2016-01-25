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

agolAdmin = Admin(username,portalURL,password) # Replace <username> with your admin username.
users = agolAdmin.getUsers()
roles = agolAdmin.getRoles()

# Make a dictionary of the roles so we can convert custom roles from their ID to their associated name.
roleLookup = {}
for role in roles:
    roleLookup[role[u'id']] = role[u'name']
    
# Designate output file for CSV user list.
# TODO: Check that directory exists, and that file name isn't already in use.
outputFile = u'c:/temp/' + agolSubdomain + time.strftime("%Y-%m-%d-%H%M%S",time.gmtime()) + u'.csv'
with open(outputFile, 'wb') as output:
    
    dataWriter = csv.writer(output, dialect='excel' )
    
    # Write header row.
    dataWriter.writerow([u'disabled',
                         u'storageQuota',
                         u'storageUsage',
                         u'assignedCredits',
                         u'culture',
                         u'favGroupId',
                         u'access',
                         u'role',
                         u'provider',
                         u'units',
                         u'mfaEnabled',
                         u'email',
                         u'username',
                         u'description',
                         u'tags',
                         u'groups',
                         u'fullName',
                         u'idpUsername',
                         u'firstName',
                         u'userType',
                         u'lastName',
                         u'region',
                         u'created',
                         u'modified',
                         u'thumbnail',
                         u'availableCredits',
                         u'orgId',
                         u'preferredView',
                         u'lastLogin',
                         u'validateUserProfile'])
    
    # Write user data.
    for user in users:

        if u'disabled' in user: disabled = str(user[u'disabled']).encode('utf-8')
        else: disabled = u''
        if u'storageQuota' in user: storageQuota = str(user[u'storageQuota']).encode('utf-8')
        else: storageQuota = u''
        if u'storageUsage' in user: storageUsage = str(user[u'storageUsage']).encode('utf-8')
        else: storageUsage = u''
        if u'assignedCredits' in user: assignedCredits = str(user[u'assignedCredits']).encode('utf-8')
        else: assignedCredits = u''
        if u'culture' in user:
            if user[u'culture'] is None: culture = u''
            else: culture = user[u'culture'].encode('utf-8')
        else: culture = u''
        if u'favGroupId' in user: favGroupId = user[u'favGroupId'].encode('utf-8')
        else: favGroupId = u''
        if u'access' in user: access = user[u'access'].encode('utf-8')
        else: access = u''
        if u'role' in user:
            #get role name from the id, using role dictionary set above. If it's not in the roles, it's one of the standard roles so just use it.
            roleID = user[u'role']
            roleName = roleLookup.get(roleID,roleID)
        else: roleName = u''
        if u'provider' in user: provider=user[u'provider'].encode('utf-8')
        else: provider = u''
        if u'units' in user: units=user[u'units'].encode('utf-8')
        else: units = u''
        if u'mfaEnabled' in user: mfaEnabled = str(user[u'mfaEnabled']).encode('utf-8')
        else: mfaEnabled = u''
        if u'email' in user: email = user[u'email'].encode('utf-8')
        else: email = u''
        if u'username' in user: username = user[u'username'].encode('utf-8')
        else: username = u''
        if u'description' in user:
            if user[u'description'] is None: description = u''
            else: description = user[u'description'].encode('utf-8')
        else: description = u''
        if u'tags' in user:
            tagList = u','.join(user[u'tags'])
            if tagList == u',': tags = u''
            else: tags = tagList.encode('utf-8')
        else: tags = u''
        if u'groups' in user:
            groupList = u','.join(user[u'groups'])
            if groupList == u',': groups = u''
            else: groups = groupList.encode('utf-8')
        else: groups = u''
        if u'fullName' in user: fullName = user[u'fullName'].encode('utf-8')
        else: fullName = u''
        if u'idpUsername' in user:
            if user[u'idpUsername'] is None: idpUsername = u''
            else: idpUsername = user[u'idpUsername'].encode('utf-8')
        else: idpUsername = u''
        if u'firstName' in user: firstName = user[u'firstName'].encode('utf-8')
        else:firstName = u''
        if u'userType' in user: userType = user[u'userType'].encode('utf-8')
        else: userType = u''
        if u'lastName' in user: lastName = user[u'lastName'].encode('utf-8')
        else: lastName = u''
        if u'region' in user:
            if user[u'region'] is None: region = u''
            else: region = user[u'region'].encode('utf-8')
        else: region = u''
        if u'created' in user: created = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'created']/1000))
        else: created = u''
        if u'modified' in user: modified = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'modified']/1000))
        else: modified = u''
        if u'thumbnail' in  user:
            if user[u'thumbnail'] is None: thumbnail = u''
            else: thumbnail = user[u'thumbnail'].encode('utf-8')
        else: thumbnail = u''
        if u'availableCredits' in user: availableCredits = str(user[u'availableCredits']).encode('utf-8')
        else: availableCredits = u''
        if u'orgId' in user: orgId = user[u'orgId'].encode('utf-8')
        else: orgId = u''
        if u'preferredView' in user:
            if user[u'preferredView'] is None: preferredView = u''
            else: preferredView = user[u'preferredView'].encode('utf-8')
        else: preferredView = u''
        if u'lastLogin' in user: lastLogin = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'lastLogin']/1000))
        else: lastLogin = u''
        if u'validateUserProfile' in user: validateUserProfile = str(user[u'validateUserProfile']).encode('utf-8')
        else: validateUserProfile = u''
                        
        dataWriter.writerow([disabled,
                             storageQuota,
                             storageUsage,
                             assignedCredits,
                             culture,
                             favGroupId,
                             access,
                             roleName,
                             provider,
                             units,
                             mfaEnabled,
                             email,
                             username,
                             description,
                             tags,
                             groups,
                             fullName,
                             idpUsername,
                             firstName,
                             userType,
                             lastName,
                             region,
                             created,
                             modified,
                             thumbnail,
                             availableCredits,
                             orgId,
                             preferredView,
                             lastLogin,
                             validateUserProfile
                             ])
