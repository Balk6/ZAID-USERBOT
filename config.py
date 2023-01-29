import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "21969185")) #optional
API_HASH = getenv("API_HASH", "33275905df7c843157fa9663e4bb6fe1") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5862898648").split()))
OWNER_ID = int(getenv("OWNER_ID", "5862898648"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://balk6:<password>@cluster0.xmoyf3q.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5876355103:AAG8eagrsaJ2goeKIH4N8Q8mglCNJH5iuN8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "809374776")
LOG_GROUP = getenv("LOG_GROUP", "809374776")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAmkniYISXOEUGZqP55P4kD1iemVqJLQckDj4rPIgHIzl8vblMlWcxL1-cJNTk1Ket51kMtnyJpTyDNEKA3l-CXGZxUiLiSWd6I1r573A8HHmMQ0_39ZrF8WX6G5_wx8Hn9ojr06GRNnxY1Vakps0ouejY9cmGdrjrSV1uXH6BP5d5qcTRRPYFvjvaRpLwDL14rUcJdpc8yAjxlcoWAbRvS6_OfP19gU-aARVSoocdonPGAO4fFno0kTeuyLB-BhYGVRyE_0FoLPtOPWpr-exa8LHEqjecG2wjfVitqodgQ4dxuEkh4BOGztXn22DgC5PQacCQm_pcnIUWgdbeQeOU7wAAAAFddLvYAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
