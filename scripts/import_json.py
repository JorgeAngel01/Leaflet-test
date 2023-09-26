
import os
import sys

# Add the directory containing your Django project to the Python path
sys.path.append('/home/angel/Desktop/a/Leaflet-test')

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django

# Call django.setup() to set up the Django environment
django.setup()


import json
from mymap.models import Location 
from django.core.exceptions import ValidationError


def import_locations_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    for item in data:
        try:
            Location.objects.create(
                Nombre=item['Nombre'],
                Descripcion=item['Descripcion'],
                Lat=item['Lat'],
                Lng=item['Lng']
            )
        except ValidationError as e:
            print(f"Error importing data: {e}")

if __name__ == "__main__":
    json_filename = "/home/angel/Desktop/a/Leaflet-test/static/places.json" 
    import_locations_from_json(json_filename)
