from datetime import date
from typing import Optional

from django.db.models import Avg, FloatField, PositiveIntegerField, Sum
from ninja import Router, Schema
from ninja.responses import Status, codes_4xx

from foco.models import Foco

router = Router()


class Message(Schema):
    mensagem: str


class RegistroFocoSchemaPayload(Schema):
    nivel_foco: int
    tempo_minutos: int
    comentario: Optional[str] = None
    categoria: Optional[str] = None
    data: Optional[date] = None


class RegistroFocoSchemaResponse(Schema):
    id: int


class DiagnosticoResponse(Schema):
    media: float
    tempo_total: int
    feedback: str


@router.post(
    "/registro-foco", response={201: RegistroFocoSchemaResponse, codes_4xx: Message}
)
def cria_registro(request, payload: RegistroFocoSchemaPayload):
    if payload.nivel_foco <= 0 or payload.nivel_foco > 5:
        return Status(400, {"mensagem": "O nivel_foco deve ser de 1 a 5"})

    created = Foco.objects.create(
        nivel_foco=payload.nivel_foco,
        tempo_minutos=payload.tempo_minutos,
        comentario=payload.comentario,
        categoria=payload.categoria,
        data=payload.data,
    )

    return Status(201, {"id": created.id})


@router.get(
    "/diagnostico-produtividade",
    response={200: DiagnosticoResponse, codes_4xx: Message},
)
def gera_diagnostico(request):
    all = Foco.objects.all()

    response = all.aggregate(
        tempo_total=Sum("tempo_minutos", output_field=PositiveIntegerField()),
        media=Avg("nivel_foco", output_field=FloatField()),
    )


    if response["media"] < 3.0:
        response["feedback"] = "Pausas mais longas e menos notificações"
    elif response["media"] > 4.0:
        response["feedback"] = "Você está em uma maratona produtiva de alto nível!"
    else:
        response["feedback"] = "Sua media esta media :)"

    return Status(200, response)
