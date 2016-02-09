from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from app.models import Bar, Tapa
from app.forms import BarForm,  TapaForm, RegistroForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    context_dict = {}

    bares_ordenados = Bar.objects.order_by('-visitas')[:5]
    context_dict['bares_ordenados']= bares_ordenados

    bares = Bar.objects.all()
    context_dict['bares']= bares

    tapas = Tapa.objects.order_by('-votos')[:5]
    context_dict['tapas']= tapas

    # Render the response and send it back!
    return render(request, 'app/index.html', context_dict)

def bar(request, bar_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        bares = Bar.objects.all()
        context_dict['bares']= bares

        bar = Bar.objects.get(slug=bar_name_slug)
        context_dict['bar_name'] = bar.nombre
        context_dict['bar_direccion'] = bar.direccion
        nueva_visita=bar.visitas+1
        bar.visitas=nueva_visita
        bar.save()
        context_dict['bar_visitas'] = bar.visitas

        tapas = Tapa.objects.filter(bar=bar)

        # Adds our results list to the template context under name pages.
        context_dict['tapas'] = tapas
        context_dict['bar'] = bar
    except Bar.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'app/bar.html', context_dict)

def tapa(request, bar_name_slug, tapa_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    try:
        bares = Bar.objects.all()
        context_dict['bares']= bares
        bar = Bar.objects.get(slug=bar_name_slug)
        tapas = Tapa.objects.all()
        context_dict['tapas']= tapas

        tapa = Tapa.objects.get(slug=tapa_name_slug, bar=bar)
        context_dict['tapa'] = tapa
        context_dict['tapa_id'] = tapa
        context_dict['tapa_name'] = tapa.nombre
        context_dict['tapa_voto'] = tapa.votos
        context_dict['tapa_descripcion'] = tapa.descripcion
        context_dict['tapa_imagen'] = tapa.picture
        context_dict['tapa_bar'] = tapa.bar
        # Adds our results list to the template context under name pages.
        context_dict['tapas'] = tapas
    except Tapa.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'app/tapa.html', context_dict)

def user_login(request):
    context_dict = {}
    bares = Bar.objects.all()
    context_dict['bares']= bares
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Tu cuenta fue desactivada.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'app/login.html', context_dict )

@login_required
def add_bar(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BarForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BarForm()


    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}
    context_dict['form'] = form

    bares = Bar.objects.all()
    context_dict['bares']= bares

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'app/add_bar.html', context_dict)

@login_required
def add_tapa(request):
    # Create a context dictionary which we can pass to the template rendering engine.
    print "llama a crear tapa"
    context_dict = {}

    bares = Bar.objects.all()
    context_dict['bares']= bares
    # A HTTP POST?
    if request.method == 'POST':
        form = TapaForm(request.POST,request.FILES)
        # Have we been provided with a valid form?
        if form.is_valid():
            if 'picture' in request.FILES:
                form.picture = request.FILES['picture']
            # Save the new category to the database.
            form.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = TapaForm()

    context_dict['form'] = form


    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'app/add_tapa.html', context_dict)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

def registrar_usuario(request)	:
    bares = Bar.objects.all()
    if request.method == "POST":
    	formulario = RegistroForm(data=request.POST)
    	if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            apellido = formulario.cleaned_data['apellido']
            name = formulario.cleaned_data['username']
            email = formulario.cleaned_data['email']
            password = formulario.cleaned_data['password']
            u = User.objects.create_user(username=name,email=email,password=password,first_name=nombre,last_name=apellido)
            u.save()
            user = authenticate(username=name, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Tu cuenta fue desactivada.")
            else:
                print formulario.errors
            #login(request, user)
            #return HttpResponseRedirect("/")
    	else:
            print formulario.errors
    else:
    	formulario = RegistroForm()

    return render(request,"app/registro.html", {"formulario":formulario, 'bares': bares})

def reclama_datos (request):
    datos = {}
    vbares=[]
    vVisitas=[]
    bares = Bar.objects.order_by('-visitas')
    for bar in bares:
        vbares.append(bar.nombre)
        vVisitas.append(bar.visitas)
    datos ['bares']= vbares
    datos ['visitas']= vVisitas
    return JsonResponse(datos, safe=False)

@login_required
def voto_tapa(request):
    tapa_id = None
    if request.method == 'GET':
        tapa_id = request.GET['tapa_id']
        print tapa_id
    votos = 0
    if tapa_id:
        tapa = Tapa.objects.get(id=int(tapa_id))
        if tapa:
            votos = tapa.votos + 1
            tapa.votos =  votos
            tapa.save()

    return HttpResponse(votos)
