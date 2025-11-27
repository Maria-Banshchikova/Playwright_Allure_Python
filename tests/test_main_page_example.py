import allure
import pytest
from pages.main_page import MainPage, expect

@allure.epic("Главная страница")
@allure.feature("Навигация по блокам и переход на сайт с вакансиями")
class TestNavigation:
    @allure.title("Проверка перехода к блоку 'Свяжитесь с нами'. Кнопка 'Оставить заявку'") # работает
    def test_scroll_to_contact_from_leave_request(self, main_page: MainPage):
        main_page.click_leave_request()
        expect(main_page.page.locator('#contact')).to_be_visible(timeout=10000)       
        assert main_page.page.is_visible("#contact")

    @allure.step("Проверка нажатия на кнопку 'Узнать больше' и переход к блоку 'Аутстафф'")  # работает
    def test_click_find_more(self, main_page: MainPage):
        main_page.click_find_more()

    @allure.title("Проверка открытия страницы вакансий при нажатии на кнопку 'Актуальные вакансии'") # работает
    def test_open_vacancies_page(self, main_page: MainPage):
        main_page.open_vacancies_page()

    @allure.step("Проверка нажатия на 2 кнопки 'Выбрать формат' и перейти к блоку 'Свяжитесь с нами'")  # работает
    def test_click_select_format_1_2(self, main_page: MainPage):
        main_page.click_select_format_1_2()

    @allure.step("Проверка перехода к блоку 'О компании' при нажатии на ссылку 'О нас'")  # работает, но тест провален, т.к. ошибка в коде
    def test_scroll_to_about_company(self, main_page: MainPage):
         main_page.scroll_to_about_company()

    @allure.step("Проверка открытия сайта https://ai-hunt.ru/vacancies/ при нажатии на ссылку 'Вакансии'")  # работает, но тест провален, т.к. ошибка в коде
    def test_open_new_page_vacancies(self, main_page: MainPage):            
        main_page.open_new_page_vacancies()

    @allure.step("Проверка перехода к блоку 'Отзывы специалистов' при нажатии на ссылку 'Отзывы'")  # работает, но тест провален, т.к. ошибка в коде
    def test_scroll_to_reviews(self, main_page: MainPage):
        main_page.scroll_to_reviews()

    @allure.step("Проверка перехода к блоку 'Контактная информация' при нажатии на ссылку 'Контакты'")  # работает
    def test_scroll_to_contacts(self, main_page: MainPage):
        main_page.scroll_to_contacts()

    @allure.title("Проверка скролла к блоку 'Аутстафф'. Ссылка 'Аутстафф'") # работает
    def test_scroll_to_outstaff(self, main_page: MainPage):
        main_page.scroll_to_outstaff()
        expect(main_page.page.locator('#services')).to_be_visible(timeout=10000)
        assert main_page.page.is_visible('#services')
    
    @allure.title("Проверка скролла к блоку 'Трудоустройство'. Ссылка 'Трудоустройство'") # работает
    def test_scroll_to_employment(self, main_page: MainPage):
        main_page.scroll_to_employment()
        expect(main_page.page.locator('#services')).to_be_visible(timeout=10000)
        assert main_page.page.is_visible("#services")

    @allure.title("Проверка скролла к блоку 'Свяжитесь с нами'. Ссылка 'Консультация'") # работает
    def test_scroll_to_consultation(self, main_page: MainPage):
        main_page.scroll_to_consultation()
        expect(main_page.page.locator('#contact')).to_be_visible(timeout=10000)
        assert main_page.page.is_visible("#contact")
