from django.shortcuts import render
from django.contrib import messages

from .models import Visitor


def greeting(request):
	if request.method == 'POST':
		name = request.POST['name']
		surname = request.POST['surname']

		if Visitor.objects.filter(name=name, surname=surname):
			messages.success(request, f"Вже бачилися, {name} {surname}!")

		else:
			new_visitor = Visitor(name=name, surname=surname)
			new_visitor.save(request)

			messages.success(request, f"Привiт, {name} {surname}!")

	return render(request, 'greetingapp/greeting.html')


def visitors_list(request):
	return render(request, 'greetingapp/visitors.html', {'visitors': Visitor.objects.all()})
