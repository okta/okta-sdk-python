import sys
import yaml  # Using PyYAML


# --- Step 1: Create a custom string class to "mark" strings for quoting ---
class QuotedString(str):
    pass


# --- Step 2: Create a custom function to format ONLY our custom string class ---
def quoted_str_presenter(dumper, data):
    """Tells PyYAML to represent instances of QuotedString as a double-quoted scalar."""
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')


# --- Step 3: Register the custom function for our custom class ---
# This ensures that only strings wrapped in QuotedString() will get quotes.
yaml.SafeDumper.add_representer(QuotedString, quoted_str_presenter)


def get_formatted_list(dict_object):
    """
    Converts a dictionary to a list of dictionaries with 'key' and 'value' pairs.
    The keys are wrapped in QuotedString to ensure they are dumped with quotes.
    """
    return [{"key": k, "value": v}  for k, v in dict_object.items()]


def extract_discriminator_mappings(spec, base_model, uppercase_keys=False):
    """
    Extracts discriminator mappings and wraps the key/value strings in QuotedString
    to ensure they are dumped with quotes.
    """
    mappings = {}
    schemas = spec.get('components', {}).get('schemas', {})

    base_model_schema = schemas.get(base_model, {})
    discriminator = base_model_schema.get('discriminator')

    if discriminator and 'mapping' in discriminator:
        for key, ref_path in discriminator['mapping'].items():
            model_name = ref_path.split('/')[-1]
            processed_key = key.upper() if uppercase_keys else key

            # --- Step 4: Wrap the specific values in our custom class ---
            mappings[QuotedString(processed_key)] = QuotedString(model_name)

    # Convert to the desired list-of-dictionaries format
    # formatted_list = [{"key": k, "value": v} for k, v in mappings.items()]
    # return formatted_list
    return mappings

def get_constants_properties(spec):
    # --- Generate the data from the OpenAPI spec ---
    generated_properties = {
        "app_sign_on_to_model": get_formatted_list(extract_discriminator_mappings(spec, "Application", uppercase_keys=True)),
        "factor_type_to_factor": get_formatted_list(extract_discriminator_mappings(spec, "UserFactor", uppercase_keys=True)),
        "policy_type_to_model": get_formatted_list(extract_discriminator_mappings(spec, "Policy", uppercase_keys=True)),
        "policy_rule_to_model": get_formatted_list(extract_discriminator_mappings(spec, "PolicyRule", uppercase_keys=True)),
        # This data is static and also needs its values wrapped for quoting
        "app_name_to_model": [
            {"key": QuotedString("template_swa"), "value": QuotedString("SwaApplication")},
            {"key": QuotedString("template_swa3field"), "value": QuotedString("SwaThreeFieldApplication")}
        ]
    }
    return generated_properties


def get_models_properties(spec):
    """
    Extracts model properties from the OpenAPI spec.
    This function is a placeholder for future enhancements.
    """
    model_properties = []
    models = [("Application", True), ("UserFactor", False), ("Policy", True), ("PolicyRule", True)]
    for model in models:
        model_mappings = extract_discriminator_mappings(spec, model[0], uppercase_keys=model[1])
        for key, value in model_mappings.items():
            model_properties.append({"key": value, "value": key})
    return {"model_properties": model_properties}


import yaml
import re


