import os
from email.message import EmailMessage


EMAIL_ADDRES=os.environ.get("EMAIL_ADDRES")
EMAIL_PASSWORD=os.environ.get("EMAIL_PASSWORD")
EMAIL_HOST=os.environ.get("EMAIL_HOST")
EMAIL_PORT=os.environ.get("EMAIL_PORT")