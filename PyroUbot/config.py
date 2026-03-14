import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6938178028").split()))

API_ID = int(os.getenv("API_ID", "32839580"))

API_HASH = os.getenv("API_HASH", "2b6cfe9b5f1600365925e17d71f5fb34")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8545876781:AAEsz1Xt3VekhBP8d2KFINL_DDYY0ANm8NUs")

OWNER_ID = int(os.getenv("OWNER_ID", "6938178028"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://cluster123:cluster123@cluster0.muszify.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002765999929"))


