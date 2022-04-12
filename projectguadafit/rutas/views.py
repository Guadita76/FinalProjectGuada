from django.views.generic import TemplateView

from django.shortcuts import render
from projectguadafit.students.models import studentsdata, personaldata, additionaldata

from .forms import *


class FormularioView (TemplateView):
    
    template_name= 'forms/index.html'
    
    def get (self, request):
        
        context = { 'forms': StudentsForms(),
                  
                  }
    
        return render (request, self.template_name, context)  
         
         
    def post(self, request):
        
        
        
        response=  StudentsForms(request.POST)
        
        if response.is_valid:
           
           
          print (response) 
          obj_response= response.cleaned_data
        
        
          name= obj_response ['name']
          last_name= obj_response ['last_name']
          address= obj_response ['address']
         
          print(f'Nombre: {name}')
          print(f'Apellido: {last_name}')
          
          obj_student= studentsdata (name=obj_response.get ('name'), last_name= obj_response.get ('last_name'), address=obj_response.get ('address' ))
          obj_student.save()
          
          context ={ 'forms': StudentsForms(),
                    }
            
          return render (request, self.template_name, context)        
                  
    
    
    

    
    # def get (self, request):
        
    #     context = { 'forms1': PersonalDataForms(),
                  
    #              }
    
    #     return render (request, self.template_name, context)  
    
    
   
           
    # def post(self, request):
        
        
        
    #     response1=  PersonalDataForms(request.POST)
        
    #     if response1.is_valid:
    #       obj_response1= response1.cleaned_data
        
        
    #       age= obj_response1 ['age']
    #       height= obj_response1 ['height']
    #       weight= obj_response1 ['eight']
    #       preexisting_condition= obj_response1 ['preexisting_condition']
         
    #       objeto_personal_data= personaldata (age=obj_response1.get ('age'), height=obj_response1.get ('height'), weight= obj_response1.get ('weight') , preexisting_condition= obj_response1.get ('preexisting_condition')) 
    #       objeto_personal_data.save()
          
    #       context ={ 'forms1': PersonalDataForms(),
    #                 }
            
    #     return render (request, self.template_name, context)     
    
    
    
    #def get (self, request):
        
    #     context = {
                  
    #               'forms2': AdditionalDataForms()
                  
    #              }
    
    #     return render (request, self.template_name, context) 
       
       
       
    # def post(self, request):
        
        
    #     response= AdditionalDataForms (request.POST)
        
    #     if response.is_valid:
    #        obj_response= response.cleaned_data
        
        
    #        extra_activities= obj_response ['extra_activities']
    #        training_style= obj_response ['training_style']
    #        proposed_objectives= obj_response ['proposed_objectives']
         
    #        objeto_extra_data= additionaldata (extra_activities= obj_response.get ('extra_activities'), training_style=obj_response.get ('training_style'), proposed_objectives=obj_response.get ('proposed_objectives'))
        
    #        objeto_extra_data.save()
          
    #        context ={ 'forms2': AdditionalDataForms(),
    #                 }
            
    #        return render (request, self.template_name, context)     
                     
        
        
class SearchView (TemplateView):
    
    template_name= 'forms/search.html'     
        
    def post (self, request):
         
        context= {'elements': studentsdata.objects.filter(name= request.POST.get('name')), 
                                                          
                  
                  }
         
        return render (request, self.template_name, context)   
        
        
        
        
       
    
      