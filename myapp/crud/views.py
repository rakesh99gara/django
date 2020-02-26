from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Student
from .form import StuForm
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'crud/index.html'
    context_object_name = 'students'

    def get_queryset(self):
        """Return the last five published questions."""
        return Student.objects.all()

class ShowView(generic.DetailView):
    model = Student
    template_name = 'crud/show.html'

      
def new(request):  
    stu = StuForm()  
    return render(request,"crud/new.html",{'form':stu})  



# Create your views here.
