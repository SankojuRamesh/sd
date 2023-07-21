from django.shortcuts import render
from rest_framework import generics, parsers, permissions, renderers, viewsets, views
from rest_framework import serializers, response
from django.conf import settings
# Create your views here.

 


class MenuView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
      
    def get(self, request):
        role = request.GET.get('role', '')
        rolse_menu ={"Superadmin":[{"title":'Company Manager', "links": [{"menu": "Company List", "rout":   settings.BASE_URL+"company"}]},
                {"title":'settings', "link": [{"menu": "Company List", "rout":    settings.BASE_URL+"settings"}]}],
             "Admin":[{"title":'Employee Manager', "links": [{"menu": "employee List", "rout":    settings.BASE_URL+"employee"},{"menu": "New Employee", "rout":    settings.BASE_URL+"newemployee"}]},

              {"title":'Atandence Manager', "links": [{"menu": "attendence List", "rout":   settings.BASE_URL+"attendence"}]}] }
       
        return response.Response(rolse_menu.get(role, {}))
    
    
    