from django.urls import path,include
from . import views


urlpatterns = [	
	path('api/',views.PostViews.as_view(),name='posts'),
	path('post/<int:pk>/', views.postDetail.as_view()),    
    
]