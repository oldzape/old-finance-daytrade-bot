import telebot
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from analise_completa import obter_dados_binance

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))
CHAT_ID = int(os.getenv("CHAT_ID"))

TOPICOS = {
    "Privado do Admin": 32,
    "Feedback de Trades": 25,
    "Chat Livre": 5,
    "Estratégias": 6,
    "Hold Spot": 18,
    "Swing Trade Futuros": 14,
    "Notícias e Análises": 19,
    "Trade Spot": 16,
    "Day Trade Futuros": 1,
    "Solicitar Acesso VIP": 34,
    "Ajuda": 30,
    "General": None
}

@bot.message_handler(commands=['start', 'teste'])
def send_test(message):
    for nome, thread_id in TOPICOS.items():
        texto = f"📊 Análise Técnica Teste enviada para o tópico: **{nome}**"
        bot.send_message(
            chat_id=CHAT_ID,
            message_thread_id=thread_id,
            text=texto,
            parse_mode="Markdown"
        )

keep_alive()
print("Bot rodando...")
bot.infinity_polling()
