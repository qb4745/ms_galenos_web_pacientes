from django.shortcuts import get_object_or_404
from ninja import Router
from api_pacientes.schemas import PacienteIn, PacienteOut
from api_pacientes.models import Paciente

from django.contrib.auth.hashers import make_password

router = Router()


@router.post("/crea", response=PacienteOut, url_name="create_paciente")
def create_paciente(request, payload: PacienteIn):
    hashed_password = make_password(payload.password)
    paciente_data = payload.dict()
    paciente_data["password"] = hashed_password
    paciente = Paciente.objects.create(**paciente_data)
    return paciente


@router.get("/lista", response=list[PacienteOut], url_name="list_pacientes")
def list_pacientes(request):
    return Paciente.objects.all()


@router.get("/lista/{int:paciente_id}", response=PacienteOut, url_name="paciente")
def get_paciente(request, paciente_id):
    return get_object_or_404(Paciente, id=paciente_id)


@router.put("/modifica/{int:paciente_id}", response=PacienteOut)
def update_paciente(request, paciente_id, payload: PacienteIn):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    for name, value in payload.dict().items():
        setattr(paciente, name, value)

    paciente.save()
    return paciente


@router.delete("/elimina/{int:paciente_id}")
def update_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    paciente.delete()

    return {"success": True}
