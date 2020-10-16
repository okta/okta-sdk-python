import pytest
import okta.models as models
from tests.mocks import MockOktaClient
from okta.errors.okta_api_error import OktaAPIError
from http import HTTPStatus


class TestTemplatesResource:
    """
    Integration Tests for the Templates Resource.
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_sms_template(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create SMS Template
        sms_translations = models.SmsTemplateTranslations()
        sms_translations.es = \
            "${org.name}: el código de verificación es ${code}"
        sms_translations.fr = \
            "${org.name}: votre code de vérification est ${code}"
        sms_translations.it = "${org.name}: il codice di verifica è ${code}"

        sms_template_model = models.SmsTemplate({
            "name": f"{TestTemplatesResource.SDK_PREFIX}-test-template",
            "type": models.SmsTemplateType.SMS_VERIFY_CODE,
            "template": "${org.name}: your verification code is ${code}",
            "translations": sms_translations
        })

        created_template, _, err = await client.\
            create_sms_template(sms_template_model)
        assert err is None
        assert isinstance(created_template, models.SmsTemplate)
        assert created_template.name == sms_template_model.name
        assert created_template.type == sms_template_model.type
        assert created_template.template == sms_template_model.template

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == created_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr

        # Delete
        _, err = await client.delete_sms_template(created_template.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_list_sms_templates(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create SMS Template
        sms_translations = models.SmsTemplateTranslations()
        sms_translations.es = \
            "${org.name}: el código de verificación es ${code}"
        sms_translations.fr = \
            "${org.name}: votre code de vérification est ${code}"
        sms_translations.it = "${org.name}: il codice di verifica è ${code}"

        sms_template_model = models.SmsTemplate({
            "name": f"{TestTemplatesResource.SDK_PREFIX}-test-template",
            "type": models.SmsTemplateType.SMS_VERIFY_CODE,
            "template": "${org.name}: your verification code is ${code}",
            "translations": sms_translations
        })

        created_template, _, err = await client.\
            create_sms_template(sms_template_model)
        assert err is None
        assert isinstance(created_template, models.SmsTemplate)
        assert created_template.name == sms_template_model.name
        assert created_template.type == sms_template_model.type
        assert created_template.template == sms_template_model.template
        assert created_template.translations.es == sms_translations.es
        assert created_template.translations.it == sms_translations.it
        assert created_template.translations.fr == sms_translations.fr

        # List
        sms_templates, _, err = await client.list_sms_templates()
        assert err is None
        assert isinstance(sms_templates, list)
        assert next((template for template in sms_templates
                     if template.id == created_template.id), None) is not None

        # Delete
        _, err = await client.delete_sms_template(created_template.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_sms_template(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create SMS Template
        sms_translations = models.SmsTemplateTranslations()
        sms_translations.es = \
            "${org.name}: el código de verificación es ${code}"
        sms_translations.fr = \
            "${org.name}: votre code de vérification est ${code}"
        sms_translations.it = "${org.name}: il codice di verifica è ${code}"

        sms_template_model = models.SmsTemplate({
            "name": f"{TestTemplatesResource.SDK_PREFIX}-test-template",
            "type": models.SmsTemplateType.SMS_VERIFY_CODE,
            "template": "${org.name}: your verification code is ${code}",
            "translations": sms_translations
        })

        created_template, _, err = await client.\
            create_sms_template(sms_template_model)
        assert err is None
        assert isinstance(created_template, models.SmsTemplate)
        assert created_template.name == sms_template_model.name
        assert created_template.type == sms_template_model.type
        assert created_template.template == sms_template_model.template

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == created_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr

        # Update
        created_template.name = sms_template_model.name + "UPDATE"
        updated_template, _, err = await client.\
            update_sms_template(created_template.id, created_template)
        assert err is None
        assert updated_template.id == created_template.id
        assert updated_template.name == sms_template_model.name + "UPDATE"

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == updated_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr

        # Delete
        _, err = await client.delete_sms_template(created_template.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_partial_update_sms_template(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create SMS Template
        sms_translations = models.SmsTemplateTranslations()
        sms_translations.es = \
            "${org.name}: el código de verificación es ${code}"
        sms_translations.fr = \
            "${org.name}: votre code de vérification est ${code}"
        sms_translations.it = "${org.name}: il codice di verifica è ${code}"

        sms_template_model = models.SmsTemplate({
            "name": f"{TestTemplatesResource.SDK_PREFIX}-test-template",
            "type": models.SmsTemplateType.SMS_VERIFY_CODE,
            "template": "${org.name}: your verification code is ${code}",
            "translations": sms_translations
        })

        created_template, _, err = await client.\
            create_sms_template(sms_template_model)
        assert err is None
        assert isinstance(created_template, models.SmsTemplate)
        assert created_template.name == sms_template_model.name
        assert created_template.type == sms_template_model.type
        assert created_template.template == sms_template_model.template

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == created_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr

        # Update
        temporary_template = models.SmsTemplate({
            "translations": models.SmsTemplateTranslations({
                "de":  "${org.name}: ihre bestätigungscode ist ${code}."
            })
        })
        updated_template, _, err = await client.\
            partial_update_sms_template(
                created_template.id, temporary_template)
        assert err is None
        assert updated_template.id == created_template.id
        assert updated_template.name == created_template.name
        assert updated_template.type == created_template.type
        assert updated_template.translations.de ==\
            temporary_template.translations.de

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == updated_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr
        assert retrieved_template.translations.de ==\
            temporary_template.translations.de

        # Delete
        _, err = await client.delete_sms_template(created_template.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_sms_template(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create SMS Template
        sms_translations = models.SmsTemplateTranslations()
        sms_translations.es = \
            "${org.name}: el código de verificación es ${code}"
        sms_translations.fr = \
            "${org.name}: votre code de vérification est ${code}"
        sms_translations.it = "${org.name}: il codice di verifica è ${code}"

        sms_template_model = models.SmsTemplate({
            "name": f"{TestTemplatesResource.SDK_PREFIX}-test-template",
            "type": models.SmsTemplateType.SMS_VERIFY_CODE,
            "template": "${org.name}: your verification code is ${code}",
            "translations": sms_translations
        })

        created_template, _, err = await client.\
            create_sms_template(sms_template_model)
        assert err is None
        assert isinstance(created_template, models.SmsTemplate)
        assert created_template.name == sms_template_model.name
        assert created_template.type == sms_template_model.type
        assert created_template.template == sms_template_model.template

        # Retrieve
        retrieved_template, _, err = await client.\
            get_sms_template(created_template.id)
        assert err is None
        assert retrieved_template.id == created_template.id
        assert retrieved_template.name == created_template.name
        assert retrieved_template.template == created_template.template
        assert retrieved_template.translations.es == sms_translations.es
        assert retrieved_template.translations.it == sms_translations.it
        assert retrieved_template.translations.fr == sms_translations.fr

        # Delete
        _, err = await client.delete_sms_template(created_template.id)
        assert err is None

        # Retrieve
        retrieved_template, resp, err = await client.\
            get_sms_template(created_template.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_template is None