def to_snake_case(name):
    """Converts camelCase or PascalCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    # Special handling for names that are just uppercase like 'IWA'
    if name.isupper():
        return name.lower()
    return name.lower()


def to_pascal_case(name):
    """Converts snake_case or camelCase to PascalCase."""
    if '_' in name:
        return "".join(word.capitalize() for word in name.split('_'))
    return name[0].upper() + name[1:]


def to_camel_case(name):
    """Converts snake_case to camelCase."""
    if '_' not in name:
        return name
    parts = name.split('_')
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


def preprocess_for_mustache(spec):
    """
    Processes the OpenAPI spec to create a data model suitable for the
    Mustache template engine.
    """
    models_data = []
    schemas = spec.get('components', {}).get('schemas', {})

    for model_name, schema in schemas.items():
        model_data = {
            'classname': model_name,
            'hasProperties': bool(schema.get('properties')),
            'isExtensibleProfile': model_name in ["UserProfile", "GroupProfile"],
            'properties': []
        }

        # Add basic attributes for extensible profiles
        if model_data['isExtensibleProfile']:
            base_ref = next(
                (item['$ref'] for item in schema.get('properties', {}).get('profile', {}).get('allOf', []) if
                 '#/definitions/base' in item['$ref']), None)
            if base_ref:
                base_def_name = base_ref.split('/')[-1]
                base_properties = schema.get('definitions', {}).get(base_def_name, {}).get('properties', {})
                model_data['basicAttributes'] = list(base_properties.keys())

        properties = schema.get('properties', {})
        for prop_name, prop_schema in properties.items():
            prop_data = {
                'name': prop_name,
                'snakeCaseName': to_snake_case(prop_name),
                'camelCaseName': to_camel_case(prop_name),
                'isArray': prop_schema.get('type') == 'array',
                'isRef': '$ref' in prop_schema or ('items' in prop_schema and '$ref' in prop_schema['items']),
                'hasDefault': 'default' in prop_schema,
                'default': prop_schema.get('default'),
                'isSpecialProp': prop_name in ["$schema", "_links"],
                'model': None,
                'pascalCaseModel': None,
                'snakeCaseModel': None,
                'itemType': None,
                'isEnum': False  # Simplified for this example
            }

            ref_path = None
            if '$ref' in prop_schema:
                ref_path = prop_schema['$ref']
            elif prop_data['isArray'] and '$ref' in prop_schema.get('items', {}):
                ref_path = prop_schema['items']['$ref']

            if ref_path:
                model = ref_path.split('/')[-1]
                prop_data['model'] = model
                prop_data['pascalCaseModel'] = to_pascal_case(model)
                prop_data['snakeCaseModel'] = to_snake_case(model)

                # Determine itemType for collections
                if prop_data['isArray']:
                    prop_data['itemType'] = prop_data['pascalCaseModel']

            # Simplified check for enums based on presence of 'enum' key
            if 'enum' in prop_schema:
                prop_data['isEnum'] = True

            model_data['properties'].append(prop_data)

        models_data.append(model_data)

    return {'models': models_data}


def main():
    if len(sys.argv) != 3:
        print("Usage: python update_config.py <path_to_openapi.yaml> <path_to_config.yaml>")
        sys.exit(1)

    openapi_spec_path = sys.argv[1]
    config_yaml_path = sys.argv[2]

    # Load the OpenAPI specification
    with open(openapi_spec_path, 'r') as f:
        spec = yaml.safe_load(f)

    constants_properties = get_constants_properties(spec)
    models_properties = get_models_properties(spec)
    models_init_data = preprocess_for_mustache(spec)
    import pdb; pdb.set_trace()
    # --- Read, Update, and Write the config.yaml using PyYAML ---
    try:
        with open(config_yaml_path, 'r') as f:
            config_data = yaml.safe_load(f)
            if not config_data:
                config_data = {}
    except FileNotFoundError:
        config_data = {}

    if 'additionalProperties' not in config_data:
        config_data['additionalProperties'] = {}

    config_data['additionalProperties'].update(constants_properties)
    config_data['additionalProperties'].update(models_properties)

    # Write back to the file using the custom SafeDumper
    with open(config_yaml_path, 'w') as f:
        # We use SafeDumper to enable the custom string quoting
        yaml.dump(config_data, f, Dumper=yaml.SafeDumper, sort_keys=False, indent=2)

    print(f"Successfully updated '{config_yaml_path}' with selective quoting.")


if __name__ == "__main__":
    main()