from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile


def logout_view(request):
    logout(request)
    JsonResponse({'Response': True})


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import json
@csrf_exempt
def signup(request):
    '''
    Description:
        Funtion used for the signup of the user.

    Resquest param should provioud validated (email, password and name)
    '''
    try:
        params = dict(request.POST)
        print("Here are the params ", params)
        name, email, password = params['name'][0], params['email'][0], params['password'][0]
        user = User.objects.create_user(name, email, password)
        return JsonResponse({'Response': True})
    except Exception as e:
        return JsonResponse({'Response': e})


from django.contrib.auth.models import User


@csrf_exempt
def login_user(request):
    params = dict(request.POST)
    print("\n\n\n", params)
    username = params['username'][0]
    password = params['password'][0]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JsonResponse({'Response': True})
        else:
            return JsonResponse({'Response': False})
            
    else:
        return JsonResponse({'Response': False})
        



# Update Email of the User
class updateEmail(APIView):
    permission_classes = (IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        try: 
            params = dict(request.POST) 
            print("params ",params) 
            user, email = request.user, params['email'][0]
            print(request.user)
            
            user = User.objects.get(username = request.user)
            user.email = email
            user.save()
            return JsonResponse({'response':True})
        except Exception as e:
            return JsonResponse({'Pass parameter (username, newusername  and email) response': e})


'''
Update and write user realated things
'''

def get_profile_instance(user_id):
    user_profile = Profile.objects.filter(user_id = user_id)
    return user_profile


from datetime import datetime
class updateUserFields(APIView):
    permission_classes = (IsAuthenticated,)
    @csrf_exempt
    def post(self, request):
        try: 
            params = dict(request.POST) 
            user_profile = get_profile_instance(request.user.id)

            if 'email' in params:
                user = User.objects.get(username = request.user)
                user.email = params['email'][0]
                user.save()

            if 'birht_date' in params:
                user_profile.update(birth_date = datetime.strptime(params['birht_date'][0], '%Y-%m-%d'))

            if 'genre' in params:
                user_profile.update(genre = params['genre'][0])

            if 'address' in params:
                user_profile.update(genre = params['address'][0])

            if 'postal_code_4' in params:
                user_profile.update(postal_code_4 = params['postal_code_4'][0])

            if 'postal_code_3' in params:
                user_profile.update(postal_code_3 = datetime.strptime(params['postal_code_3'][0], '%Y-%m-%d'))

            if 'locatity' in params:
                user_profile.update(locatity = params['locatity'][0])

            if 'marital_status' in params:
                user_profile.update(marital_status = params['marital_status'][0])

            if 'child_amount' in params:
                user_profile.update(postal_code_4 = params['child_amount'][0])

            if 'postal_code_3' in params:
                user_profile.update(postal_code_3 = params['postal_code_3'][0])

            if 'locatity' in params:
                user_profile.update(locatity = params['locatity'][0])

            if 'marital_status' in params:
                user_profile.update(marital_status = params['marital_status'][0])

            if 'child_amount' in params:
                user_profile.update(postal_code_4 = params['child_amount'][0])


            if 'about_user' in params:
                user_profile.update(about_user = params['about_user'][0])

            if 'locatity' in params:
                user_profile.update(locatity = params['locatity'][0])

            if 'image' in params:
                user_profile.update(image = params['image'][0])

            return JsonResponse({'response':True})
        except Exception as e:
            return JsonResponse({'Pass parameter (username, newusername  and email) response': e})
            

def search(request):

    template_name = 'search.html'

    query = request.GET.get('q', '')
    if query:
        # query example
        results = MyEntity.objects.filter(name__icontains=query).distinct()
    else:
        results = []
    return JsonResponse({'Pass parameter (username, newusername  and email) response': results})




def hello(request):
    return JsonResponse({"response" : "Getting response"})