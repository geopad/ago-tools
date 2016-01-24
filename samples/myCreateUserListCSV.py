# Requires admin role.
import csv, time
from agoTools.admin import Admin

##username = ''
##password = ''
##portalName = 'devumich'

username = ''
password = ''
portalName = 'umich'

portal = 'https://' + portalName + '.maps.arcgis.com'

agoAdmin = Admin(username,portal,password) # Replace <username> with your admin username.
users = agoAdmin.getUsers()
roles = agoAdmin.getRoles()
#Make a dictionary of the roles so we can convert custom roles from their ID to their associated name.
roleLookup = {}
for role in roles:
    roleLookup[role["id"]] = role["name"]

outputFile = 'c:/temp/' + portalName + time.strftime("%Y-%m-%d-%H%M%S",time.gmtime()) + '.csv'

with open(outputFile, 'wb') as output:
    
##    dataWriter = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
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
        #set fields
        if u'disabled' in user: disabled = str(user[u'disabled']).encode('utf-8')
        else: disabled = ""
        if u'storageQuota' in user: storageQuota = str(user[u'storageQuota']).encode('utf-8')
        else: storageQuota = ""
        if u'storageUsage' in user: storageUsage = str(user[u'storageUsage']).encode('utf-8')
        else: storageUsage = ""
        if u'assignedCredits' in user: assignedCredits = str(user[u'assignedCredits']).encode('utf-8')
        else: assignedCredits = ""
        if u'culture' in user:
            if user[u'culture'] is None: culture = ""
            else: culture = user[u'culture'].encode('utf-8')
        else: culture = ""
        if u'favGroupId' in user: favGroupId = user[u'favGroupId'].encode('utf-8')
        else: favGroupId = ""
        if u'access' in user: access = user[u'access'].encode('utf-8')
        else: access = ""
        if u'role' in user:
            #get role name from the id. If it's not in the roles, it's one of the standard roles so just use it.
            roleID = user[u'role']
            roleName = roleLookup.get(roleID,roleID)
        else: roleName = ""
        if u'provider' in user: provider=user[u'provider'].encode('utf-8')
        else: provider = ""
        if u'units' in user: units=user[u'units'].encode('utf-8')
        else: units = ""
        if u'mfaEnabled' in user: mfaEnabled = str(user[u'mfaEnabled']).encode('utf-8')
        else: mfaEnabled = ""
        if u'email' in user: email = user[u'email'].encode('utf-8')
        else: email = ""
        if u'username' in user: username = user[u'username'].encode('utf-8')
        else: username = ""
        if u'description' in user:
            if user[u'description'] is None: description = ""
            else: description = user[u'description'].encode('utf-8')
        else: description = ""
        if u'tags' in user:
            tagList = u','.join(user[u'tags'])
            if tagList == u',': tags = ""
            else: tags = tagList.encode('utf-8')
        else: tags = ""
        if u'groups' in user:
            groupList = u','.join(user[u'groups'])
            if groupList == u',': groups = ""
            else: groups = groupList.encode('utf-8')
        else: groups = ""
        if u'fullName' in user: fullName = user[u'fullName'].encode('utf-8')
        else: fullName = ""
        if u'idpUsername' in user:
            if user[u'idpUsername'] is None: idpUsername = ""
            else: idpUsername = user[u'idpUsername'].encode('utf-8')
        else: idpUsername = ""
        if u'firstName' in user: firstName = user[u'firstName'].encode('utf-8')
        else:firstName = ""
        if u'userType' in user: userType = user[u'userType'].encode('utf-8')
        else: userType = ""
        if u'lastName' in user: lastName = user[u'lastName'].encode('utf-8')
        else: lastName = ""
        if u'region' in user:
            if user[u'region'] is None: region = ""
            else: region = user[u'region'].encode('utf-8')
        else: region = ""
        if u'created' in user: created = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'created']/1000))
        else: created = ""
        if u'modified' in user: modified = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'modified']/1000))
        else: modified = ""
        if u'thumbnail' in  user:
            if user[u'thumbnail'] is None: thumbnail = ""
            else: thumbnail = user[u'thumbnail'].encode('utf-8')
        else: thumbnail = ""
        if u'availableCredits' in user: availableCredits = str(user[u'availableCredits']).encode('utf-8')
        else: availableCredits = ""
        if u'orgId' in user: orgId = user[u'orgId'].encode('utf-8')
        else: orgId = ""
        if u'preferredView' in user:
            if user[u'preferredView'] is None: preferredView = ""
            else: preferredView = user[u'preferredView'].encode('utf-8')
        else: preferredView = ""
        if u'lastLogin' in user: lastLogin = time.strftime("%m/%d/%Y %I:%M:%S %p",time.gmtime(user[u'lastLogin']/1000))
        else: lastLogin = ""
        if u'validateUserProfile' in user: validateUserProfile = str(user[u'validateUserProfile']).encode('utf-8')
        else: validateUserProfile = ""
                        
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
