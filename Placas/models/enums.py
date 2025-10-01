from django.db import models

class tipo_monitor (models.TextChoices): 
    INSTITUCION = 'institución', 'Institución '
    TERCERO = 'tercero', 'Tercero'

class punto_encuentro (models.TextChoices):
    PORTERIA_1 = 'porteria 1', 'Porteria 1'
    PORTERIA_2 = 'porteria 2', 'Porteria 2'
    SUBIENDO = 'subiendo', 'Subiendo'
    BAJANDO = 'bajando', 'Bajando'

class tipo_licencia (models.TextChoices):
    A1 = 'A1' , 'A1'
    A2 = 'A2' , 'A2'
    B1 = 'B1' , 'B1'
    B2 = 'B2' , 'B2'
    C1 = 'C1' , 'C1'
    C2 = 'C2' , 'C2'

class grado (models.TextChoices):
    PREESCOLAR = 'preescolar', 'Preescolar'
    PRIMERO = 'primero','Primero'
    SEGUNDO = 'segundo', 'Segundo'
    TERCERO =  'tercero', 'Tercero'
    CUARTO = 'cuarto', 'Cuarto'
    QUINTO = 'quinto', 'Quinto'
    SEXTO = 'sexto', 'Sexto'
    SEPTIMO = 'septimo' , 'Septimo'
    OCTAVO = 'octavo' , 'Octavo'
    NOVENO = 'noveno' , 'Noveno'
    DECIMO = 'decimo' , 'Decimo'
    ONCE = 'once' , 'Once'

class tipo_monitor_institucion (models.TextChoices):
    INSTITUCION = 'institucion', 'Institución'
    TERCERO = 'tercero', 'Tercero'