from django.contrib import admin
from .models import Variable, Tipo_nodo, Tipo_ubicacion, Tipo_sensor, Ubicacion, Nodo, Sensor, Lectura
# Register your models here.


admin.site.register(Variable)
admin.site.register(Tipo_ubicacion)
admin.site.register(Tipo_sensor)
admin.site.register(Ubicacion)
admin.site.register(Nodo)
admin.site.register(Sensor)
admin.site.register(Lectura)
admin.site.register(Tipo_nodo)

