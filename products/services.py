import requests
import hashlib
from datetime import datetime
from django.conf import settings
from .models import Kategori, Status, Produk

class ProductService:
    @staticmethod
    def sync_products():
        now = datetime.now()
        utc_hour = int(now.strftime('%H'))
        local_hour = (utc_hour + 7) % 24
        
        day = now.strftime('%d')
        month = now.strftime('%m')
        year_short = now.strftime('%y')

        username = f"tesprogrammer{day}{month}{year_short}C{local_hour:02d}"
        password_source = f"bisacoding-{day}-{month}-{year_short}"
        password = hashlib.md5(password_source.encode()).hexdigest()
        
        url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'

        try:
            response = requests.post(url, data={'username': username, 'password': password})
            data = response.json().get('data')

            if not data:
                return False, "No data received"

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
            return True, "Success"
            
        except Exception as e:
            return False, str(e)
