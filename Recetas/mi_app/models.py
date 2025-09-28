from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    resumen = models.CharField(max_length=160, blank=True, help_text="Descripción breve (máx. 160 chars)")
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='media/imgs', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    