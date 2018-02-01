from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.schema.UserSchema import UserSchema

class SchemaClient(ApiClient):

    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1/meta/schemas'
        ApiClient.__init__(self, *args, **kwargs)

    # CRUD

    def add_property_to_user_schema(self, user_custom_schema):
        """Adds a custom property to the user profile

        :param user_schema: the custom propery to add
        :type user_schema: UserProfileCustomSubschema
        :rtype: UserSchema
        """
        response = ApiClient.post_path(self, '/user/default', user_custom_schema)
        return Utils.deserialize(response.text, UserSchema)