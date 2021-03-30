from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Override the ready method and import the signals module
    # so that update_on_save and update_on_delete will be called
    # after an OrderLineItem model instance is saved or deleted
    def ready(self):
        import checkout.signals
