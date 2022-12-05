from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddPostForm, UserRegisterForm, UserLoginForm, FormContact
from .models import *
from django.views.generic import ListView, DetailView, CreateView, FormView

from .utils import *


class WomenHome(DataMixin, ListView):
    paginate_by = 3
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        res_con = self.get_user_context(title='Главная')
        return dict(list(context.items()) + list(res_con.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat')


class RegisterUser(DataMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'women/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        res_con = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(res_con.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        res_con = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(res_con.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


# def index(request):
#     posts = Women.objects.all()
#     cats = Categories.objects.all()
#     context = {'menu': menu, 'title': 'Главная', 'posts': posts, 'cats': cats, 'cat_selected': 0}
#     return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        res_con = self.get_user_context(title='Добавление')
        return dict(list(context.items()) + list(res_con.items()))


class ContactView(DataMixin, FormView):
    form_class = FormContact
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        res_con = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(res_con.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')





# def login(request):
#     return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post':post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#     return render(request, 'women/post.html', context=context)

class WomenCategories(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Categories.objects.get(cat__slug=self.kwargs['cat_slug'])
        res_con = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(res_con.items()))


# def show_categories(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     cats = Categories.objects.all()
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'posts': posts, 'cats': cats, 'menu': menu, 'title': 'Отображение по рубрикам', 'cat_selected': cat_id}
#
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request, exeption):
    return HttpResponseNotFound(f'<p>Page not found</p>')
