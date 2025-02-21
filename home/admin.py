from django.contrib import admin
from home.models import Contact  # ✅ Ensure it's "Contact" (capital C)

admin.site.register(Contact)  # ✅ Register the model correctly
