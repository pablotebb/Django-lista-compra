from django.urls import path  # Importa la función path de django.urls, que se usa para definir las rutas de URL.
from . import views  # Importa el módulo views desde el paquete actual (la misma aplicación).

# Lista de patrones de URL para la aplicación.
urlpatterns = [
    # Define la ruta raíz (''), que mapea a la vista product_list.
    # Cuando se accede a la raíz del sitio (por ejemplo, /appListaCompra/), se llama a views.product_list.
    # El nombre 'product_list' se usa para referirse a esta ruta en otras partes de la aplicación.
    path('', views.product_list, name='product_list'),
    
     # Define una ruta para los detalles de un producto específico.
    # La URL incluye un entero (pk) que se pasa a la vista product_detail.
    # Por ejemplo, /products/product/1/ llamará a views.product_detail con pk=1.
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Define una ruta para crear un nuevo producto.
    # Acceder a /products/product/new/ llamará a views.product_create.
    path('product/new/', views.product_create, name='product_create'),
    
    # Define una ruta para editar un producto existente.
    # La URL incluye un entero (pk) que se pasa a la vista product_edit.
    # Por ejemplo, /products/product/1/edit/ llamará a views.product_edit con pk=1.
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    
    # Define una ruta para eliminar un producto existente.
    # La URL incluye un entero (pk) que se pasa a la vista product_delete.
    # Por ejemplo, /products/product/1/delete/ llamará a views.product_delete con pk=1
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Define una ruta para alternar el estado de selección de un producto.
    # La URL incluye un entero (pk) que se pasa a la vista toggle_selected.
    # Por ejemplo, /products/product/1/toggle_selected/ llamará a views.toggle_selected con pk=1.
    path('product/<int:pk>/toggle_selected/', views.toggle_selected, name='toggle_selected'),
]
