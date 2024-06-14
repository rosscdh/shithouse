from django.contrib import admin

from shithouse.apps.house import models


admin.site.register([models.Address])