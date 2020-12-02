from okta import utils


def test_to_snake_case():
    assert utils.to_snake_case('string') == 'string'
    assert utils.to_snake_case('CamelCaseStr') == 'camel_case_str'
    assert utils.to_snake_case('lowerCamelCaseStr') == 'lower_camel_case_str'
    assert utils.to_snake_case('snake_case_str') == 'snake_case_str'


def test_to_lower_camel_case():
    assert utils.to_lower_camel_case('string') == 'string'
    assert utils.to_lower_camel_case('CamelCaseStr') == 'camelCaseStr'
    assert utils.to_lower_camel_case('lowerCamelCaseStr') == 'lowerCamelCaseStr'
    assert utils.to_lower_camel_case('snake_case_str') == 'snakeCaseStr'
