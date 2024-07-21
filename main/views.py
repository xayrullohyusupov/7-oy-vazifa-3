from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView,RedirectView
from .models import Product,Category,Productimg



class HomeView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        return render(request, 'index.html',context={})


class ProductListView(ListView):
    model = Product
    # queryset = Product.objects.filter(status=True)
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 30


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        data['Productimg'] = Productimg.objects.all()
        return data

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'product_detail.html'

class ProductAddView(CreateView):
    model = Product
    template_name = 'product_add.html'
    fields = ['name', 'quantity', 'price','category']
    success_url = '/'

class ProductEitView(UpdateView):
    model = Product
    template_name = 'product_add.html'
    fields = ['name', 'quantity', 'price','category']
    success_url = '/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    fields = '__all__'
    success_url = '/'


class TemplatesView(TemplateView):
    template_name = 'index.html'



class RedirectsView(RedirectView):
    url = '/products/'


