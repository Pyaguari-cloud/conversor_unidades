from django.db import models

# 1. El nivel más alto (Tus 3 pilares)
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True) # Ciencias, Contabilidad, Informática
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre

# 2. El tipo de conversión dentro de la especialidad
class Magnitud(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='magnitudes')
    nombre = models.CharField(max_length=100) # Ej: Temperatura, Almacenamiento, IVA
    
    # Este campo es clave: le dirá a tu view qué función de Python usar
    codigo_calculo = models.CharField(max_length=50, unique=True) # Ej: 'calc_temp', 'calc_bytes', 'calc_iva'

    def __str__(self):
        return f"{self.especialidad.nombre} - {self.nombre}"

# 3. Las unidades a mostrar en los selectores
class Unidad(models.Model):
    magnitud = models.ForeignKey(Magnitud, on_delete=models.CASCADE, related_name='unidades')
    nombre = models.CharField(max_length=50) # Ej: Celsius, Megabyte, Dólar
    simbolo = models.CharField(max_length=10) # Ej: °C, MB, $
    
    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"