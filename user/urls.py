from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    
    # Login, Signup, Chnage_password and generate token url 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here,
    path('change_password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
    # Update user content urls
    path('update_user/', views.updateUserFields.as_view(), name='update_user'),

    # Search User
    path('search_user/',views.searchUserFields.as_view(), name='search_user'),

 ]