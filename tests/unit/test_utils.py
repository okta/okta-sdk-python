from okta.utils import convert_absolute_url_into_relative_url


def test_convert_absolute_url_into_relative_url():
    absolute_url = 'https://test.okta.com/api/v1/users'
    relative_url = '/api/v1/users'
    assert relative_url == convert_absolute_url_into_relative_url(absolute_url)

    absolute_url = 'https://test.okta.com/api/v1/users?activate=false'
    relative_url = '/api/v1/users?activate=false'
    assert relative_url == convert_absolute_url_into_relative_url(absolute_url)
