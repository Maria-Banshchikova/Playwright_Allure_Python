# UI Тесты для effective-mobile.ru с использованием Playwright, Pytest и Allure

Этот проект представляет собой набор автоматизированных UI тестов для главной страницы сайта [effective-mobile.ru](http://effective-mobile.ru). Тесты проверяют переходы по различным блокам (О нас, Контакты и т.д.) и соответствие локаторов и URL. Проект разработан с использованием фреймворка Playwright, Pytest и библиотеки Allure для отчётов.

## Используемые технологии
- **Язык**: Python 3.10
- **Фреймворк тестирования**: Playwright (для браузерной автоматизации) + Pytest
- **Отчёты**: Allure
- **Паттерн**: Page Object Model
- **Дополнительно**: Docker (опционально)


## Структура проекта (Framework Structure)

Playwright_Allure_Python/
 ```
├── .venv/                          # Виртуальное окружение Python (не входит в репозиторий)
├── allure-results/                 # Результаты выполнения тестов для Allure (не отслеживается в Git)
├── data/                           # Файлы с тестовыми данными для заполнения формы
├── pages/                          # Page Objects
│   ├── contact_page.py             # Page Object для заполнения формы
│   └── main_page.py                # Page Object для главной страницы
├── tests/                          # Тесты
│   ├── test_contact_form.py        # Тесты для заполнения формы
│   └── test_main_page.py           # Тесты для главной страницы
├── utils/                          # Вспомогательные функции и классы (пусто)
├── conftest.py                     # Pytest fixture (настройки тестовой среды)
├── README.md                       # Этот файл
├── requirements.txt                # Список зависимостей Python
└── Dockerfile                      # Файл для сборки Docker-контейнера
 ```

## Требования

*   Python 3.10
*   Playwright
*   Pytest
*   Allure

## Инструкция по установке (Setup Instructions)

1.  **Клонируйте репозиторий:**

    ```bash
    git clone <ваш_репозиторий>
    cd <имя_папки_проекта>
    ```

2.  **Создайте виртуальное окружение:**

    ```bash
    python3 -m venv .venv
    ```
    Активируйте виртуальное окружение:
    * Linux/macOS:
    ```bash
    source .venv/bin/activate
    ```
    * Windows:
    ```bash
     .venv\Scripts\activate
    ```

3.  **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Установите браузеры для Playwright:**

    ```bash
    playwright install
    ```

## Запуск тестов (Run Tests)

1.  **Запустите тесты:**

    ```bash
    pytest --alluredir=allure-results
    ```
    Эта команда запустит все тесты в каталоге `tests` и сохранит результаты в папку `allure-results`.

2.  **Сформируйте отчет Allure:**

    ```bash
    allure serve allure-results
    ```

    Эта команда запустит веб-сервер и откроет Allure отчет в вашем браузере.  Вы можете просмотреть отчет локально, чтобы анализировать результаты тестов.

## Docker (Опционально)

1.  **Соберите Docker-образ:**

    ```bash
    docker build -t tests-effective-mobile .
    ```

2.  **Запустите Docker-контейнер:**

    ```bash
    docker run -v $(pwd)/allure-results:/app/allure-results tests-effective-mobile
    ```
    *Замените `$(pwd)` на текущую директорию или полный путь к папке с проектом в Windows.*
    Эта команда запустит контейнер, выполнит тесты и сохранит отчет Allure в локальную папку `allure-results`.

Советы:
Проблемы?: Если таймауты — проверьте интернет/VPN.

Автор и контакты: [mba-tomsk@mail.ru, @AmaltheaJ5].
