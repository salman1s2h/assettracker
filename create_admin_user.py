import os
import django
import logging.config

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assettracker.settings')

# Setup Django
django.setup()

# Now you can import your models and run Django code
from django.contrib.auth import get_user_model

def create_superuser(username, email, password):
    # Get the custom user model
    User = get_user_model()
    
    # Create superuser
    superuser = User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully.")

# Manually configure logging to avoid ImproperlyConfigured error
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
}

logging.config.dictConfig(logging_config)

# Usage example:
create_superuser('admin', 'admin@test.com', 'admin')
