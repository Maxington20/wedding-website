from django.urls import path,re_path
# Import the views from the site_app
from site_app import views 
from django.urls import reverse_lazy

app_name='site_app'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('guest/list',views.GuestListView.as_view(),name='guest_list'),
    path('guest/new',views.GuestCreateView.as_view(),name='guest_new'),
    re_path(r'^guest/(?P<pk>\d+)/$',views.GuestDetailView.as_view(),name='guest_detail'),
]
