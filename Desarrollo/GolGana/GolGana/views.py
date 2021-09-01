from django.views import generic

class Home(generic.TemplateView):
    template_name = 'GolGana/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = "GolGana"
        return context