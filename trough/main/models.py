from django.db import models

from trough.ratings.models import RatingCategory


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'


class Amount(models.Model):
    GRAM = 0
    PIECES = 1
    TEA_SPOON = 2
    TABLE_SPOON = 3
    GLASS = 4
    PINCH = 5

    UNITS_CHOICES = (
        (GRAM, 'Gram'),
        (PIECES, 'Pieces'),
        (TEA_SPOON, 'Tea spoon'),
        (TABLE_SPOON, 'Table spoon'),
        (GLASS, 'Glass'),
        (PINCH, 'Pinch'),
    )
    value = models.IntegerField(null=True)
    units = models.IntegerField(null=True, choices=UNITS_CHOICES, default=GRAM)

    def __str__(self):
        return f'{self.value} {self.get_units_display()}(s)'


class Dish(models.Model):
    name = models.CharField(max_length=255, blank=False)
    rating_categories = models.ManyToManyField(RatingCategory)

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    amount = models.ForeignKey(Amount, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (f'amount: {self.amount.value} '
                f'{self.amount.get_units_display()},'
                f'product: {self.product.name}')
