import allure
import pytest
from playwright.sync_api import Page

from data import test_data
from pages.contact_page import ContactPage, expect

@allure.epic("Форма для заполнения пользователем")
@allure.feature("Заполнение и отправка")
def test_contact_form_submission(page: Page):
    contact_page = ContactPage(page)

    with allure.step("Заполнение формы"):
        contact_page.fill_form(
            test_data.valid_name,
            test_data.valid_email,
            test_data.valid_phone,
            test_data.valid_specialization,
            test_data.valid_message,
        )

    with allure.step("Активация капчи"):
        contact_page.activate_captcha()  # Кликаем на чекбокс.

    with allure.step("Проверка, что кнопка 'Отправить заявку' становится активной"):
        contact_page.check_submit_button_enabled()  # Проверяем активность кнопки. Но этот тест не пройдет, т.к. обойти капчу автоматически бесплатными способами нельзя. Можно отключить ее в тестовой среде.

    with allure.step("Отправка формы (имитация)"):
        contact_page.submit_form_without_sending()
    