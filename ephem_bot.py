"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

today = '2019/11/27'
planet_dict = {'Mars': ephem.Mars(today), 'Venus': ephem.Venus(today), 'Saturn': ephem.Saturn(today), 'Jupiter': ephem.Jupiter(today),
               'Neptune': ephem.Neptune(today), 'Uranus': ephem.Uranus(today), 'Mercury': ephem.Mercury(today)}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def which_constellation(bot, update):
    planet_name = update.message.text.split()[1]
    ephem_body = planet_dict.get(planet_name, None)
    if ephem_body!=None:
        constellation = ephem.constellation(planet_dict[planet_name])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('I don\'t know this planet!')


def main():
    # mybot = Updater("1050767852:AAGJLxpdMCIB3q_m3TtHrWaMUTj15-Nvfps", request_kwargs=PROXY)
    mybot = Updater("1050767852:AAGJLxpdMCIB3q_m3TtHrWaMUTj15-Nvfps")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", which_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
