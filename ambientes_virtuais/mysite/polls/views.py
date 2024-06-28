from django.shortcuts import render

#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render, redirect
from .forms import LoginForm

def registro_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário se forem válidos
            form.save()
            return redirect('sucesso')
    else:
        form = LoginForm()

    return render(request, 'registro.html', {'form': form})

def index(request):
    return render(request, '../templates/index.html')