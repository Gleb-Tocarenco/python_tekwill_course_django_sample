from django.urls import path
from new_app import views


urlpatterns = [
    path('', views.my_first_view),
    path('date-view/', views.date_view),
    path('days-untill-new-year', views.days_until_new_year),

    
    path('posts/<int:year>/', views.year_view),
    path('posts/2003/', views.special_case_2003),
    path('posts/<int:year>/<int:month>/', views.month_view),
    path('posts/<int:year>/<int:month>/<str:title>/', views.article_detail),

    path('my-cat/', views.cat_image_view),
    path('csv-file/', views.cvs_file_view),
    path('json-file/', views.json_view),
    path('streaming-view/', views.streaming_view)
]
