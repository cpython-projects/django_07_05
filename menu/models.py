from django.db import models


class MenuCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    is_visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=0)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('sort',)
        verbose_name_plural = 'Menu Categories'


class Dish(models.Model):
    title = models.CharField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='dish_photos')
    desc = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=500)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='dishes')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('sort',)
        verbose_name_plural = 'Dishes'
        db_table = 'dishes'



