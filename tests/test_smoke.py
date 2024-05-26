import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_job_is_qa_engineer():
    """
    Test case to check if the job is 'qa engineer'
    """
    # Опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")  # Открываем на полный экран
    chrome_options.add_argument("--disable-infobars")  # Отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")  # Отключаем расширения
    # chrome_options.add_argument("--headless")  # Спец. режим "без браузера"

    # Устанавливаем путь к webdriver
    service = Service()  # Укажите путь к chromedriver, если он не в PATH

    # Запускаем браузер с указанными настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Определяем путь к локальному HTML-файлу
    html_file_path = 'file:///C:\projects\CV\index.html'
    driver.get(url=html_file_path)

    try:
        # Проверяем наличие текста 'job : QA-ENGINEER' на странице
        job_element = driver.find_element(By.XPATH, "//div[contains(@class, 'list') and contains(., 'job')]/span[3]")
        assert job_element.text == 'QA-ENGINEER', f"Expected job to be 'qa engineer', but got '{job_element.text}'"
        print("Проверка прошла успешно: job = 'QA-ENGINEER'")
    finally:
        # Закрываем браузер
        driver.quit()

@pytest.mark.xfail(reason="Wait till age is 23")
def test_age_is_23():
    """
    Test case to check if the age is 23
    """
    # Опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")  # Открываем на полный экран
    chrome_options.add_argument("--disable-infobars")  # Отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions")  # Отключаем расширения
    # chrome_options.add_argument("--headless")  # Спец. режим "без браузера"

    # Устанавливаем путь к webdriver
    service = Service()  # Укажите путь к chromedriver, если он не в PATH

    # Запускаем браузер с указанными настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Определяем путь к локальному HTML-файлу
    html_file_path = 'file:///C:\projects\CV\index.html'
    driver.get(url=html_file_path)

    try:
        # Проверяем наличие текста 'age : 23' на странице
        job_element = driver.find_element(By.XPATH, "//div[contains(@class, 'list') and contains(., 'age')]/span[3]")
        assert job_element.text == '23', f"Expected job to be '23', but got '{job_element.text}'"
        print("Проверка прошла успешно: age = '23'")
    finally:
        # Закрываем браузер
        driver.quit()