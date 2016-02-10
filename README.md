# **Practica_7_DAI:**
 
**Ángel Valera  Motos**


[![resultado del test](https://travis-ci.org/AngelValera/Practica_7_DAI.svg?branch=master)](https://snap-ci.com/AngelValera/bares-y-tapas-DAI/branch/master/build_image)

[![SnapCI](https://snap-ci.com/AngelValera/Practica_7_DAI/branch/master/build_image)](https://snap-ci.com/AngelValera/Practica_7_DAI/branch/master/build_image)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://practica7daiavm.herokuapp.com/)


##**Despliegue en un Paas Heroku**##


He decidido desplegar la aplicación que hicimos en las prácticas anteriores de bares y tapas en heroku, de manera que poniendo en el settings.py:

```python
DEBUG = False
ALLOWED_HOSTS = ['*']
```
La aplicación siga funcionando correctamente en el puerto 80, concretamente que los ficheros estáticos sigan funcionando, ya que al poner Debug=false, estos dejan de funcionar.

La aplicación podemos verla funcionando **[aquí](http://practica7daiavm.herokuapp.com/)**.

Dicho esto para desplegar la aplicación he hecho lo siguiente:



Primero necesitamos una serie de ficheros que necesitamos para el despliegue, estos son:

- **[Procfile](https://github.com/AngelValera/Practica_7_DAI/blob/master/Procfile):** se usa para que heroku sepa que tiene que ejecutar, para ello utiliza gunicorn:

```
web: gunicorn proyecto_DAI.wsgi --log-file -
```
- **[requirements.txt](https://github.com/AngelValera/Practica_7_DAI/blob/master/requirements.txt)**: para que la aplicación funcione necesita indicar que necesita para ejecutarse:

```
Django==1.8.5
argparse==1.2.1
dj-database-url==0.3.0
dj-static==0.0.6
django-toolbelt==0.0.1
djangorestframework==3.3.1
django-bootstrap-toolkit==2.15.0
django-classy-tags==0.6.2
django-easy-maps==0.9.2
foreman==0.9.7
futures==3.0.3
gunicorn==19.3.0
psycopg2==2.4.5
Pillow==2.3.0
requests==2.8.1
requests-futures==0.9.5
static3==0.6.1
setuptools==0.7.3
WTForms==2.0.2
whitenoise==2.0.6
wheel==0.26.0
wsgiref==0.1.2
```

Una vez definidos estos ficheros debemos desplegarla en heroku, para ello hay que realizar una serie de comandos:

Lo primero es clonarnos el repositorio de [github](https://github.com/AngelValera/Practica_7_DAI) de la aplicación y acontinuación:

**wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh**

**heroku login**-->Nos logueamos dentro de heroku

**heroku create**-->Creamos la aplicación dentro de heroku

**heroku apps:rename practica7daiavm**-->Le cambiamos el nombre que nos pone por defecto por el de practica7daiavm

**git push heroku master**-->La desplegamos.

Hecho esto, ya tenemos la aplicación desplegada.

Ahora añadimos integracion continua con Snap-ci, para ello seleccionamos el repositorio que queremos y lo configuramos de la siguiente manera:

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_014_zpsswl0efhx.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_015_zpslbfybkxq.png)

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_016_zpsarihuseh.png)

Con esto cada vez que hagamos push  nos pasará los test y si son satisfactorios desplegará la aplicación.

##**Directorio /static con Debug=False**

Para que nos siga sirviendo el contenido estático, he añadido las siguientes líneas a los archivos proyecto_DAI/settings.py y proyecto_DAI/urls.py:

**En [proyecto_DAI/settings.py](https://github.com/AngelValera/Practica_7_DAI/blob/master/proyecto_DAI/settings.py):**

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
```

**En [proyecto_DAI/urls.py](https://github.com/AngelValera/Practica_7_DAI/blob/master/proyecto_DAI/urls.py):**

```python
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
```

Añadidas estas líneas, podemos ver que la aplicación está funcionando, sirviendo el contenido que hay en la carpeta [/static](https://github.com/AngelValera/Practica_7_DAI/tree/master/static) y desplegada en heroku.

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_017_zpsm5ipzpz6.png)



Por último, para que se vean las imágenes de /media, lo que hecho hasido copiar ese directorio dentro de/static mostrando así que también muestra esas imágenes (si ya estaban en el directorio media, si no no se muestran porque no se almacenan en el servidor):

Pra esto último, copiamos el direcctorio /media, como he dicho, en el /static y en l settings.py ponemos lo siguiente:


```python
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/static/media/')
```

![](http://i666.photobucket.com/albums/vv21/angelvalera/Seleccioacuten_018_zpscmuobn87.png)