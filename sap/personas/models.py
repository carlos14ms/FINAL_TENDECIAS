from django.db import models

class persona(models.Model):
    nombre_completo = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    correo_electronico = models.EmailField(max_length=254)
    nombre_evento = models.CharField(max_length=250, default='sin evento')
    OPCIONES_BOLETO = (
        ('general', 'General'),
        ('palcos', 'Palcos'),
        ('preferencial', 'Preferencial'),
    )
    tipo_boleto = models.CharField(max_length=20, choices=OPCIONES_BOLETO)
