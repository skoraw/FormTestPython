import pytest
from page_object_pattern.pages.form_page import FormPage


@pytest.mark.usefixtures("setup")
@pytest.mark.webtest
class TestFormPage:

    def test_fill_up_form(self):
        test_form_page = FormPage(self.driver)
        test_form_page.fill_all_fields()
        assert test_form_page.fill_all_fields_validation() is True
        pass

    def captcha_filed_required(self):
        test_form_page = FormPage(self.driver)
        assert test_form_page.captcha_not_filled() is True
