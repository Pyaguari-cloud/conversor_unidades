from django.shortcuts import render, get_object_or_404
from .models import Especialidad, Magnitud, Unidad
from .utils import convertir_valor


def seleccionar_magnitud(request):
    """
    Página inicial: lista especialidades y magnitudes para elegir.
    """
    especialidades = Especialidad.objects.prefetch_related("magnitudes")
    return render(request, "conversor/seleccionar_magnitud.html", {
        "especialidades": especialidades,
    })


def convertir_view(request, magnitud_id):
    """
    Formulario de conversión para una magnitud concreta.
    """
    magnitud = get_object_or_404(Magnitud, id=magnitud_id)
    unidades = magnitud.unidades.all()

    resultado = None
    error = None
    unidad_origen_sel = None
    unidad_destino_sel = None

    if request.method == "POST":
        try:
            valor = float(request.POST.get("valor", "0"))
            unidad_origen_sel = get_object_or_404(
                Unidad, id=request.POST.get("unidad_origen")
            )
            unidad_destino_sel = get_object_or_404(
                Unidad, id=request.POST.get("unidad_destino")
            )

            resultado = convertir_valor(
                magnitud.codigo_calculo,
                valor,
                unidad_origen_sel.simbolo,
                unidad_destino_sel.simbolo,
            )
        except Exception as e:
            error = str(e)

    return render(request, "conversor/convertir.html", {
        "magnitud": magnitud,
        "unidades": unidades,
        "resultado": resultado,
        "error": error,
        "unidad_origen_sel": unidad_origen_sel,
        "unidad_destino_sel": unidad_destino_sel,
    })