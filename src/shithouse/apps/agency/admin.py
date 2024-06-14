from django.contrib import admin
from shithouse.apps.agency import models

admin.site.register([models.Agency, models.Agent, models.Branch])