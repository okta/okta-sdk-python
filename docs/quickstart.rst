---------------
Quickstart
---------------

Create a client
===============
::

    from okta import UsersClient
    
    usersClient = UsersClient("https://example.okta.com", "EXAMPLE_KEY")

Create a user
=============
::

    from okta.models.user import User # Include with other imports above

    user = User(login='example@example.com',
    		email='example@example.com',
    		firstName='Saml',
    		lastName='Jackson')

    user = usersClient.create_user(user, activate=False)

Activate a user
===============
::

    usersClient.activate_user(user)

Loop through a list
===================
::

    users = self.client.get_paged_users(limit=1)
    
    first_page_hit = subsequent_page_hit = False
    
    for user in users.result:
        first_page_hit = True
        # Do something
    
    while not users.is_last_page():
        users = self.client.get_paged_users(url=users.next_url)
        for user in users.result:
            subsequent_page_hit = True
            # Do something