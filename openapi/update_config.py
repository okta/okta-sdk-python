# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import sys

import yaml  # Using PyYAML


# --- Step 1: Create a custom string class to "mark" strings for quoting ---
class QuotedString(str):
    pass


# --- Step 2: Create a custom function to format ONLY our custom string class ---
def quoted_str_presenter(dumper, data):
    """Tells PyYAML to represent instances of QuotedString as a double-quoted scalar."""
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


# --- Step 3: Register the custom function for our custom class ---
# This ensures that only strings wrapped in QuotedString() will get quotes.
yaml.SafeDumper.add_representer(QuotedString, quoted_str_presenter)


def get_formatted_list(dict_object):
    """
    Converts a dictionary to a list of dictionaries with 'key' and 'value' pairs.
    The keys are wrapped in QuotedString to ensure they are dumped with quotes.
    """
    return [{"key": k, "value": v} for k, v in dict_object.items()]


def extract_discriminator_mappings(spec, base_model, uppercase_keys=False):
    """
    Extracts discriminator mappings and wraps the key/value strings in QuotedString
    to ensure they are dumped with quotes.
    """
    mappings = {}
    schemas = spec.get("components", {}).get("schemas", {})

    base_model_schema = schemas.get(base_model, {})
    discriminator = base_model_schema.get("discriminator")

    if discriminator and "mapping" in discriminator:
        for key, ref_path in discriminator["mapping"].items():
            model_name = ref_path.split("/")[-1]
            processed_key = key.upper() if uppercase_keys else key

            # --- Step 4: Wrap the specific values in our custom class ---
            if base_model == "UserFactor" and ":" in processed_key:
                processed_key = processed_key.replace(":", "_COLON_")
            mappings[QuotedString(processed_key)] = QuotedString(model_name)
    return mappings


def get_constants_properties(spec):
    # --- Generate the data from the OpenAPI spec ---
    generated_properties = {
        "app_sign_on_to_model": get_formatted_list(
            extract_discriminator_mappings(spec, "Application", uppercase_keys=True)
        ),
        "factor_type_to_factor": get_formatted_list(
            extract_discriminator_mappings(spec, "UserFactor", uppercase_keys=True)
        ),
        "policy_type_to_model": get_formatted_list(
            extract_discriminator_mappings(spec, "Policy", uppercase_keys=True)
        ),
        "policy_rule_to_model": get_formatted_list(
            extract_discriminator_mappings(spec, "PolicyRule", uppercase_keys=True)
        ),
        # This data is static and also needs its values wrapped for quoting
    }
    return generated_properties


def main():
    if len(sys.argv) != 3:
        print(
            "Usage: python update_config.py <path_to_openapi.yaml> <path_to_config.yaml>"
        )
        sys.exit(1)

    openapi_spec_path = sys.argv[1]
    config_yaml_path = sys.argv[2]

    # Load the OpenAPI specification
    with open(openapi_spec_path, "r") as f:
        spec = yaml.safe_load(f)

    constants_properties = get_constants_properties(spec)
    # --- Read, Update, and Write the config.yaml using PyYAML ---
    try:
        with open(config_yaml_path, "r") as f:
            config_data = yaml.safe_load(f)
            if not config_data:
                config_data = {}
    except FileNotFoundError:
        config_data = {}

    if "additionalProperties" not in config_data:
        config_data["additionalProperties"] = {}

    config_data["additionalProperties"].update(constants_properties)

    # Write back to the file using the custom SafeDumper
    with open(config_yaml_path, "w") as f:
        # We use SafeDumper to enable the custom string quoting
        yaml.dump(config_data, f, Dumper=yaml.SafeDumper, sort_keys=False, indent=2)

    print(f"Successfully updated '{config_yaml_path}' with selective quoting.")


if __name__ == "__main__":
    main()
