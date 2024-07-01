from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=100)

    from .marca import Marca
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos", null=True, blank=True)

    from .categoria import Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelos", null=True, blank=True)

    
    
     

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"