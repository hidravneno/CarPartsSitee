from django.shortcuts import render, get_object_or_404, redirect
from .models import Part
from .forms import PartForm

def parts_list(request):
    parts = Part.objects.all()
    return render(request, 'products/parts_list.html', {'parts': parts})

def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    return render(request, 'products/part_detail.html', {'part': part})

def part_edit(request, pk=None):
    if pk:
        part = get_object_or_404(Part, pk=pk)
    else:
        part = None
    form = PartForm(request.POST or None, request.FILES or None, instance=part)  # Agrega request.FILES aquí
    if form.is_valid():
        form.save()
        return redirect('parts_list')
    return render(request, 'products/part_form.html', {'form': form})
