from django.db import models

class Veiculo(models.Model):
    from .modelo import Modelo
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)

    from .cor import Cor
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)

    
    ano = models.CharField(max_length=10, null=True, default="0") #completar
    def __str__(self):
        return f"{self.ano} - {self.ano.upper()}"
    
    preco = models.CharField(max_length=100, null=True, default="0") #completar
    def __str__(self):
        return f"{self.nome}"

    from .acessorio import Acessorio
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="veiculos", null=True, blank=True)


    
    
     

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"