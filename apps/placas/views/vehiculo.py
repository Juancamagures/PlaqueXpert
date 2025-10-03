from rest_framework import status
from rest_framework import viewsets
from apps.placas.models.vehiculo import Vehiculo
from apps.placas.serializers.vehiculo import VehiculoSerializers
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError


"""
    GET : OBTENER
    POST: ENVIAR
    PUT | PATCH : EDITAR
    DELETE: ELIMINAR
"""
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset=Vehiculo.objects.all()
    serializer_class=VehiculoSerializers

    def retrieve(self, request, *args, **kwargs):
        #Sobrescribe el método RETRIEVE (GET /vehiculos/pk/)
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {
                    "error": f"El vehículo no existe"
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request, *args, **kwargs):
        # Sobrescribe el método POST para manejar la creación de un nuevo profesor.
        # Se crear una instanca del profesor serializer
        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
            try:
                instance = serializer.save()
                # Valida el modelo
                instance.full_clean()
                
                # Obtener la lista completa actualizada
                vehiculos = self.get_queryset()
                lista_serializer = self.get_serializer(vehiculos, many=True)
                return Response(lista_serializer.data, status=status.HTTP_201_CREATED)
            
            except DRFValidationError as e:
                 instance.delete() 
                 raise DRFValidationError(e.message_dict)
            
            # En caso de que quisiera solamente retornar el objeto creado
                # response_serializer = self.get_serializer(instance)
                # return Response(response_serializer.data, status=201)
        
        else:
            return Response(
                {
                    "message": "Hubo un error al crear el vehículo",
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def update(self, request, *args, **kwargs):
        # Sobrescribe el método UPDATE (PUT/PATCH) para manejar la actualización de un profesor.
        """
            Partial se utliza para permitir actualizaciones parciales
            Aquí, partial se pasa al serializer, permitiendo una actualización total (PUT) o parcial (PATCH), dependiendo de si vino como partial=True
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            try:
                instance = serializer.save()
                instance.full_clean()
                
                # Obtener la lista completa actualizada
                vehiculos = self.get_queryset()
                lista_serializer = self.get_serializer(vehiculos, many=True)
                return Response(lista_serializer.data, status=status.HTTP_201_CREATED)
            
            except DRFValidationError as e:
                 instance.delete() 
                 raise DRFValidationError(e.message_dict)

        else:
            return Response(
                {
                    "message": "Hubo un error al actualizar el vehículo",
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
            #Sobrescribe el método DESTROY para eliminar un profesor
        try:
            instance = self.get_object()
            self.perform_destroy(instance)

            #Retorno toda la lista de vehiculos.
            vehiculos = self.get_queryset()
            serializer = self.get_serializer(vehiculos, many=True)
            return Response( serializer.data, status=status.HTTP_200_OK)
        
        except Exception :
            return Response(
                {
                    "error": f"El vehículo no existe"
                },
                status=status.HTTP_404_NOT_FOUND
            )

