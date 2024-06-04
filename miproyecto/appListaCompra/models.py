from django.db import models  # Importa el módulo models de Django para definir modelos de base de datos.

# Define la clase Product que representa el modelo de un producto en la base de datos.
class Product(models.Model):
    # Campo 'name' de tipo CharField, con un máximo de 100 caracteres.
    name = models.CharField(max_length=100)
    
    # Campo 'description' de tipo TextField, que permite almacenar texto largo.
    description = models.TextField()
    
    # Campo 'price' de tipo DecimalField, que almacena números decimales con hasta 10 dígitos en total y 2 decimales.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Campo 'selected' de tipo BooleanField, que indica si el producto está seleccionado. Por defecto es False.
    selected = models.BooleanField(default=False)

    # Método especial __str__ que devuelve el nombre del producto cuando se imprime un objeto Product.
    def __str__(self):
        return self.name
