from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid4
import os

class Bar(models.Model):
    nombre = models.CharField(max_length=128, primary_key=True, unique=True)
    direccion= models.CharField(max_length=128, unique=True)
    visitas= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bar, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre


class Tapa(models.Model):

    bar = models.ForeignKey(Bar)
    nombre = models.CharField(max_length=128)
    votos = models.IntegerField(default=0)
    descripcion= models.CharField(max_length=500)
    slug = models.SlugField()


    def generar_ruta_imagen(instance, filename):
        print "Entra en generar ruta"
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo
        ruta = os.path.join('bar',instance.bar.slug )

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(uuid4().hex, extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)

    print generar_ruta_imagen

    picture = models.ImageField(upload_to=generar_ruta_imagen, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Tapa, self).save(*args, **kwargs)


    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre
