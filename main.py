import telebot
from movie import recommendations, rating
bot = telebot.TeleBot("6621694688:AAGosGI64VmB81NeP2i-1G5hvcp-ESrqh_Q")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Введите название фильма/мультфильма для рекомендации или напишите rating для вывода топа фильмов по рейтингу")

@bot.message_handler(func=lambda message: True)
def recommend_movie(message):
    if message.text!="rating":
        user_input = message.text
        recommendation = recommendations(user_input)
        result_message = f'Вот список похожих фильмов и мультфильмов:\n'
        for idx, movie_title in enumerate(recommendation, start=1):
         result_message += f"{idx}) {movie_title}\n"
    else:
        result_message=rating()

    bot.reply_to(message, result_message)

bot.polling()