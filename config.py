import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "396b10bcf5e1ed5fcc71f1603800b7cf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7371246781:AAGIVGgXOBfGHamn74PUyoxUZDB7U3weqBc")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "5461760")
    OWNER = os.environ.get("OWNER", "6521935712")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "siddhant_devil")
    PASSWORD = os.environ.get("PASSWORD", "@ftmdeveloper")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002187287666")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
                                         #"BQG3FogAkXFq48_fYpmJhUFE9y7TWFSeIZwbiFaMaNwVnm5M_4Unc_mu_FLOtG_bXeIB1FrGNtMzk06eUfTvu2vN2ykeUR3OJ3JdjN4jy7Vas8mRafAQxZf4cGnW3CZIdBJJnVgpJz-oM-C0GzQLQNjBQqhLWE5WCmYVzH-gQKmSwS7lYbLSykK5PceiPWeRtEEtvacZrs-ofBD9Rd3DWWVqy5GzEL-6cqD-eg8JeuWlBMVUgclhAwPebzVXzgac3TUz1LOwE3Wb3kO1i31Wrg-7ruKnAb2bebIju3qQEQzHPdh91wyb-Wp_nveNVdmE8GFnxF6wFh4RB_Qh0b_EngIFPEpNTQAAAAGjxJFrAA")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
