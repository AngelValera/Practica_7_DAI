from django import forms
from app.models import Bar, Tapa
from django.contrib.auth.models import User

class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre del bar.")
    visitas  = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    direccion = forms.CharField(max_length=128,label="Introduce la direccion del bar", help_text="Direccion con formato: <Pais, ciudad, calle>")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('nombre', 'direccion')

class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce el nombre de la tapa.", widget=forms.TextInput())
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols': 50}),max_length=200, help_text="Introduce una breve descripcion  de la tapa.")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    bar = forms.ModelChoiceField(queryset=Bar.objects.all(),empty_label=None,help_text="Introduce el bar al que pertenece la tapa.")



    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            tapa = Tapa.objects.get(nombre=nombre, bar=self.cleaned_data['bar'])
        except Tapa.DoesNotExist:
            return nombre
        raise forms.ValidationError('***Esta tapa ya existe en este bar***')

    #picture = forms.ImageField(required=True)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa
        fields = ('bar','nombre','descripcion')



class RegistroForm(forms.Form):
    nombre = forms.CharField(label="Nombre :", widget=forms.TextInput())
    apellido = forms.CharField(label="Apellido :", widget=forms.TextInput())
    username = forms.CharField(label="Cuenta :", widget=forms.TextInput())
    email = forms.EmailField(label="Email :", widget=forms.EmailInput())
    password = forms.CharField(label="password :", widget=forms.PasswordInput(render_value=False),max_length=8,help_text="(numeros y letras hasta 8)")
    password2 = forms.CharField(label="confirmar password :", widget=forms.PasswordInput(render_value=False),max_length=8)

    def clean_username(self):
        print "Entra en el metodo"
    	username = self.cleaned_data['username']
    	try:
    		u = User.objects.get(username=username)
    	except User.DoesNotExist:
    		return username
    	raise forms.ValidationError('***Usuario ya existe***')
    def clean_email(self):
    	email = self.cleaned_data['email']
    	try:
    		u = User.objects.get(email=email)
    	except User.DoesNotExist:
    		return email
    	raise forms.ValidationError('***Correo ya registrado***')
    def clean_password2(self):
    	password = self.cleaned_data['password']
    	password2 = self.cleaned_data['password2']
    	if password==password2:
    		pass
    	else:
    		raise forms.ValidationError('***Passwords no coinciden**')
    class Meta:
        model = User
        fields = ( 'nombre','apellido','username','email','password','password2')
