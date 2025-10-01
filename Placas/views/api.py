from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from Placas.models.vehiculo import vehiculo

import json 

@csrf_exempt
def registrar_placa(request):
   
    try:
        if request.method != "POST":
            return JsonResponse({"error": "Método no permitido"}, status=405)

        data = json.loads(request.body.decode("utf-8"))
        placa =str( request.POST.get("placa")).upper().strip()
        print(f"placa:{placa}")

        if not placa:
            return JsonResponse({"error": "No se envió la placa"}, status=400)

        try:

            vehiculo = vehiculo.objects.get(placa=placa)

            return JsonResponse({
                "placa": vehiculo.placa,
                "marca": vehiculo.marca,
                "modelo": vehiculo.modelo,
                "capacidad": vehiculo.capacidad,
            })

        except vehiculo.DoesNotExist:
            return JsonResponse({"error": f"Vehículo {placa} no registrado"}, status=404)

    except Exception as e:
        return JsonResponse({"error": f"Ocurrió un error: {str(e)}"}, status=500)

        
        
    
