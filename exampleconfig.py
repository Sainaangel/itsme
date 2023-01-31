from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 6296490
    API_HASH = "24385183c93a98ae4155c25d9f5f64b2"
    # the name to display in your alive message
    ALIVE_NAME = "Your value"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    TECHNO_STRING = "BABrY7BN9dbJQ748w_gU7jgarI3LD82o2sI6OlILL6uiL4wiP_ix5IiwbrkxPKiiwt1Ef3yFunNDwOvjV9t9eKZagtmIfDEYxUutM_CrqebpnbmJSlvJ1P7s2V5AoVQg2tWw3NyVNKVhAskGMUZwTBRo0jTvlJdIe7RW1MQ3rk-P4udB6ok-t3GQvrd9fv06NuNQYC-BlrBF1CgqtWvrZm8sEFRcROFU5VA3H18GgTFl5WcBgNo2Ro3DcnkiDS2Pfj5GiHS8bvwqktRad5PqnphscV5G_fGBSWMYBnJH9w4Ix_4eR6kg7XjcWhDhi6aeFw1dOUslyLEzd34nz2CKKivBAAAAAUXgjJAA"
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "5609161013:AAHhzn3nULekbZADhjPBbLqDmwfu-dupzps"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTRA_REPO = "https://github.com/TECHNOBOT-OP/PLUGINS"
    UPSTREAM_REPO = "pro"
    # Your City's TimeZone
    TZ = "Kolkata, West Bengal (GMT+5:30)"
