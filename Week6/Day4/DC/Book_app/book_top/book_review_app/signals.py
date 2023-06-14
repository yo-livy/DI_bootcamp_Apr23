from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookReview
from django.db import models



@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, created, **kwargs):
    if created or instance.rating != instance.book.average_rating:
        # Calculate the new average rating for the book
        reviews = instance.book.bookreview_set.all()
        rating_sum = reviews.aggregate(total_rating=models.Sum('rating'))['total_rating']
        review_count = reviews.count()
        new_average_rating = rating_sum / review_count

        # Update the book's average rating
        instance.book.average_rating = new_average_rating
        instance.book.save()