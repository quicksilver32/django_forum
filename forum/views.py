from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime

from .models import Theme, Post, Comment
from .forms import LeaveComm, MyUserCreationForm, ChangeProfile


class ThemeListView(generic.ListView):
    model = Theme
    paginate_by = 20


class ThemeDetailView(generic.DetailView):
    model = Theme


def post(request, pk):
    comms = Comment.objects.filter(post_id=pk)
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = LeaveComm(request.POST)

        if form.is_valid():
            comm = Comment()
            comm.author = request.user
            comm.post_id = pk
            comm.post_time = datetime.datetime.now()
            comm.text = form.cleaned_data['comm']
            comm.save()

        return HttpResponseRedirect('/forum/post/%d' % int(pk))

    else:
        form = LeaveComm()

    return render(request, 'post.html', {'form': form, 'comments': comms, 'post': post})


class PostCreate(generic.edit.CreateView):
    model = Post
    fields = '__all__'


class ThemeCreate(generic.edit.CreateView):
    model = Theme
    fields = '__all__'


class PostDelete(generic.edit.DeleteView):
    model = Post
    success_url = '/'


class ThemeDelete(generic.edit.DeleteView):
    model = Theme
    success_url = '/'


class CommentDelete(generic.edit.DeleteView):
    model = Comment
    success_url = '/'


def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('profile')
    else:
        form = MyUserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    username = request.user
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email

    return render(request, 'profile.html', {'username': username, 'first_name': first_name, 'last_name': last_name,
                                            'email': email})


@login_required
def change_profile(request):
    if request.method == 'POST':
        form = ChangeProfile(request.POST)
        if form.is_valid():
            user = request.user
            if form.cleaned_data['first_name']:
                user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data['last_name']:
                user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['email']:
                user.email = form.cleaned_data['email']
            if form.cleaned_data['password1']:
                user.set_password(form.cleaned_data['password1'])
            user.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('profile')
    else:
        form = ChangeProfile()
    return render(request, 'change_profile.html', {'form': form})
