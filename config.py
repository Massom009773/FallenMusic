from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "99999"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/57dbda8d0aa010c307956.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/a43d3eb322614c8c46e14.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/innocentop")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_meeBacha")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5611809645").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
