from django.apps import AppConfig


class BookReviewAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_review_app'

    def ready(self):
        import book_review_app.signals

