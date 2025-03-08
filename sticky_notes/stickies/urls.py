from django.urls import path
from . import views

# URL pattern for the root/home page
# views.get_all - function that handles displaying all sticky notes
# 'sticky_list' - name used to reference this URL in templates/views
urlpatterns = [
    path('', views.get_all, name='sticky_list'),
    path('<int:pk>/', views.get, name='sticky_view'),
    path('new/', views.create, name='create_sticky'),
    path('<int:pk>/edit/', views.update, name='edit_sticky'),
    path('<int:pk>/delete/', views.delete, name='delete_sticky'),
]
