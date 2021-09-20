from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from users.models import Ciudad


##AJAX UTIL VIEW

def load_cities(request):
    departamento_id = request.GET.get('id_departamento')
    ciudad = Ciudad.objects.filter(departamento_id = departamento_id).all()
    return render(request, 'GolGana/cities_dropdown.html', {'ciudades': ciudad})

class Home(generic.TemplateView):
    template_name = 'GolGana/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = "GolGana"
        return context



