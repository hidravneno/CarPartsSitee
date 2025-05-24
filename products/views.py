from django.utils.timezone import now
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Part, InventoryItem
from .forms import PartForm
from django.contrib.auth.decorators import login_required, permission_required

def get_inventory_summary():
    total_parts = Part.objects.count()
    categories_count = Part.objects.values('category').distinct().count()
    recent_period = now() - timedelta(days=30)
    recent_parts_count = Part.objects.filter(created_at__gte=recent_period).count()
    return {
        'total_parts': total_parts,
        'categories_count': categories_count,
        'recent_parts_count': recent_parts_count,
    }

def home(request):
    # Simple welcome page, no inventory data passed
    return render(request, 'pages/home.html')

def inventory(request):
    context = get_inventory_summary()
    parts = Part.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        parts = parts.filter(category=selected_category)
    context['parts'] = parts
    context['categories'] = Part.objects.values_list('category', flat=True).distinct()
    context['selected_category'] = selected_category
    return render(request, 'products/inventory.html', context)

def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    context = {'part': part}
    return render(request, 'products/part_detail.html', context)

def part_edit(request, pk=None):
    part = get_object_or_404(Part, pk=pk) if pk else None
    if request.method == 'POST':
        form = PartForm(request.POST, request.FILES, instance=part)
        if form.is_valid():
            form.save()
            messages.success(request, 'Part saved successfully.')
            return redirect('inventory')
    else:
        form = PartForm(instance=part)
    return render(request, 'products/part_form.html', {'form': form})

def part_delete(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'POST':
        part.delete()
        messages.success(request, 'Part deleted successfully.')
        return redirect('inventory')
    return render(request, 'products/part_confirm_delete.html', {'part': part})

def parts_list(request):
    parts = Part.objects.all()
    selected_category = request.GET.get('category')  # Obtener la categoría seleccionada del query string
    if selected_category:
        parts = parts.filter(category=selected_category)  # Filtrar las partes por la categoría seleccionada

    categories = Part.objects.values_list('category', flat=True).distinct()  # Obtener las categorías únicas
    context = {
        'parts': parts,
        'categories': categories,
        'selected_category': selected_category,  # Pasar la categoría seleccionada al contexto
    }
    return render(request, 'products/parts_list.html', context)

@login_required
@permission_required('products.view_inventory', raise_exception=True)
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'products/inventory_list.html', {'items': items})

@login_required
@permission_required('products.manage_inventory', raise_exception=True)
def inventory_manage(request):
    # Lógica para agregar/eliminar inventario
    return render(request, 'products/inventory_manage.html')  # Asegúrate de tener esta plantilla
