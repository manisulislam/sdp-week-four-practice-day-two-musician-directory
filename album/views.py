from django.shortcuts import render, redirect
from album.models import album_model
from album.forms import AlbumForm

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'add_album.html')
            return redirect("home")
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def edit_album(request, album_id):
    album = album_model.objects.get(pk=album_id)
    album_form = AlbumForm(request.POST, instance=album)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form .is_valid():
            album_form .save()
            return redirect("home")
    return render(request, 'add_album.html', {'form': album_form })

def delete_album(request, album_id):
    album = album_model.objects.get(pk=album_id)
    album.delete()
    return redirect("home")