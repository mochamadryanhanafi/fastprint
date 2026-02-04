from rest_framework import serializers
from .models import Produk, Kategori, Status

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.CharField(source='kategori.nama_kategori')
    status = serializers.CharField(source='status.nama_status')

    class Meta:
        model = Produk
        fields = ('id_produk', 'nama_produk', 'harga', 'kategori', 'status')

class ProdukFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ('nama_produk', 'harga', 'kategori', 'status')

    def validate_nama_produk(self, value):
        if not value:
            raise serializers.ValidationError("Nama produk tidak boleh kosong.")
        return value

    def validate_harga(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Harga harus berupa angka.")
        return value
