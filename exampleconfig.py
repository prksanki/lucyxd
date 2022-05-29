from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 4390713
  API_HASH = "1048cd9670d6ff78e06649d7d711dd7c"

  # the name to display in your alive message.
  # If not filled anything then default value is Mafia User.
  ALIVE_NAME = "LUCY USER "
  ABUSE = "ON"
  BAN_PIC = "https://telegra.ph/file/736f13fd86d7bf6ebac95.jpg"
  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://pnsftyvf:8MOqY9w1AcqebUHRe_aI0UHMnk3k4ciT@fanny.db.elephantsql.com/pnsftyvf"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  STRING_SESSION = "1BVtsOJUBu13VM08R2fOaAGO9ysJ2p8R4BMrLd3DdeHxaHTW6PtLTkx-TryKiDV7lBTI0njlf1kXDPHkGIkHvbxPxKksbiE5gMYKjcaf9EzzsYtGz-M3kkPrqWLT1h2EyondE4yZZBGosOlZuYhhFv1_YWvBX5D7grqxdYJ__8nnxriAcjQpnjw2hn7_AeMPn7INDmpjpKBQtyUKWaeFY5hnuJgJlfRvumjq9gLwLDTJQTtE6jGKJW0299Y_cItLYrpj8OQwTxQ2fSXEHrPScAHQqb3Be3QsoWogfkZx0FAG024aEizB5_I5vhmhN5JNVy-45P_ZCAQM4wVBI_VCK65KNrTuOAmQ="

  # Create a bot in @botfather and fill the following values with bot token and username.
  TG_BOT_TOKEN_BF_HER = "5220470824:AAFWHXol_gG4JMKGasFQVCHPgAKNtuwW-YQ" #token
  TG_BOT_USER_NAME_BF_HER = "PrkMafiabot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -1001606123062
          MAFIABOT_LOGGER = -1001606123062
  # Custom Command Handler. 
  COMMAND_HAND_LER = "."

  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = "."
  
  
