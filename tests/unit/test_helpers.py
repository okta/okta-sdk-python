from okta import helpers


def test_to_snake_case():
    assert helpers.to_snake_case('string') == 'string'
    assert helpers.to_snake_case('CamelCaseStr') == 'camel_case_str'
    assert helpers.to_snake_case('lowerCamelCaseStr') == 'lower_camel_case_str'
    assert helpers.to_snake_case('snake_case_str') == 'snake_case_str'


def test_to_lower_camel_case():
    assert helpers.to_lower_camel_case('string') == 'string'
    assert helpers.to_lower_camel_case('CamelCaseStr') == 'camelCaseStr'
    assert helpers.to_lower_camel_case('lowerCamelCaseStr') == 'lowerCamelCaseStr'
    assert helpers.to_lower_camel_case('snake_case_str') == 'snakeCaseStr'
