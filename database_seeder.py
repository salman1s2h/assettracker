import os
import django
import logging.config

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assettracker.settings')

# Setup Django
django.setup()


import uuid
from django_seed import Seed
from asset.models import AssetCatg, AssetManage




def seed_data():
    seeder = Seed.seeder()
    
    seeder.add_entity(AssetCatg, 1, {
        'asset_cat': "Monitor",
        'asset_discription': "This will Contain monitor of different brand",
    })

    seeder.add_entity(AssetCatg, 1, {
        'asset_cat': "Mouse",
        'asset_discription': "This will Contain Mouse of different brand",
    })

    seeder.add_entity(AssetCatg, 1, {
        'asset_cat': "Keyboard",
        'asset_discription': "This will Contain monitor of different brand",
    })

    seeder.add_entity(AssetCatg, 1, {
        'asset_cat': "RAM",
        'asset_discription': "This will Contain RAM of different brand",
    })

    # Seed AssetManage model with the specific category
    seeder.add_entity(AssetManage, 10, {
        'asset_name': lambda x: seeder.faker.word(),
        'asset_catg': lambda x: AssetCatg.objects.get(asset_cat='Monitor'),
        'is_active': lambda x: seeder.faker.boolean(),
    })

    seeder.add_entity(AssetManage, 20, {
        'asset_name': lambda x: seeder.faker.word(),
        'asset_catg': lambda x: AssetCatg.objects.get(asset_cat='Mouse'),
        'is_active': lambda x: seeder.faker.boolean(),
    })

    seeder.add_entity(AssetManage, 30, {
        'asset_name': lambda x: seeder.faker.word(),
        'asset_catg': lambda x: AssetCatg.objects.get(asset_cat='Keyboard'),
        'is_active': lambda x: seeder.faker.boolean(),
    })

    seeder.add_entity(AssetManage, 7, {
        'asset_name': lambda x: seeder.faker.word(),
        'asset_catg': lambda x: AssetCatg.objects.get(asset_cat='RAM'),
        'is_active': lambda x: seeder.faker.boolean(),
    })

    # Execute seeding
    seeder.execute()

# Call the seed function to populate the database
seed_data()
