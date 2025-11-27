import allure
from playwright.sync_api import (
    Page,
    expect,
    TimeoutError,
    TimeoutError as PlaywrightTimeoutError,
)


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.link_outstaff = "a[href='#services']"
        self.link_employment = "a[href='#services']"
        self.link_consultations = "a[href='#contact']"
        self.button_leave_request = "button:has-text('Оставить заявку')"
        self.button_vacancies = "text=Актуальные вакансии"
        self.button_find_more = "button:has-text('Узнать больше')"
        self.button_select_format = "button:has-text('Выбрать формат')"
        self.link_about_company = "a[href='#about']"
        self.link_vacancies = "a[href='#specializations']"
        self.link_reviews = "a[href='#testimonials']"
        self.link_contacts = "a[href='#contact']"
        self.section_contacts = "div:has(h3:has-text('Контактная информация'))"

    @allure.step("Нажать кнопку 'Оставить заявку' и перейти к блоку 'Свяжитесь с нами'")  # работает
    def click_leave_request(self):
        self.page.locator(self.button_leave_request).click()
        self.page.locator("#contact").scroll_into_view_if_needed()

    @allure.step("Нажать кнопку 'Узнать больше' и перейти к блоку 'Аутстафф'")  # работает
    def click_find_more(self):
        self.page.locator(self.button_find_more).click()
        self.page.locator("#services").scroll_into_view_if_needed()

    @allure.step("Нажать кнопку 'Актуальные вакансии' и проверить, что открылся сайт https://ai-hunt.ru/vacancies/")  # работает
    def open_vacancies_page(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(self.button_vacancies).click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://ai-hunt.ru/vacancies/")

    @allure.step("Нажать на обе кнопки 'Выбрать формат' и перейти к блоку 'Свяжитесь с нами'")  # работает
    def click_select_format_1_2(self):
        butt_select_format = self.page.locator(self.button_select_format)
        count= butt_select_format.count()
        for i in range(count):  # Итерируемся по *всем* кнопкам
            butt_select_format.nth(i).click() # Кликаем по каждой кнопке
            self.page.locator("#contact").scroll_into_view_if_needed()
            self.page.locator("#contact").wait_for()

    @allure.step("Перейти к блоку 'О компании' при нажатии на ссылку 'О нас'")  # работает
    def scroll_to_about_company(self):
        self.page.locator(self.link_about_company).get_by_text("О нас", exact=False).click()
        self.page.wait_for_selector('#about').scroll_into_view_if_needed()

    @allure.step("Открыть сайт https://ai-hunt.ru/vacancies/ при нажатии на ссылку 'Вакансии'")  # работает
    def open_new_page_vacancies(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(self.link_vacancies).click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url("https://ai-hunt.ru/vacancies/")

    @allure.step("Перейти к блоку 'Отзывы специалистов' при нажатии на ссылку 'Отзывы'")  # работает
    def scroll_to_reviews(self):
        self.page.locator(self.link_reviews).get_by_text("Отзывы", exact=False).click()
        self.page.wait_for_selector("#testimonials").scroll_into_view_if_needed()

    @allure.step("Перейти к блоку 'Контактная информация' при нажатии на ссылку 'Контакты'")  # работает
    def scroll_to_contacts(self):
        self.page.locator(self.link_contacts).get_by_text("Контакты", exact=False).click()
        self.page.wait_for_selector(self.section_contacts).scroll_into_view_if_needed()

    @allure.step("Перейти к блоку 'Аутстафф' при нажатии на ссылку 'Аутстафф'")  # работает
    def scroll_to_outstaff(self):
        try:
            element = self.page.locator(self.link_outstaff).get_by_text("Аутстафф", exact=False)  # exact=False для частичного совпадения
            element.click()
            self.page.wait_for_selector("#services", state="visible", timeout=30000)  
            self.page.locator("#services").scroll_into_view_if_needed()
        except PlaywrightTimeoutError:
            self.page.screenshot(path="error_screenshot.png")  # Отладка: скриншот при ошибке
            raise  # Перебрасываем ошибку для pytest

    @allure.step("Перейти к блоку 'Трудоустройство' при нажатии на ссылку 'Трудоустройство'")  # работает
    def scroll_to_employment(self):
        element = self.page.locator(self.link_employment).get_by_text("Трудоустройство", exact=False)
        element.click()
        self.page.wait_for_selector("#services").scroll_into_view_if_needed()

    @allure.step("Перейти к блоку 'Свяжитесь с нами' при нажатии на ссылку 'Консультация'")  # работает
    def scroll_to_consultation(self):
        self.page.locator(self.link_consultations).get_by_text("Консультация", exact=False).click()
        self.page.wait_for_selector("#contact").scroll_into_view_if_needed()
