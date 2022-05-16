from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.pyplot import get

from students.models import Student
from .forms import StudentForms

# Create your views here.

def student_create_view(req):
    form = StudentForms(req.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForms()
    context = {
        'form': form,
    }
    return render(req, 'create.html', context)

def student_list_view(req):
    keyword = req.GET.get('keyword')
    
    if keyword:
        queryset = Student.objects.filter(code__icontains=keyword)
    else:
        queryset = Student.objects.all()
        
    context = {
        'students': queryset,
        'keyword': keyword,
    }
    
    return render(req, 'list.html', context)

def student_detail_view(req, id):
    obj = get_object_or_404(Student, id=id)
    context = {
        'student': obj,
    }
    return render(req, 'detail.html', context)

def student_update_view(req, id):
    queryset = get_object_or_404(Student, id=id)
    form = StudentForms(req.POST or None, instance=queryset)
    
    if req.method == 'POST':
        form.save()
        return redirect('list')
    
    context = {
        'form': form,
    }
    
    return render(req, 'update.html', context)

def student_delete_view(req, id):
    queryset = get_object_or_404(Student, id=id)

    if req.method == 'POST':
        queryset.delete()
        return redirect('list')


    context = {
        'student': queryset
    }

    return render(req, 'delete.html', context)
