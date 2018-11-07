#!/usr/bin/env python
# Mel 2018-10-26 - search employees in AD ldap

import ldap3
import sys

# be sure and change the next 2 lines from example.com and YourPasswordHere
server=ldap3.Server('ad.morsco.com',get_info=ldap3.ALL)
conn=ldap3.Connection(server, user="ad\\ldap", password='morscoLD@P',auto_bind=True)
# also change search_base from example.com
# searchParameters = { 'search_base': 'dc=ad,dc=morsco,dc=com',
#                      'search_filter': '(&(objectClass=Person))',
#                      'attributes': ['cn', 'givenName', 'displayName', 'sn', 'name', 'sAMAccountName', 'userPrincipalName',
#                      'mail', 'employeeID', 'manager', 'department', 'company', 'distinguishedName', 'title',
#                      'physicalDeliveryOfficeName', 'memberOf', 'description' ],
#                      'paged_size': 10 }

searchParameters = { 'search_base': 'dc=ad,dc=morsco,dc=com',
                     'search_filter': '(&(objectClass=Person))',
                     'attributes': ['sAMAccountName', 'memberOf'],
                     'paged_size': 10 }

while True:
    conn.search(**searchParameters)
    for entry in conn.entries:
        for argument in sys.argv[1:]:
            if argument in entry['sAMAccountName']:
                # num = 1
                # for x in entry['memberOf']:
                #     print("%d -> %s" % (num, x))
                #     num += 1
                # print(entry['memberOf'])
                if entry['memberOf'][131] is "CN=HDesk,CN=Users,DC=ad,DC=morsco,DC=com":
                    print("In the help desk")
                else:
                    print(entry['memberOf'][131])
    cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
    if cookie:
        searchParameters['paged_cookie'] = cookie
    else:
        break