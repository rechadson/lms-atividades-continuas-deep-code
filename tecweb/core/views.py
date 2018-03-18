from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'GET':
        return render(request, 'contato.html')
    else:
        print (request.POST.get('nome'))
        return render(request,'contato.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if request.method == 'POST':
            if request.POST.get("pwd") == 'teste123':
                print("Usuario", request.POST.get('email'), "entrou com sucesso")
                return render(request,'index.html')
            else:
                print("Usuario", request.POST.get("email"), "Digitou a senha errada")
                return render(request, 'login.html')
