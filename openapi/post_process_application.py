#!/usr/bin/env python3
"""
Post-processing script to add unknown discriminator handling ONLY to Application model.
This runs after SDK generation to add the specific logic without affecting other models.

Usage: python3 post_process_application.py
"""

import re
import sys
from pathlib import Path

# Paths
APPLICATION_FILE = Path(__file__).parent.parent / 'okta' / 'models' / 'application.py'

def check_if_already_processed():
    """Check if the file has already been processed"""
    content = APPLICATION_FILE.read_text()
    return '_original_sign_on_mode: Optional[str] = None' in content

def add_original_field():
    """Add the _original_sign_on_mode field to the Application class"""
    content = APPLICATION_FILE.read_text()

    # Pattern: after links field, before __properties
    pattern = r'(    links: Optional\[ApplicationLinks\] = Field\(default=None, alias="_links"\)\n)(    __properties: ClassVar)'

    if not re.search(pattern, content):
        print("⚠️  Warning: Could not find insertion point for _original_sign_on_mode field")
        return False

    replacement = r"\1    # Store the original sign-on mode value when it's not in the enum\n    _original_sign_on_mode: Optional[str] = None\n\2"
    content = re.sub(pattern, replacement, content)

    APPLICATION_FILE.write_text(content)
    print("✓ Added _original_sign_on_mode field")
    return True

def add_to_dict_logic():
    """Add logic to return original sign-on mode in to_dict method"""
    content = APPLICATION_FILE.read_text()

    # Pattern: before "return _dict" in to_dict method
    pattern = r"(        # override the default output from pydantic by calling `to_dict\(\)` of links\n        if self\.links:\n            if not isinstance\(self\.links, dict\):\n                _dict\['_links'\] = self\.links\.to_dict\(\)\n            else:\n                _dict\['_links'\] = self\.links\n\n)(        return _dict)"

    if not re.search(pattern, content):
        print("⚠️  Warning: Could not find insertion point for to_dict logic")
        return False

    replacement = r"\1        # If we have an original sign-on mode (was unknown), return it instead of OTHER\n        if self._original_sign_on_mode:\n            _dict['signOnMode'] = self._original_sign_on_mode\n\2"
    content = re.sub(pattern, replacement, content)

    APPLICATION_FILE.write_text(content)
    print("✓ Added to_dict logic for original sign-on mode")
    return True

def add_from_dict_logic():
    """Add logic to handle unknown sign-on modes in from_dict method"""
    content = APPLICATION_FILE.read_text()

    # Pattern: Find where Application class processes itself (first occurrence in the mappedModels loop)
    # We need to find: if object_type == 'Application': ... if object_type == cls.__name__: return cls.model_validate(obj)
    # Use a more specific pattern that only matches the first occurrence
    pattern = r"(        if object_type == 'Application':\n            # Check if the discriminator maps to the same class to avoid infinite recursion\n            if object_type == cls\.__name__:\n)(                return cls\.model_validate\(obj\)\n)(            return models\.Application\.from_dict\(obj\))"

    # Check if already processed
    if "# Handle unknown sign-on modes" in content:
        print("  → Already processed (skipping duplicate addition)")
        return True

    if not re.search(pattern, content):
        print("⚠️  Warning: Could not find insertion point for from_dict logic")
        return False

    replacement = r'''\1                # Handle unknown sign-on modes
                original_discriminator = obj.get(cls.__discriminator_property_name)
                if original_discriminator and original_discriminator not in cls.__discriminator_value_class_map:
                    # Store the original value and replace with OTHER
                    obj_copy = obj.copy()
                    # Note: This assumes an OTHER value exists in the discriminator enum
                    obj_copy[cls.__discriminator_property_name] = "OTHER"
                    instance = cls.model_validate(obj_copy)
                    instance._original_sign_on_mode = original_discriminator
                    return instance
\2\3'''

    # Only replace the FIRST occurrence
    content = re.sub(pattern, replacement, content, count=1)

    APPLICATION_FILE.write_text(content)
    print("✓ Added from_dict logic for unknown sign-on mode handling")
    return True

def remove_discriminator_logic_from_other_models():
    """Remove the _original_ field from other discriminator-based models"""
    models_dir = APPLICATION_FILE.parent

    # Find all Python files with discriminators (except Application)
    count_fixed = 0
    for py_file in models_dir.glob('*.py'):
        if py_file.name == 'application.py' or py_file.name == '__init__.py':
            continue

        content = py_file.read_text()

        # Check if this file has the _original_ field pattern
        if re.search(r'_original_\w+: Optional\[str\] = None', content):
            # Remove the field
            content = re.sub(
                r'    # Store the original discriminator value.*?\n    _original_\w+: Optional\[str\] = None\n',
                '',
                content
            )

            # Remove the to_dict logic
            content = re.sub(
                r'        # If we have an original discriminator value.*?\n.*?_dict\[.*?\] = self\._original_.*?\n',
                '',
                content
            )

            # Remove the from_dict logic (more complex pattern)
            content = re.sub(
                r'                # Handle unknown discriminator values\n.*?instance\._original_.*?\n.*?return instance\n',
                '',
                content,
                flags=re.DOTALL
            )

            py_file.write_text(content)
            count_fixed += 1
            print(f"  ✓ Cleaned up {py_file.name}")

    if count_fixed > 0:
        print(f"✓ Removed discriminator logic from {count_fixed} other model(s)")

    return count_fixed

def main():
    """Main function to apply Application-specific modifications"""
    print("="*70)
    print("Post-Processing: Adding Unknown Discriminator Handling to Application")
    print("="*70)

    if not APPLICATION_FILE.exists():
        print(f"❌ Error: Application file not found at {APPLICATION_FILE}")
        sys.exit(1)

    # Check if already processed
    if check_if_already_processed():
        print("\n⚠️  Application.py appears to already be processed.")
        print("   Skipping modifications to avoid duplication.")
        print("   If you need to reprocess, regenerate the SDK first.")
        return

    try:
        success = True
        success &= add_original_field()
        success &= add_to_dict_logic()
        success &= add_from_dict_logic()

        # Clean up other models
        print("\nCleaning up other models...")
        remove_discriminator_logic_from_other_models()

        if success:
            print("\n" + "="*70)
            print("✓ Post-processing completed successfully!")
            print("  Application.py now handles unknown sign-on modes")
            print("  Other models remain unaffected")
            print("="*70)
        else:
            print("\n⚠️  Post-processing completed with warnings")
            sys.exit(1)

    except Exception as e:
        print(f"\n❌ Post-processing failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()






