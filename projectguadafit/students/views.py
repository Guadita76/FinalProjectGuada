
from django.views.generic import TemplateView
from django.shortcuts import render

from typing import Any, Dict

from multiprocessing import context

class StudentView (TemplateView):

    template_name= "/students/index.html"

    def get (self, request, status= None):

        context= {}

        return render (request, self.template_name, context)