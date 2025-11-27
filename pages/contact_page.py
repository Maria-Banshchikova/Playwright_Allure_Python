import allure
from playwright.sync_api import Page, expect, TimeoutError, TimeoutError as PlaywrightTimeoutError


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_field = "input[name='name']"
        self.email_field = "input[name='email']"
        self.phone_field = "input[name='phone']"
        self.specialization_field = "input[name='specialization']"
        self.message_field = "textarea[name='message']"
        self.captcha_checkbox = "#recaptcha-container"
        self.submit_button = "button[data-slot='button']:has-text('Отправить заявку')"

    @allure.step("Заполнить форму контакта")
    def fill_form(self, name, email, phone, specialization, message):
        self.page.fill(self.name_field, name)
        self.page.fill(self.email_field, email)
        self.page.fill(self.phone_field, phone)
        self.page.fill(self.specialization_field, specialization)
        self.page.fill(self.message_field, message)

    @allure.step("Активировать капчу")
    def activate_captcha(self):
        self.page.click(self.captcha_checkbox)

    @allure.step("Проверить активность кнопки 'Отправить заявку'") 
    def check_submit_button_enabled(self):
        expect(self.page.locator(self.submit_button)).to_be_enabled(timeout=10000) # Проверяем активность кнопки. Но этот тест не пройдет, т.к. обойти капчу автоматически бесплатными способами нельзя. Можно отключить ее в тестовой среде.

    @allure.step("Отправить форму (без реальной отправки)")
    def submit_form_without_sending(self):
        # Заглушка для реальной отправки.
        self.page.click(self.submit_button) # Кликаем на кнопку
        self.page.wait_for_timeout(1000)  # Имитируем ожидание обработки запроса
