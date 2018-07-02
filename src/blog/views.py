from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from blog.models import Article, Category
from django.contrib.auth.mixins import LoginRequiredMixin
# from blog.mixins import SimplePrint
from django.core.mail import send_mail
from django.conf import settings
from blog.forms import ArticleCreateForm, CategoryCreateForm
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as root_login

def article_listview(request):
    template_name = 'article_listview.html'
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def category_listview(request):
    template_name = 'category_listview.html'
    queryset = Category.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def test(request):
    context = {
    }
    return render(request, "test.html", context)

def index(request):
    context = {
    }
    return render(request, "index.html", context)

        # Article
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article_form.html'

# def post_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = ArticleCreateForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return redirect('/details/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = ArticleCreateForm()
#     return render(request, 'name.html', {'form': form})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'article_form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = '/article/'

        # Category
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category_form.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'category_form.html'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = '/category/'

        # Login_Logout
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            root_login(request, user)
            return redirect('/',{'message': "Successfully logged in"})
        else:
            return render(request, 'register.html', {'message': "Something wrong"})
    else:
        return render(request, 'register.html', {'message': ''})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            root_login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'message': "Something wrong"})
    else:
        return render(request, 'login.html', {'message': '...'})

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')