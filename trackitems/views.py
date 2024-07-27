from trackitems.models import Tracking, Pieza
from trackitems.forms import TrackingForm
from django.shortcuts import render, get_object_or_404, redirect

def HomeView(request):
    # Obtener todos los objetos de Empresa, Pieza y Tracking
    piezas = Pieza.objects.all()
    trackings = Tracking.objects.all()
    
    # Pasar los datos al template
    return render(request, 'index.html', {
        'piezas': piezas,
        'trackings': trackings,
    })

def TrackingDetailView(request, id):
    tracking = get_object_or_404(Tracking, id=id)
    return render(request, 'tracking_detail.html', {"tracking": tracking})

def edit_tracking(request, id):
    tracking = get_object_or_404(Tracking, id=id)
    if request.method == 'POST':
        form = TrackingForm(request.POST, instance=tracking)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la lista después de guardar
    else:
        form = TrackingForm(instance=tracking)
    return render(request, 'edit_tracking.html', {'form': form, 'tracking': tracking})