from django.urls import path
from .views import HomeView,ProductListView,CategoryDetailView,ProductAddView,ProductEitView,ProductDeleteView,TemplatesView,RedirectsView

urlpatterns = [
    path('', HomeView.as_view(), name='index' ),
    path('template/', TemplatesView.as_view()),
    path('products', ProductListView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('product/add',ProductAddView.as_view()),
    path('product/edit/<int:pk>',ProductEitView.as_view()),
    path('product/delete/<int:pk>', ProductDeleteView.as_view()),
    path('template/', RedirectsView.as_view(url='/products/')),
]