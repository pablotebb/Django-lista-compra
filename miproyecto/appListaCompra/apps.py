from django.apps import AppConfig  # Importa la clase AppConfig del módulo apps de Django

class ApplistacompraConfig(AppConfig):
    # Configuración para el campo auto incremental predeterminado para los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    # Nombre de la aplicación
    name = 'appListaCompra'

