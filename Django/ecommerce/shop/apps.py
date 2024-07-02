from django.apps import AppConfig

class ShopConfig(AppConfig):
    name = 'shop'

    def ready(self):
        import shop.templatetags.custom_filters
