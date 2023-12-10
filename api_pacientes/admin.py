from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "rut",
        "nombres",
        "apellidos",
        "prevision_type",
        "telefono",
        "direccion",
        "comuna",
        "fecha_nacimiento",
    )
    search_fields = ("email", "rut", "nombres", "apellidos")
    list_filter = ("prevision_type", "comuna")
