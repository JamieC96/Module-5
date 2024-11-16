from django.urls import path
from . import views

# configuration of all the urls on the site
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),  
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_project/', views.create_project, name='create_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('inbox/', views.inbox, name='inbox'),
    path('send_message/', views.send_message, name='send_message'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

] 
