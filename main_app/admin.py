from django.contrib import admin

from .models import Cat, Feeding, Toy  # import the model

admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Toy)