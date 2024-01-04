from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.

def yangilik_detail(request, slug):
    yangiliklar = get_object_or_404(Yangiliklar, sl_url=slug)
    context = {
        'yangilik': yangiliklar
    }
    return render(request, 'yangilik_detail.html', context)


# def homeView(request):
#     categorys = Category.objects.all()
#     yangiliklar = Yangiliklar.objects.defer("publish_time").all()[:6]
#     mahalliy_one = Yangiliklar.objects.filter(category__nom="Mahalliy").order_by('-publish_time').last()
#     mahalliy_news = Yangiliklar.objects.filter(category__nom="Mahalliy")[:6]
#
#
#     content = {
#         "yangiliklar": yangiliklar,
#         "categorys": categorys,
#         "mahalliy_news": mahalliy_news,
#         "mahalliy_one": mahalliy_one
#     }
#     return render(request, 'index.html',  context=content)

class HomeView(ListView):
    model = Yangiliklar
    template_name = 'index.html'
    context_object_name = "yangiliklar"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content["categorys"] = Category.objects.all()
        content["yangiliklar"] = Yangiliklar.objects.defer("publish_time").all()[:6]
        content["mahalliy_xabarlari"] = Yangiliklar.objects.filter(category__nom="Mahalliy").order_by('-publish_time')
        content["xorij_xabarlari"] = Yangiliklar.objects.filter(category__nom="Xorij").order_by("-publish_time")
        content["sport_xabarlari"] = Yangiliklar.objects.filter(category__nom="Sport").order_by("-publish_time")
        content["texnologiya_xabarlari"] = Yangiliklar.objects.filter(category__nom="Texnologiya").order_by('-publish_time')

        return content



class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()

        content = {
            "form": form
        }
        return render(request, 'contact.html', content)


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur!</h2>")

        content = {
            "form": form
        }
        return render(request, 'contact.html', content)



class MahalliyYangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'local.html'
    context_object_name = "local_yangiliklar"

    def get_queryset(self):
        yangiliklar = Yangiliklar.objects.all().filter(category__nom="Mahalliy").order_by("-publish_time")
        return yangiliklar





class TexnologiyaYangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'technology.html'
    context_object_name = "technology_yangiliklar"

    def get_queryset(self):
        yangiliklar = Yangiliklar.objects.filter(category__nom="Texnologiya")
        return yangiliklar



class SportYangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'sport.html'
    context_object_name = "sport_yangiliklar"

    def get_queryset(self):
        yangiliklar = Yangiliklar.objects.filter(category__nom="Sport")
        return yangiliklar



class XorijYangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'foreign.html'
    context_object_name = "xorij_yangiliklar"

    def get_queryset(self):
        yangiliklar = Yangiliklar.objects.all().filter(category__nom="Xorij").order_by("-publish_time")
        return yangiliklar


class UpdateYangilikNews(UpdateView):
    model = Yangiliklar
    fields = ["sarlavha", "matn", "rasm", "category", "status",]
    template_name = "update.html"
    form_class = YangilikForm



class DeleteYangilikNews(DeleteView):
    model = Yangiliklar
    template_name = 'delete.html'








