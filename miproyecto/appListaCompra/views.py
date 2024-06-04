from django.shortcuts import render, redirect  # Importa las funciones render y redirect de Django.
from .models import Product  # Importa el modelo Product del archivo models.py en la misma aplicación.
from .forms import ProductForm  # Importa el formulario ProductForm del archivo forms.py en la misma aplicación.


# Vista para listar todos los productos.
def product_list(request):
    # Obtiene todos los objetos Product de la base de datos.
    products = Product.objects.all()
    # Renderiza la plantilla 'appListaCompra_list.html' con el contexto de los productos.
    return render(request, 'appListaCompra/appListaCompra_list.html', {'products': products})

# Vista para mostrar los detalles de un producto específico.
def product_detail(request, pk):
    # Obtiene un único objeto Product usando la clave primaria (pk).
    product = Product.objects.get(pk=pk)
    # Renderiza la plantilla 'appListaCompra_detail.html' con el contexto del producto específico.
    return render(request, 'appListaCompra/appListaCompra_detail.html', {'product': product})

# Vista para crear un nuevo producto.
def product_create(request):
    # Si la solicitud es POST, significa que el formulario ha sido enviado.
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados.
        form = ProductForm(request.POST)
        # Verifica si el formulario es válido.
        if form.is_valid():
            # Guarda el nuevo producto en la base de datos.
            form.save()
            # Redirige a la lista de productos.
            return redirect('product_list')
    else:
        # Si la solicitud no es POST, crea un formulario vacío.
        form = ProductForm()
    # Renderiza la plantilla 'appListaCompra_form.html' con el formulario.
    return render(request, 'appListaCompra/appListaCompra_form.html', {'form': form})

# Vista para editar un producto existente
def product_edit(request, pk):
    # Obtiene el producto a editar usando la clave primaria (pk).
    product = Product.objects.get(pk=pk)
    # Si la solicitud es POST, significa que el formulario ha sido enviado.
    if request.method == 'POST':
        # Crea una instancia del formulario con los datos enviados y el producto existente.
        form = ProductForm(request.POST, instance=product)
        # Verifica si el formulario es válido.
        if form.is_valid():
            # Guarda los cambios del producto en la base de datos.
            form.save()
            # Redirige a la lista de productos.
            return redirect('product_list')
    else:
        # Si la solicitud no es POST, crea un formulario con los datos del producto existente.
        form = ProductForm(instance=product)
    # Renderiza la plantilla 'product_form.html' con el formulario.
    return render(request, 'appListaCompra/appListaCompra_form.html', {'form': form})

# Vista para eliminar un producto existente.
def product_delete(request, pk):
    # Obtiene el producto a eliminar usando la clave primaria (pk).
    product = Product.objects.get(pk=pk)
    # Si la solicitud es POST, significa que se ha confirmado la eliminación.
    if request.method == 'POST':
        # Elimina el producto de la base de datos.
        product.delete()
        # Redirige a la lista de productos.
        return redirect('product_list')
    # Renderiza la plantilla 'appListaCompra_delete.html' para confirmar la eliminación.
    return render(request, 'appListaCompra/appListaCompra_delete.html', {'product': product})


# Vista para alternar el estado de seleccionado de un producto.
def toggle_selected(request, pk):
    # Obtiene el producto usando la clave primaria (pk).
    product = Product.objects.get(pk=pk)
    # Alterna el estado de seleccionado.
    product.selected = not product.selected
    # Guarda el cambio en la base de datos.
    product.save()
    # Redirige a la lista de productos.
    return redirect('product_list')

