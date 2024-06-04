from django import forms  # Importa el módulo forms de Django, que proporciona herramientas para trabajar con formularios.
from .models import Product  # Importa el modelo Product del archivo models.py en la misma aplicación.

# Define la clase ProductForm que hereda de forms.ModelForm.
class ProductForm(forms.ModelForm):
    # Clase interna Meta que define la configuración del formulario.
    class Meta:
        # Especifica que este formulario está asociado con el modelo Product.
        model = Product
        # Lista de campos del modelo que estarán incluidos en el formulario.
        fields = ['name', 'description', 'price']
