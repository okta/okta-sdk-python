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
    formatted_list = [{"key": k, "value": v} for k, v in mappings.items()]
    return formatted_list


def main():
    if len(sys.argv) != 3:
        print("Usage: python update_config.py <path_to_openapi.yaml> <path_to_config.yaml>")
        sys.exit(1)

    openapi_spec_path = sys.argv[1]
    config_yaml_path = sys.argv[2]

    # Load the OpenAPI specification
    with open(openapi_spec_path, 'r') as f:
        spec = yaml.safe_load(f)

    # --- Generate the data from the OpenAPI spec ---
    generated_properties = {
        "app_sign_on_to_model": extract_discriminator_mappings(spec, "Application", uppercase_keys=True),
        "factor_type_to_factor": extract_discriminator_mappings(spec, "UserFactor", uppercase_keys=True),
        "policy_type_to_model": extract_discriminator_mappings(spec, "Policy", uppercase_keys=True),
        "policy_rule_to_model": extract_discriminator_mappings(spec, "PolicyRule", uppercase_keys=True),
        # This data is static and also needs its values wrapped for quoting
        "app_name_to_model": [
            {"key": QuotedString("template_swa"), "value": QuotedString("SwaApplication")},
            {"key": QuotedString("template_swa3field"), "value": QuotedString("SwaThreeFieldApplication")}
        ]
    }

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

    config_data['additionalProperties'].update(generated_properties)

    # Write back to the file using the custom SafeDumper
    with open(config_yaml_path, 'w') as f:
        # We use SafeDumper to enable the custom string quoting
        yaml.dump(config_data, f, Dumper=yaml.SafeDumper, sort_keys=False, indent=2)

    print(f"Successfully updated '{config_yaml_path}' with selective quoting.")


if __name__ == "__main__":
    main()