Brach of oktasdk-python by DiabolusBR
=======================
Added some features to the existing API:

#List users in Application
usersInApp = AppInstanceClient.get_app_users("id_of_application")

#List groups in Application
groupsinapp = AppInstanceClient.get_app_groups("id_of_application")

#List all users in a group
userlist = UserGroupsClient.get_users_by_group("id_of_group")

This SDK allows managing an Okta instance via Python.
