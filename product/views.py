from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Product
from .forms import ProductModelForm
# Create your views here.

class ProductListView(ListView):
    template_name = 'product/product_list.html'
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('my_id')
        return get_object_or_404(Product,id=id_)

class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    template_name = 'product/product_create.html'
    form_class = ProductModelForm

    def get_object(self):
        id_ = self.kwargs.get('my_id')
        return get_object_or_404(Product,id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    form_class = ProductModelForm

    def get_object(self):
        id_ = self.kwargs.get('my_id')
        return get_object_or_404(Product,id=id_)
    
    def get_success_url(self):
        return reverse('product:product-list')