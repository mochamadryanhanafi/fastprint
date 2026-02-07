from django.core.management.base import BaseCommand
from products.services import ProductService

class Command(BaseCommand):
    help = 'Fetches and populates data from the API'

    def handle(self, *args, **options):
        success, message = ProductService.sync_products()
        if success:
            self.stdout.write(self.style.SUCCESS(message))
        else:
            self.stdout.write(self.style.ERROR(message))
