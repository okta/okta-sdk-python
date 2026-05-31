import pytest
from pydantic import ValidationError

from okta.models.log_stream import LogStream
from okta.models.log_stream_aws import LogStreamAws
from okta.models.log_stream_settings_aws import LogStreamSettingsAws


@pytest.mark.parametrize(
    "event_source_name",
    [
        "p",
        "MultiCharacter",
        "event.source-name_123",
        "a" * 75,
    ],
)
def test_log_stream_settings_aws_accepts_valid_event_source_names(event_source_name):
    settings = LogStreamSettingsAws(
        accountId="123456789012",
        eventSourceName=event_source_name,
        region="us-east-1",
    )

    assert settings.event_source_name == event_source_name


@pytest.mark.parametrize(
    "event_source_name",
    [
        "",
        "contains space",
        "contains/slash",
        "a" * 76,
    ],
)
def test_log_stream_settings_aws_rejects_invalid_event_source_names(event_source_name):
    with pytest.raises(ValidationError):
        LogStreamSettingsAws(
            accountId="123456789012",
            eventSourceName=event_source_name,
            region="us-east-1",
        )


def test_log_stream_aws_deserializes_multi_character_event_source_name():
    log_stream = LogStream.from_dict(
        {
            "created": "2026-01-01T00:00:00.000Z",
            "id": "logstream123",
            "lastUpdated": "2026-01-01T00:00:00.000Z",
            "name": "AWS EventBridge Log Stream",
            "status": "ACTIVE",
            "type": "aws_eventbridge",
            "_links": {
                "self": {
                    "href": "/api/v1/logStreams/logstream123",
                    "method": "GET",
                }
            },
            "settings": {
                "accountId": "123456789012",
                "eventSourceName": "MultiCharacter",
                "region": "us-east-1",
            },
        }
    )

    assert isinstance(log_stream, LogStreamAws)
    assert log_stream.settings.event_source_name == "MultiCharacter"
