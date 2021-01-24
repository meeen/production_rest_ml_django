from django.contrib import admin

# Register your models here.

from .models import machine
admin.site.register(machine)

from .models import product_typ
admin.site.register(product_typ)

from .models import production
admin.site.register(production)



from .models import order
admin.site.register(order)

from .models import tool_change
admin.site.register(tool_change)