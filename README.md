# Автоматизация тестирования API Яндекс Маркета

Проект покрывает автоматизированное тестирование REST API личного кабинета продавца на [Яндекс Маркете](https://partner.market.yandex.ru/).

Документация: https://yandex.ru/dev/market/partner-api/doc/ru/

---

## Технологии

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="50" title="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="50" title="pytest"/>
  <img src="https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png" height="50" title="Requests"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" height="50" title="jsonschema"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="50" title="PyCharm"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="50" title="Jenkins"/>
  <img src="https://avatars.githubusercontent.com/u/5879127" height="50" title="Allure Report"/>
  <img src="https://avatars.githubusercontent.com/u/101354427" height="50" title="Allure TestOps"/>
  <img src="https://cdn.simpleicons.org/telegram/2AABEE" height="50" title="Telegram"/>
</p>

| Технология | Назначение |
|---|---|
| Python 3 | Язык программирования |
| pytest | Фреймворк для тестирования |
| requests | HTTP-клиент для API-запросов |
| jsonschema | Валидация схем ответов |
| Allure | Отчёты о прохождении тестов |
| Allure TestOps | Управление тест-кейсами |
| Jenkins | CI/CD, удалённый запуск тестов |
| Telegram Bot | Уведомления о результатах |

---

## Покрываемый функционал

- **Авторизация** — проверка доступа с валидными и невалидными токенами
- **Кампании** — получение и управление рекламными кампаниями
- **Точки продаж (outlets)** — работа с торговыми точками
- **Рекомендации** — получение рекомендаций для магазина
- **Настройки** — управление настройками кабинета
- **Отчёт аналитики продаж** — генерация отчёта по показам и продажам
- **Отчёт единого нетинга** — генерация финансовых отчётов

---

## Запуск тестов

### Локально

1. Склонировать репозиторий:
```bash
git clone <repository-url>
cd qa_guru_yandex_api_python
```

2. Создать и активировать виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Запустить тесты:
```bash
pytest
```

### Через Jenkins

Тесты запускаются автоматически через CI/CD на [Jenkins](https://jenkins.autotests.cloud/job/test_example_api_/).

Для ручного запуска:
1. Открыть джобу в Jenkins
2. Выбрать окружение 
2. Нажать **Build Now**
![alt text](image/image-6.png)
![Jenkins Build](image/image.png)

---

## Отчёты Allure

### Локально

После прогона тестов открыть отчёт:
```bash
allure serve allure-results
```
Ниже представлен пример allure отчета 

![Allure Report Local](image/image-1.png)

### Из Jenkins

Нажать на иконку **Allure Report** в строке нужного билда.

![Allure Report Jenkins](image/image-2.png)

---

## Allure TestOps

В проекте настроена интеграция с Allure TestOps для хранения и управления тест-кейсами.

![Allure TestOps](image/image-3.png)
![Allure TestOps](image/image-4.png)

---

## Уведомления в Telegram

После каждого запуска в Jenkins отправляется краткий отчёт в Telegram-чат.

![Telegram](image/image-5.png)
