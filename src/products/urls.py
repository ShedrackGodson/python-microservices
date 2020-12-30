from .views import ProductViewSet, UserAPIView
from django.urls import path

urlpatterns = [
    path("products/", ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path("products/<str:pk>/", ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path("user/", UserAPIView.as_view())
]
