""" Проверка кода стараниц методами GET POST """

import time
import requests
import allure
from url.url_page import Url


headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/77.0.3865.120 Mobile Safari/537.36 ",
}

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Список работ")
def test_get_jobs():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_jobs, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass


@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на главную страницу")
def test_get_home_page():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_homepage, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Отчеты")
def test_get_reports():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_reports, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Центр")
def test_get_center():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_center, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Образовательный сайт")
def test_get_educational():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_educational, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Служба раннего вмешательства")
def test_get_eis():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_eis, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Сад")
def test_get_kindergarten():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_kindergarten, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Школа")
def test_get_school():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_school, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Специалисты")
def test_get_specialists():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_specialists, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Волонтеры")
def test_get_volunteers():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_volunteers, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Мастерские")
def test_get_workshops():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_workshops, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Контакты")
def test_get_contacts():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_contacts, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Уставные документы")
def test_get_documents():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_documents, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

@allure.feature("Тестирование кода ответа методом GET")
@allure.story("Вход на страницу Уставные документы")
def test_get_documents():
    """ Проверка кода ответа. """

    response = requests.get(Url.url_documents, headers=headers, timeout=10)
    with allure.step("Проверка кода ответа"):
        assert (
            response.status_code == 200
        ), f"Неверный код ответа, получен {response.status_code}"
    with allure.step(f"Посмотрим что получили {response}"):
        pass

