import uuid
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, verbose_name="UUID")

    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")

    is_deleted = models.BooleanField(default=False, verbose_name="Удален")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["is_deleted"]),
        ]

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
        return True


