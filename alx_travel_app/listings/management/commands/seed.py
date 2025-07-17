from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
        help = 'Seed the database with sample listings'

            def handle(self, *args, **kwargs):
                        Listing.objects.all().delete()
                                locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Naivasha']
                                        for i in range(10):
                                                        Listing.objects.create(
                                                                                title=f'Listing {i+1}',
                                                                                                description=f'Description for listing {i+1}',
                                                                                                                location=random.choice(locations),
                                                                                                                                price_per_night=random.uniform(50, 300),
                                                                                                                                                is_available=True
                                                                                                                                                            )
                                                                self.stdout.write(self.style.SUCCESS('✅ Database seeded with sample listings.'))

