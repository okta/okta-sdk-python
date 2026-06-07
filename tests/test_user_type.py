from okta.models.user_type import UserType


def test_user_type_from_dict_preserves_response_fields():
    user_type = UserType.from_dict(
        {
            "id": "oty123",
            "name": "employee",
            "displayName": "Employee",
            "description": "Employee user type",
            "default": False,
            "createdBy": "00ucreated",
            "created": "2026-01-02T03:04:05.000Z",
            "lastUpdatedBy": "00uupdated",
            "lastUpdated": "2026-01-03T04:05:06.000Z",
        }
    )

    assert user_type.id == "oty123"
    assert user_type.name == "employee"
    assert user_type.display_name == "Employee"
    assert user_type.description == "Employee user type"
    assert user_type.default is False
    assert user_type.created_by == "00ucreated"
    assert user_type.created is not None
    assert user_type.last_updated_by == "00uupdated"
    assert user_type.last_updated is not None


def test_user_type_to_dict_keeps_create_and_update_fields():
    user_type = UserType(
        id="oty123",
        name="employee",
        displayName="Employee",
        description="Employee user type",
    )

    assert user_type.to_dict() == {
        "description": "Employee user type",
        "displayName": "Employee",
        "id": "oty123",
        "name": "employee",
    }
