import telebot, os, states, datetime, time, Myconfig as config
from instabot import Bot


'''write below  data of your bot'''

TOKEN = '---'
TelBot = telebot.TeleBot(TOKEN)
'''InstBot = Bot()
InstBot.login(username = '---', password = '---')'''



class User_States():
    state = 'Not active'
user = User_States()




@TelBot.message_handler(content_types = 'photo')
def photo_handler(message):
    TelBot.send_message(message.from_user.id, text = 'you sent me a photo')
    photo = message.photo[-1]
    #  Из photo узнаем идентификационный номер картинки
    file_id = photo.file_id

    #  По file_id мы можем найти путь, по которому хранится картинка на сервере:
    file_path = TelBot.get_file(file_id).file_path

    #  С помощью этого пути мы cможем скачать картинку, используя метод бота, реализованный в библиотеке
    downloaded_file = TelBot.download_file(file_path)
    name = file_id + ".jpg"
    new_file = open(name, mode = 'wb')
    new_file.write(downloaded_file)
    new_file.close()
    TelBot.send_message(message.from_user.id, text = 'and I downloaded it')




'''
@TelBot.message_handler(commands = ['start']) # start command handler
def start_handler(message):
    if str(message.from_user.id) == '---':
        TelBot.send_message(message.from_user.id, text = f'Hi, {message.from_user.first_name}! To start with lets register in of your Instagram account /text /photo')
    else:
        TelBot.send_message(message.from_user.id,
                            text=f'Hi, {message.from_user.first_name}! You are not welcome here. Go away!')


@TelBot.message_handler(commands = ['text']) # text command handler
def enterText_handler(message):
    user.state = 'text'
    print(user.state)
    TelBot.send_message(message.from_user.id, text = f'Hi, {message.from_user.first_name}! Your status was changed on {user.state}')



@TelBot.message_handler(content_types = 'text')
def text_handler(message):
    if user.state == 'text':
        TelBot.send_message(message.from_user.id, text = f'Waiting for the text')
    else:
        TelBot.send_message(message.from_user.id, text = f'I am not able to speak with you yet, but I will learn it!')






@TelBot.message_handler(commands = ['post'])
def post(message):
    InstBot.upload_photo('HI.jpg', caption = 'Today is the first day of bot creating)')
    TelBot.send_message(message.from_user.id, text = f'It worked out. I hope..')





'''





if __name__ == '__main__':
     TelBot.infinity_polling()


'''

now = datetime.datetime.now()
def timer(t):
    if str(now) > t:
        return bot.upload_photo('HI.jpg', caption= 'Я тут учусь использовать Питон в личных целях))')

    else:
        time.sleep(60)
        return timer(t)


bot = Bot()
bot.login(username = 'lasur2012', password = 'vW%t=^VWPGvin4e')
bot.upload_photo('HI.jpg', caption= 'Я тут учусь использовать Питон в личных целях))')



if timer('2020-12-19 21:01'):
    print("I did it again")

'''

