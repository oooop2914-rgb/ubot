import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "6787098484").split()))

API_ID = int(os.getenv("API_ID", "23205651"))

API_HASH = os.getenv("API_HASH", "5a5d93f4564092db12126729cacf58ac")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8011986562:AAFkkSt-EkH6l37rDB3WpiV2sPv3_KkvyWs")

OWNER_ID = int(os.getenv("OWNER_ID", "8150600900"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://cluster123:cluster123@cluster0.muszify.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002765999929"))


