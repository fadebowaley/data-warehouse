from app import app
import urllib
import os

# secret key for user session
app.secret_key = "@dem0l@333"


#setting up mail
app.config['MAIL_SERVER']='smtp.gmail' #mail server
app.config['MAIL_PORT'] = 587 #mail port
app.config['MAIL_USERNAME'] = 'fadebowaley@gmail.com' #email
app.config['MAIL_PASSWORD'] =  'possible12' #password
# app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD'] #password
app.config['MAIL_USE_TLS'] = True #security type
app.config['MAIL_USE_SSL'] = False #security type

#database connection parameters
# connection_params = {
#     'user': '',
#     'password': os.environ['DB_PASSWORD'],
#     'host': '',
#     'port': 'port',
#     'namespace': '',
# }
