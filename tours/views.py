from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.views import View



class MainView(View):
    def get(self, request):
        return render(request, '1.html')


class DepartureView(View):
    def get(self, request, departure):
        return render(request, '2.html')


class TourView(View):
    def get(self, request, id):
        return render(request, '3.html')
