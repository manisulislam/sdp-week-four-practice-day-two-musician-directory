from django.shortcuts import render, redirect
from .forms import musician_form
from .models import musician_model
# Create your views here.
def add_musician(request):
    if request.method=='POST':
        form=musician_form(request.POST)
        if form.is_valid():
            form.save()
            # return render(request,'add_musician.html')
            return redirect("home")
    else:
        form=musician_form()
    return render(request, 'add_musician.html', {'form': form})

def edit_musician(request, musician_id):
    musician = musician_model.objects.get(pk=musician_id)
    music_form = musician_form(request.POST, instance=musician)
    if request.method == 'POST':
        music_form  = musician_form(request.POST, instance=musician)
        if music_form .is_valid():
            music_form .save()
            return redirect("home")
    return render(request, 'add_musician.html', {'form': music_form})