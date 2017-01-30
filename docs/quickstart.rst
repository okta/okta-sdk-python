---------------
Quickstart
---------------

Create a client
===============
::

    from okta import UsersClient
    # http://developer.okta.com/docs/api/getting_started/getting_a_token.html
    usersClient = UsersClient('https://example.oktapreview.com/',
                              '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')

Create a user
=============
::

    from okta import UsersClient
    # http://developer.okta.com/docs/api/getting_started/getting_a_token.html
    usersClient = UsersClient('https://example.oktapreview.com/',
                              '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')

    new_user = User(login='example@example.com',
                    email='example@example.com',
                    firstName='Saml',
                    lastName='Jackson')
    user = usersClient.create_user(new_user, activate=False)

Activate a user
===============
::
    from okta import UsersClient
    from okta.models.user import User
    # http://developer.okta.com/docs/api/getting_started/getting_a_token.html
    usersClient = UsersClient('https://example.oktapreview.com/',
                              '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')

    user = usersClient.get_user('example@example.com')
    usersClient.activate_user(user.id)

Loop through a list
===================
::


    from okta import UsersClient
    # http://developer.okta.com/docs/api/getting_started/getting_a_token.html
    usersClient = UsersClient('https://example.oktapreview.com/',
                              '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')
    
    users = usersClient.get_paged_users()
    while True:
        for user in users.result:
            print u"First Name: {}".format(user.profile.firstName)
            print u"Last Name:  {}".format(user.profile.lastName)
            print u"Login:      {}".format(user.profile.login)
            print u"User ID:    {}\n".format(user.id)
        if not users.is_last_page():
            # Keep on fetching pages of users until the last page
            users = usersClient.get_paged_users(url=users.next_url)
        else:
            break
