# assettracker
Create virtual enviroment by bellow command
cmd : virtualenv -p /usr/bin/python3 venv
Then activate virtual enviroment by bellow command
cmd :source venv/bin/activate
Then insatll all python package by bellow command
cmd : pip install -r requirements.txt
Create .env file and create variable which are we using in setting.py like DATABASE_NAME,DATABASE_USER,DATABASE_PASSWORD etc..
I am using postgres DATABASE and it look like bellow 
'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.getenv('DATABASE_NAME'),
         'USER': os.getenv('DATABASE_USER'),
         'PASSWORD': os.getenv('DATABASE_PASSWORD'),
         'HOST': 'localhost',
         'PORT': '5432',
   }
Then run python manage.py makemigrations 
Then python manage.py migrate  
Then Create admin user by running python script in create_admin_user.py 
Then populate database by running script in database_seeder.py
After this setting we have to run python manage.py runserver
Now we have to go on http://127.0.0.1:8000/auth/login/
NOW login with User name is : admin@test.com
                         pwd: admin
