from .models import Empresa, Reserva, Cancha
from users.models import Ciudad, Departamento
from django.db.models.base import Model
from django.forms import ModelForm, Textarea

class UpdateEmpresaForm(ModelForm):
    
    class Meta:
        model = Empresa
        fields = ['nombre', 'descripcion', 'direccion', 'telefono','ciudad', 'departamento', 'hora_inicio', 'hora_final', 'image']
        widgets = {'descripcion': Textarea(attrs={'rows': 5, 'cols': 90, 'max_length': '120', 'style': 'resize:none;'})}

    def __init__(self, *args, **kwargs):
        super(UpdateEmpresaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['ciudad'].queryset = Ciudad.objects.none() 

#SI SE CREA UN PERFIL NUEVO ESTO DARA ERROR A LA HORA DE CARGAR LAS CIUDADES DEL DEPARTEMENTO 
        if 'departamento' in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(departamento_id = departamento_id).order_by('nombre')
                
            except(ValueError, TypeError):
                pass
        ###SOLUCION CUANDO LA CIUDAD ESTA NULL
        elif self.instance.pk:
            try:
                self.fields['ciudad'].queryset = self.instance.departamento.ciudad_set.order_by('nombre')
            except:
                pass 

class CrearReserva(ModelForm):
    class Meta:
        model = Reserva
        fields = ['cancha', 'precio', 'date']

class CrearCancha(ModelForm):
    class Meta:
        model = Cancha
        fields = ['nombre', 'jugadores', 'image']
