from django.contrib import admin
from .models import Account, Component, Assembly, AssemblyDetail
# Register your models here.
admin.site.register([Account, Component, Assembly, AssemblyDetail])