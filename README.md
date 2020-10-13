### Тестовое приложение для Emphasoft
Веб приложение на Django с VK OAuth авторизацией

### Установка
1. `git clone`
2. `virtualenv venv`
3. `source venv/bin/activate`
4. `pip install requirements.txt`
5. `./manage.py migrate`
6. `создать в корне проект .env файл, прописать в нем `[ID проекта и секретный ключ](https://vk.com/editapp?act=create)
```
SOCIAL_AUTH_VK_OAUTH2_KEY=XXXXXXXXX
SOCIAL_AUTH_VK_OAUTH2_SECRET=XXXXXXXX
```
### Технологии
* `Python 3.8.2`
* `Django 3.1.2`
* `SQLite`
