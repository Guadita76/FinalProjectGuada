from django.urls import include, path

from projectguadafit.students.views import StudentView
from django.views.generic import TemplateView
from projectguadafit.rutas.views import FormularioView, SearchView

app_name= "rutas"


urlpatterns= [
    
    path("students/", StudentView.as_view(), name= "students_rutas"),
    
    path ("", TemplateView.as_view (template_name= "rutas/index.html"), name= "rutas"),
    
    #path ("template/", TemplateView.as_view(template_name= "rutas/home.html"), name= "template"),
    
    
    path ("formulario/", FormularioView.as_view(), name= "formulario"),
    path ("search/", SearchView.as_view(), name= "search"),
]