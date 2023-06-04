from django.shortcuts import render,get_object_or_404, reverse , redirect
from catalog.models import Product,  Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class ProductListView(ListView):
    """Класс для работы с моделью Продуктов"""
    model = Product
    extra_context = {
        'title': 'Все продукты',
    }

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset =queryset.filter(is_active = True)
        return queryset

class ProductDetailView(DetailView):
    """Класс для получение деталей модели Продуктов"""
    model = Product
    def get_context_data(self,*args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ProductCreateView(CreateView):
    """Класс для создания продуктов Продуктов"""
    model = Product
    fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    """Класс для обновления  Продуктов"""
    model = Product
    fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    """Класс для удаления Продуктов"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')

def toggle_activity(request, pk):
    product_item = get_object_or_404(Product,pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:product_detail',args=[product_item.pk]))


# def home(request):
#
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Главная страница',
#     }
#     # В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
#     # latest_products = Product.objects.order_by('-creation_date')[:5]
#     # for products in latest_products:
#     #     print(products.name)
#
#     return render(request, 'catalog/product_list.html',context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name} with phone {phone} send message: {message}')
    return render(request, 'catalog/contacts.html')

# def product(request, pk=None):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'title': product_item.name,
#         'desc': product_item.description,
#         'category': product_item.category,
#         'price': product_item.unit_price,
#         'create_date': product_item.creation_date,
#         'change_date': product_item.modified_date,
#     }
#     return render(request, 'catalog/product_detail.html', context)