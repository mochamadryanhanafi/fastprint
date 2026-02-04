import requests
from django.core.management.base import BaseCommand
from products.models import Kategori, Status, Produk

class Command(BaseCommand):
    help = 'Fetches and populates data from the API'

    def handle(self, *args, **options):
        username = 'tesprogrammer040226C23'
        password = '4003304cd3cc911ee562a8fb0392390c'
        url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'

        response = requests.post(url, data={'username': username, 'password': password})
        data = response.json().get('data')

        for item in data:
            kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
            status, _ = Status.objects.get_or_create(nama_status=item['status'])

            Produk.objects.update_or_create(
                nama_produk=item['nama_produk'],
                defaults={
                    'harga': item['harga'],
                    'kategori': kategori,
                    'status': status,
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))
