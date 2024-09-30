

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PreTaskFormModelForm

def submit_form(request):
    if request.method == 'POST':
        form = PreTaskFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PreTaskFormModelForm()
    return render(request, 'submit_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
