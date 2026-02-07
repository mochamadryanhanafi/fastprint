from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produk, Kategori, Status
from .serializers import ProdukSerializer, ProdukFormSerializer

class ProductListView(APIView):
    def get(self, request):
        status = Status.objects.filter(nama_status='bisa dijual').first()
        if status:
            products = Produk.objects.filter(status=status)
        else:
            products = Produk.objects.none()
        serializer = ProdukSerializer(products, many=True)
        return Response(serializer.data)

class ProductView(View):
    def get(self, request):
        return render(request, 'products/product_list.html')

class ProductCreateView(View):
    def get(self, request):
        form = ProdukFormSerializer()
        kategori = Kategori.objects.all()
        status = Status.objects.all()
        return render(request, 'products/product_form.html', {'form': form, 'kategori': kategori, 'status': status})

    def post(self, request):
        serializer = ProdukFormSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('/products/?success=created')
        kategori = Kategori.objects.all()
        status = Status.objects.all()
        return render(request, 'products/product_form.html', {'form': serializer, 'kategori': kategori, 'status': status})

class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Produk, pk=pk)
        form = ProdukFormSerializer(instance=product)
        kategori = Kategori.objects.all()
        status = Status.objects.all()
        return render(request, 'products/product_form.html', {'form': form, 'kategori': kategori, 'status': status})

    def post(self, request, pk):
        product = get_object_or_404(Produk, pk=pk)
        serializer = ProdukFormSerializer(instance=product, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('/products/?success=updated')
        kategori = Kategori.objects.all()
        status = Status.objects.all()
        return render(request, 'products/product_form.html', {'form': serializer, 'kategori': kategori, 'status': status})

class ProductDeleteView(View):
    def post(self, request, pk):
        product = get_object_or_404(Produk, pk=pk)
        product.delete()
        return redirect('product_list')