from cProfile import label
from django.shortcuts import render
from . import models
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView
from django.urls import reverse, reverse_lazy
from .forms import AccountForm, LoginForm
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

class Index(TemplateView):
    template_name = "blog/index.html"

class SaunaList(ListView): #サウナの投稿を一覧表示するためのビュー
    
    model = models.SaunaImformation
    context_object_name = "sauna_list"
    template_name = "blog/saunalist.html"


class Sauna_form(LoginRequiredMixin,CreateView):#サウナの投稿を作るためのビュー
    
    model = models.SaunaImformation
    fields = ("name","author","created","fee","rouryu","place","FreeText")
    template_name= "blog/sauna_form.html"
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(Sauna_form, self).get_form()
        form.fields['name'].label = 'サウナ名'
        form.fields['author'].label = '投稿者'
        form.fields['created'].label = '投稿日'
        form.fields['fee'].label = '料金'
        form.fields['rouryu'].label = 'ロウリュの有無'
        form.fields['place'].label = '場所、地域'
        form.fields['FreeText'].label = '特徴、感想'
       
        return form

class Sauna_update(UpdateView):
    
    fields = ("name","author","created","fee","rouryu","place","FreeText")
    model = models.SaunaImformation
    template_name = "blog/sauna_form.html"
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
    
    
class Sauna_Detail(DetailView):

    model = models.SaunaImformation
    context_object_name = "sauna"
    template_name = "blog/sauna_detail.html"

class Sauna_delete(DeleteView):
    
    model = models.SaunaImformation
    template_name = "blog/sauna_delete.html"
    success_url = reverse_lazy("list")
    context_object_name = "sauna"

class Signup(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    def get(self, request):
        self.params["account_form"] =AccountForm()
        self.params["AccountCreate"] = False
        return render(request,"blog/signup.html",context=self.params)

    def post(self, request):
        self.params["account_form"] = AccountForm(data=request.POST)

        if self.params["account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()

            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"blog/signup.html",context=self.params)

class MypageView(TemplateView):
    template_name = 'blog/mypage.html'
    
   







