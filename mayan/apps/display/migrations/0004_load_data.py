from django.db import migrations, models
from django.core.management import call_command
import os

def load_fixture(apps, schema_editor):
    app_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    json_path = os.path.join(app_path, 'fixtures', 'data.json')
    call_command("loaddata", json_path)

class Migration(migrations.Migration):  

    dependencies = [
        ('display', '0003_add_fake_reviews'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]