import os

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
PASSWORD = os.environ.get('MAILGUN_PASSWORD')
SMTP = os.environ.get('MAILGUN_SMTP')
PORT = os.environ.get('MAILGUN_PORT')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"
