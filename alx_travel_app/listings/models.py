from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
        title = models.CharField(max_length=255)
            description = models.TextField()
                location = models.CharField(max_length=100)
                    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
                        is_available = models.BooleanField(default=True)
                            created_at = models.DateTimeField(auto_now_add=True)

                                def __str__(self):
                                            return self.title


                                        class Booking(models.Model):
                                                user = models.ForeignKey(User, on_delete=models.CASCADE)
                                                    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
                                                        start_date = models.DateField()
                                                            end_date = models.DateField()
                                                                booked_at = models.DateTimeField(auto_now_add=True)

                                                                    def __str__(self):
                                                                                return f'{self.user.username} booked {self.listing.title}'


                                                                            class Review(models.Model):
                                                                                    user = models.ForeignKey(User, on_delete=models.CASCADE)
                                                                                        listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
                                                                                            rating = models.PositiveIntegerField()
                                                                                                comment = models.TextField()
                                                                                                    reviewed_at = models.DateTimeField(auto_now_add=True)

                                                                                                        def __str__(self):
                                                                                                                    return f'{self.user.username} reviewed {self.listing.title}'

