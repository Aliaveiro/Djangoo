from django.contrib import admin
from .models import Contact, Photos, Commentaire, Gestion, Mandat

# Register your models here.


admin.site.register(Contact)
admin.site.register(Photos)
admin.site.register(Commentaire)
admin.site.register(Gestion)
admin.site.register(Mandat)
