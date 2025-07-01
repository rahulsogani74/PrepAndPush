#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26321307"))
API_HASH = environ.get("API_HASH", "989c16548c72fb4c56f1442780d557ea")
BOT_TOKEN = environ.get("BOT_TOKEN", "7255192343:AAEhEirCK4U33TnFRqlZsXnXMkwv_PYfLRk")
OWNER = int(environ.get("OWNER", "7727240590"))
CREDIT = "@PrepAndPush"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
