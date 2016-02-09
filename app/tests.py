#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.test import TestCase
from app.models import Bar, Tapa
from django.core.urlresolvers import reverse

# Create your tests here.


def add_bar(nombre, direccion, visitas=0):
    bar = Bar.objects.get_or_create(nombre=nombre)[0]
    bar.direccion= direccion
    bar.visitas=visitas
    bar.save()
    return bar

def add_tapa(bar, nombre, descripcion, votos=0):
    tapa = Tapa.objects.get_or_create(bar=bar, nombre=nombre)[0]
    tapa.votos=votos
    tapa.descripcion=descripcion
    tapa.save()
    return tapa


class BarMethodTests(TestCase):

    def test_crear_bar(self):
        bar1= add_bar('Plaza','España Orce Plaza Nueva nº 4')
        self.assertEqual(bar1.nombre,'Plaza' )
        print("Test: Creación de un nuevo bar correcta")

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


class TapaMethodTests(TestCase):
    def test_crear_tapa(self):
        bar1= add_bar('Plaza','España Orce Plaza Nueva nº 4')
        t=add_tapa(bar=bar1,nombre="Boquerones",descripcion="Boquerones fritos ricos ricos ")
        self.assertEqual(bar1, t.bar)
        print("Test: Creacion de un nueva tapa Correcta")



class IndexViewTests(TestCase):

    def test_index_view_with_no_bares(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay bares presentes")
        self.assertQuerysetEqual(response.context['bares'], [])
        print("Test:Petición a la portada sin bares Correcta")



    def test_index_view_with_bares(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        bar1= add_bar('tmp','España Orce Plaza Nueva nº 4')
        bar2= add_bar('test','España Orce calle Chorreador nº 6')
        bar3= add_bar('temp','España Orce Fernando villalobos nº 8')
        bar4= add_bar('tmp test temp','España Orce calle Angel nº 2 ')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_bares =len(response.context['bares'])
        self.assertEqual(num_bares , 4)
        print("Test:Petición a la portada con bares Correcta")
