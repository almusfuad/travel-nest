from django.urls import path, include
from . import views

urlpatterns = [
      path('locations/', views.LocationListView.as_view(), name = 'location-list'),
      path('list/', views.DormitoryListView.as_view(), name = 'dormitory-list'),
      path('list/<int:id>/', views.DormitoryDetailsView.as_view(), name = 'dormitory-details'),
      path('<int:id>/reviews/', views.DormitoryReviewListView.as_view(), name = 'dormitory_reviews'),
      path('<int:id>/reviews/create/', views.DormitoryReviewCreateView.as_view(), name = 'create_review'),
      path('reviews/<int:id>/update/', views.DormitoryReviewUpdateView.as_view(), name = 'update_review'),
]