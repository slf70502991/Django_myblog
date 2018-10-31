from django.db import models
from django.urls import reverse
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value <0 :
        raise models.ValidationError(
            _('Price should not be smaller than 0.'),
            params={'value': value},
        )

class Product(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = '', max_length = 255, null=True, blank = True)
    price = models.IntegerField(validators=[validate_even])
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("product:product-detail", kwargs={"my_id": self.id})


                               