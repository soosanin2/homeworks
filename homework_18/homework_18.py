
# 1. Створити клас Bot з атрибутом name та методами say_name та send_message.
#
# send_message має приймати параметри self і message і має друкувати message.
#
# Метод say_name має друкувати значення атрибуту name.

class Bot:
    name = "Bot"

    def say_name(self):
        print(self.name)

    def send_message(self, messege):
        self.messege = messege
        print(self.messege)

some_bot = Bot()

some_bot.say_name()
some_bot.send_message(messege = "som text")

# 2. Створити клас TelegramBot, який має бути унаслідуваний від Bot та має містити:
# власні атрибути url, chat_id(None за замовчуванням) методи send_message, set_url та set_chat_id.
# Ці методи, крім self, мають приймати 1 параметр(url та chat_id відповідно) та присвоювати значення цього параметру
# атрибутам url та chat_id відповідно.
# Також TelegramBot має перевизначити метод send_message – друкувати значення параметру message з будь - яким допоміжним
# текстом.Цей текст також має містити в собі значення url та chat_id
# Результатом має бути:
#
# some_bot = Bot('Marvin')
# some_bot.say_name()
# >> > "Marvin"
#
# some_bot.send_message("Hello")
# >> > "Hello"
#
# telegram_bot = TelegramBot("TG")
# telegram_bot.say_name()
# >> > "TG"
#
# telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat None using None"
#
# telegram_bot.set_chat_id(1)
# telegram_bot.send_message('Hello')
# >> > "TG bot says Hello to chat 1 using None"

class Bot:

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)

    def send_message(self, messege):
        self.messege = messege
        print(self.messege)


class TelegramBot(Bot):
    url = None
    chat_id = None

    def __int__(self, url, chat_id):
        self.url = url
        self.chat_id = chat_id

    def send_message(self, messege):
        self.messege = messege
        print(f"{self.name} bot says Hello to chat {self.chat_id} using {self.url}")

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

some_bot = Bot("Marvin")
some_bot.say_name()

some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()

telegram_bot.send_message('Hello')

telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')
