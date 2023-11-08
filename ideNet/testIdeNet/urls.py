from django.urls import path
from testIdeNet import views
from django.contrib import admin

admin.site.site_header = "IDE-NET"
admin.site.site_title = "IDE-NET"
admin.site.index_title = 'Administration'

urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.AccountLoginView.as_view(), name='account_login'),
    

]