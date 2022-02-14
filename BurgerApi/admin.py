from django.contrib import admin
from BurgerApi.models import UserProfile, Order, CustomerDetail, Ingredient

class UserprofileAdmin(admin.ModelAdmin):

    list_display = ['email']

    class Meta:
        model = UserProfile

class IngredientAdmin(admin.ModelAdmin):

    list_display = ['salad', 'cheese', 'meat']

    class Meta:
        model = Ingredient

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['delivery_address', 'payment_type', 'phone']

    class Meta:
        model = CustomerDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ingredients', 'customer', 'price', 'order_time']

    class Meta:
        model = Order

# Register your models here.
admin.site.register(UserProfile, UserprofileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(CustomerDetail, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
