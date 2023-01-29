import os
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN','1948196001:AAGifVfJ-ZsdZsdL-EU5jHAZOfyl_4kQWiM')
    GUSERNAME = os.environ.get('GUSER_NAME','pythoncp@gmail.com')
    GPASSWORD = os.environ.get('GPASSWORD','*12345678#')
    SCHEDULE = os.environ.get('SCHEDULE', True)
    USERID = os.environ.get('USERID','1344298238')
# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', 'BOT_TOKEN_HERE')
# GUSERNAME = os.environ.get('GUSER_NAME', 'Google Email')
# GPASSWORD = os.environ.get('GPASSWORD', 'Google Email Password')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
