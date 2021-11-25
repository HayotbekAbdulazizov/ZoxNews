from django.urls import path
from .import views

app_name = 'weather'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('details/<slug:slug>', views.PostDetailsView.as_view(), name='post_details'),
    # path('update/<slug:slug>', views.PostUpdateView.as_view(), name='post_update'),
    # path('category/<slug:slug>', views.CategorySortView.as_view(), name='category_sort'),
    # path('addlike/', views.add_to_liked, name='add_to_liked'),
    # path('comment/', views.comment, name='comment'),


]