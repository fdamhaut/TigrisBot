BOT_TOKEN = ""  # Token of the bot given by the Discord Developer Portal (must be changed)

DB_NAME_TIGRIS = "./tigris.db"  # Name of the file containing the SQLite main database
DB_NAME_JOBS = "./jobs.db"
BALANCE_TABLE = "balance"   # Name of the table containing the balances
TRANSACTION_TABLE = "transac"   # Name of the table containing the transactions
JOB_TABLE = "job"   # Name of the table containing the job details
NAME_TABLE = "name"     # Name of the table containing the name of the users

ALLOWED_CHAN = ["general"]  # Name of the channels on which the bot is allowed

ADMIN = [0]     # Discord User ID of the admins (must be changed)
ADMIN_NAME = [""]   # Name of the ADMIN, only for initialisation
TIGRISBOT_CREATOR = 0   # Creator of the tigrisbot
INIT_MONEY = 100000000  # Amount of tigris for the first user

DEBUG = True

# INVENTORY
DB_NAME_MARKETPLACE = "./marketplace.db"    # Name of the file containing the SQLite marketplace database
ITEM_TABLE = "item"     # Name of the table containing the items
FOR_SALE_TABLE = "for_sale"     # Name of the table containing items to be sold
TRADE_TABLE = "trade"   # Name of the table containing history of trades

# PRESIDENT
PRESIDENT_ROLES_ID = 0 # Role id of president
BR_CHANNEL_ID = 0 # Channel ID for the Battle Royale des Votes

# BOUFFON
LAUGH_LIST = ["*rires*", "*trololo*", "*rires enregistrés*", "*hin hin hin*", "*ha. ha. ha.*", "*HueHueHue*", "*Haha*", "*Hahaha.*"]
LAUGHS_CATEGORIES = []  # Channel categories in which laughs work
FIBREVILLE_CHANNEL_ID = 0   # Channel ID for the bouffon interaction (must be changed)
BOUFFON_ROLES_ID = 0    # Role ID of the bouffon (must be changed)

# NINI
NINI_SAVE_FILE_PREFIX = "./nini_history_"   # Name of the prefix for files containing nini results
LOSER_ROLE_NAME = ""   # Name of the role to be applied to the NiNi loser(s)
NUMBER_OF_LOSER = 2   # Number of people to receive the loser role

# BASIC INCOME

INCOME_BASE = 1500
INCOME_STEP_VALUE = 250
