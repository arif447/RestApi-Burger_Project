from rest_framework.viewsets import ModelViewSet
from BurgerApi.models import UserProfile, Order, CustomerDetail, Ingredient
from BurgerApi.serializer import UserprofileSerializer, OrderSerializer, CustomerSerializer, IngredientSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserProfileViewset(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserprofileSerializer

class OrderViewset(ModelViewSet):
    #queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        #IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset
