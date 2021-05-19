import os
import datetime

DEBUG=True
SECRET_KEY =os.urandom(24)
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=20)


UPLOAD_FOLDER='static\\files\\'