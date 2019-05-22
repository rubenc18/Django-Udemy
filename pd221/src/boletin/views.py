from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo = "HOLA"
	if request.user.is_authenticated:
		titulo = "Bienvenido  %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
				"titulo": titulo,
				"el_form": form,
			}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre = "PERSONA"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(instance.nombre)
		}
		if not (instance.nombre):
			context = {
				"titulo": "Gracias %s!" %(email)
			}
		print (instance)
		print (instance.timestamp)
		#form_data = form.cleaned_data
		#abc = form_data.get("email")
		#abc2 = form_data.get("nombre")
		#obj = Registrado.objects.create(email=abc, nombre=abc2)


	return render(request, "inicio.html", context)