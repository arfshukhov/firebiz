import re
from models import *
from crypto import crypto
from origin import *


class User:
    @staticmethod
    def register_new(first_name, last_name, email, password_hash, country_code, phone):
        try:
            user = Users(
                first_name=first_name, last_name=last_name, email=email,
                password_hash=password_hash, country_code=country_code,
                phone=phone
            ).save()
            return 1
        except Exception as e:
            return 0

    @staticmethod
    def validate_username(name) -> strbool:
        pattern1 = r'^[a-zA-Z]+$'
        pattern2 = r'^[а-яА-Я]+$'
        if 1 <= len(name) <= 30 and (re.match(pattern1, name)
                                     or re.match(pattern2, name)):
            return name
        else:
            return 0

    @staticmethod
    def validate_email(email) -> strbool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if 1 <= len(email) <= 50 and re.match(pattern, email)\
                and len(Users.select().where(Users.email == email)) == 0:
            return email
        else:  
            return 0

    @staticmethod
    def validate_password(password) -> strbool:
        if len(password) < 6:
            return 0
        if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
            return 0
        if not re.search(r'\d', password):
            return 0

        return crypto.encrypt(password)

    @classmethod
    def validate_country_code(cls, country_code) -> strbool:
        if len(country_code) == 2 and re.match(r"[a-zA-Z]{2}", country_code):
            return country_code
        else:
            return 0

    @classmethod
    def validate_phone(cls, phone) -> strbool:
        pattern = r'^\+\d{1,20}$'
        if re.match(pattern, phone):
            return phone
        else:
            return 0

    @classmethod
    def match_password(cls, login, password) -> bool:
        """
        используется для сопоставления логина и пароля для авторизации
        :param login: строка
        :param password: строка
        :return: 1 или 0 в зависимости от успешности авторизации
        """
        account = Users.select().where(Users.login == login).get()
        if account.password_hash == crypto.encrypt(password):
            return 1
        else:
            return 0


