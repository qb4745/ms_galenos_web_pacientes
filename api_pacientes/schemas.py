# Westeros/stark/schemas.py
from ninja import ModelSchema
from api_pacientes.models import Paciente


class PacienteIn(ModelSchema):
    class Config:
        model = Paciente
        model_exclude = [
            "id",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        ]


class PacienteOut(ModelSchema):
    class Config:
        model = Paciente
        model_fields = "__all__"
