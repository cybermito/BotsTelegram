import telebot
from telebot import types

TOKEN = 'My token'
chatid = 'id del Chat'

tb = telebot.Telebot(TOKEN)

tb.send_message(chatid, text) #Enviar un mensaje al bot.

#Enviar una foto
photo = open('url de la foto a enviar', 'rb')
tb.send_photo(chatid, photo)

#Enviar un documento PDF
pdf = open('url del documento a enviar', 'rb')
tb.send_document(chatid, pdf)

#Enviar un vídeo --> tb.send_video()
#Enviar un sticker --> tb.sticker()
#Enviar un localización
tb.send_location(Chatid, latitud, longitud)

#Reenviar un mensaje (Cualquier tipo de mensaje)
tb.forward_message(to_chatid, from_chatid, message_id)

#Enviar acciones del chat
tb.send_chat_action(chatid, action_string) ## Están disponibles todas estas acciones typing,upload_photo,record_video,upload_video,record_audio,upload_audio,upload_document,find_location (Me gustaría que existiera una acción de "Durmiendo...", estaría gracioso :D).

#Obtener actualizaciones
tb.get_updates()

#Crear un teclado de acciones
#from telebot import types --> Esto ponerlo al principio del programa
