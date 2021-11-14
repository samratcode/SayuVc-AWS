import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = "AQAP3fV9d7EG9IHVTHrfPFoRXSFtqPHcPHOzAUvw1kO0EDreOAOgptK1oGLDjToNK3H4R7mF_9f3aMbkgyF0Dn6fAgI0HukrDXLFbwwDENWI9nPFYH3SmJiLDDhlvAIu23JVw4-m1Ri3f8G77-GgbsWM4q7Cst1UKJpk_slyZvWGq2lxfZ6rcqhN1cFJ_CLIrcs0dOLUbbeKFy_ie96SlsaZKcDzi4DIYA6lYz6-DY4rtRQ33wQjxye7L4Au7VIF7Nv5OpqG6U9ELe3upND_l_6FYZSMGlqwlz65q2077luWgWx8d6R3R10vLfZPWLvqUoKCmEsfuJsqfpwlZvJh-0XMdcSqmwA"
BOT_TOKEN = "1931163050:AAFaNETwdYhxwU1DlHZEMW3tsfMhdB9z8kQ"
BOT_NAME = "Sayu"
API_ID = 8896402
API_HASH = "de2f306c240b3036cac3866e738fad3f"
DATABASE_URL = "mongodb+srv://fridayub:7352007414@cluster0.garnp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
OWNER_NAME = "TheSexyKid"
ALIVE_NAME = "SayuMusic"
BOT_USERNAME = "SayuVc"
ASSISTANT_NAME = "SayuVc"
GROUP_SUPPORT = "RukaSupport"
UPDATES_CHANNEL = "Rukaupdates"
SUDO_USERS = "1634155867"
COMMAND_PREFIXES = "/"
ALIVE_IMG = "https://telegra.ph/file/16fd73ce91fb4e569db9e.jpg")
DURATION_LIMIT = "60"
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
