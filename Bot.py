import telebot
from googletrans import Translator

# أدخل التوكن الخاص بالبوت هنا
TOKEN = "7689316936:AAEz8jU6BbEi5IwkAKC0Ztv7ajQI49CuOFY"
bot = telebot.TeleBot(TOKEN)
translator = Translator()

# دالة لمعرفة لغة النص
def detect_language(text):
    return translator.detect(text).lang

# التعامل مع الرسائل
@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        # كشف لغة النص
        lang = detect_language(message.text)

        # الترجمة للعربية إذا كان النص إنجليزيًا والعكس صحيح
        if lang == "en":
            translated = translator.translate(message.text, dest="ar")
        elif lang == "ar":
            translated = translator.translate(message.text, dest="en")
        else:
            translated = None

        # إرسال الترجمة
        if translated:
            bot.reply_to(message, f"🔹 الترجمة: {translated.text}")
        else:
            bot.reply_to(message, "❌ لا يمكنني ترجمة هذه اللغة!")
    
    except Exception as e:
        bot.reply_to(message, "❌ حدث خطأ أثناء الترجمة!")

# تشغيل البوت
print("🚀 بوت الترجمة يعمل...")
bot.polling()
