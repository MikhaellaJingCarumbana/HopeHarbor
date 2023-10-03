from django.contrib import admin
from Beneficiary.models import Beneficiary  # Import the Beneficiary model from your app's models.py file

# Register the Beneficiary model with the admin interface
admin.site.register(Beneficiary)
