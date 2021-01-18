from selenium.webdriver.support.select import Select

from page_object_pattern.tests.test_data import TestData


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.name_input_xpath = "//input[@name='imie-i-nazwisko']"
        self.mail_input_xpath = "//input[@name='e-mail']"
        self.topic_selector_name = "wybierz-temat"
        self.text_input_xpath = "//textarea[@name='tresc']"
        self.rodo_checkbox_xpath = "//label[@class='custom-control-label']"
        self.send_button_xpath = "//button[@type='submit']"
        self.fill_all_fields_validation_xpath = "//i[@class='las la-ban la-lg mr-2']"
        self.captcha_xpath = "//span[@class='invalid-feedback ']"

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.name_input_xpath).clear()
        self.driver.find_element_by_xpath(self.name_input_xpath).send_keys(name)

    def set_mail(self, mail):
        self.driver.find_element_by_xpath(self.mail_input_xpath).clear()
        self.driver.find_element_by_xpath(self.mail_input_xpath).send_keys(mail)

    def set_topic(self, topic):
        chosen_topic = Select(self.driver.find_element_by_name(self.topic_selector_name))
        chosen_topic.select_by_value(topic)

    def set_text(self, text):
        self.driver.find_element_by_xpath(self.text_input_xpath).clear()
        self.driver.find_element_by_xpath(self.text_input_xpath).send_keys(text)

    def click_rodo_button(self):
        self.driver.find_element_by_xpath(self.rodo_checkbox_xpath).click()

    def click_send_button(self):
        self.driver.find_element_by_xpath(self.send_button_xpath).click()

    def fill_all_fields_validation(self):
        return self.driver.find_element_by_xpath(self.fill_all_fields_validation_xpath).is_displayed()

    def captcha_not_filled(self):
        self.driver.find_element_by_xpath(self.captcha_xpath).is_displayed()

    def fill_all_fields(self):
        self.set_name(TestData.name)
        self.set_mail(TestData.makeEmail())
        self.set_topic(TestData.topic)
        self.set_text(TestData.text)
        self.click_rodo_button()
        self.click_send_button()
