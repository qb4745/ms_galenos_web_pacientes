from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from api_pacientes.api import router as paciente_router
from django.views.generic import RedirectView

galenos = NinjaAPI()
galenos.add_router("/web/pacientes/", paciente_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("galenos/", galenos.urls),
    path("", RedirectView.as_view(url="/galenos/docs"), name="redirect-to-docs"),
]
