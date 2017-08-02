# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song

# def index(request):
    # all_albums = Album.objects.all()
    # context = {
        # 'all_albums':all_albums,
    # }
    # return render(request, 'music/index.html', context)
    
# def detail(request, album_id):
    # album = get_object_or_404(Album, pk=album_id)
    # return render(request, 'music/detail.html', {'album': album})
    
# def favourite(request, album_id):
    # album = get_object_or_404(Album, pk=album_id)
    # try:
        # selected_song = album.song_set.get(pk=request.POST['song'])
    # except(KeyError, Song.DoesNotExist):
        # return render(request, 'music/detail.html', {
            # 'album': album,
            # 'error_message':'Did not select a valid song'
        # })
    # else:
        # selected_song.is_favourite = True
        # selected_song.save()
        # return render(request, 'music/detail.html', {'album': album})

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Album

class IndexView(generic.ListView):
    template_name = "music/index.html"
    
    def get_queryset(self):
        return Album.objects.all()
        
class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"
    
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre', 'logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
    
    #blank form (POST)
    def get(self, request):
        form =  self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    #process form data (POST)
    def post(self, request):
        form =  self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #return user objects if correct credentials
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:
                
                    login(request, user)
                    #request.user.username
                    return redirect('music:index')

        return render(request, self.template_name, {'form':form})
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    


















