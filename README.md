# Боты которые умеют отвечать для VK b Telegram>

### Как установить

1. Для запуска проекта Python3 должен быть установлен.

2. Затем используйте 'pip' (или 'pip3'если есть конфликт с Python2) для установки зависимостей:

   ```
   pip install -r requiriments.txt
   ```

3. [Создай DialogFlow Agent](https://dialogflow.cloud.google.com/#/newAgent) для взаимодействия с [Docs](https://cloud.google.com/dialogflow/es/docs/quick/build-agent).

4. [Установи интерфейс командной строки gcloud](https://cloud.google.com/sdk/docs/install)

5. [Инициализируй облачный сервис командной строки Google Cloud](https://cloud.google.com/dialogflow/es/docs/quick/setup#sdk)

6. [Включи API](https://cloud.google.com/dialogflow/es/docs/quick/setup#api) для твоего агента DialogFlow

7. Создай [API key](https://cloud.google.com/docs/authentication/api-keys#create)

8. [Предоставь учетные данные пользователя](https://cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) для твоего аккаунта Google

9. [Включи API](https://console.cloud.google.com/apis/api/apikeys.googleapis.com/)

10. Если хочешь обучить своего бота новым фразам: 
- создай файл `.json`. Для примера используй файл `questions.json` 
- тренируй DialogFlow. Для этого используй команду
    ```
    python3 creation_intent.py
    ```  

11. Не забудь внести данные в `.env` как показано в `.env.example` 

## Запусти свой проект:

### 1. Для Telegram:
- Создай своего бота с помощью `@BotFather` и сохрани токен в `.env` как показано в `.env.example`
- Запусти своего бота:

  ```
  python3 tg_bot.py
  ```

### 2. Для VK:
- [Создай свою группу в VK](https://vk.com/) и сохрани токен в `.env`
- Разреши твоей группе отправлять сообщения в настройках группы
- запусти своего бота:
  ```
  python3 vk_bot.py
  ```

### Пример работы ботов
- Telegram:
![tg_bot](C:\Users\abram\PycharmProjects\dvmnDialog0.8\tg-bot.gif)
- VK:
![vk_bot](C:\Users\abram\PycharmProjects\dvmnDialog0.8\vk_bot.gif)

### Цель проекта

Проект написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).