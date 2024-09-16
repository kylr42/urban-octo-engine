from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_deleted", "created_at", "updated_at"]
    list_filter = ["is_deleted"]
    search_fields = ["name", "description"]
    readonly_fields = ["created_at", "updated_at", "is_deleted"]
    fieldsets = [
        (None, {"fields": ["name", "description", "price"]}),
        ("Meta", {"fields": ["is_deleted", "created_at", "updated_at"], "classes": ["collapse"]}),
    ]
    actions = ["delete_model"]

    def delete_model(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, "Удалено успешно")

    delete_model.short_description = "Удалить выбранные товары (мягко)"
