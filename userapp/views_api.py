from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
class LoginView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data
            if data.get('email') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(email= data.get('email')).first()
            print(check_user)
            if check_user is None:
                response['message'] = 'Invalid username not found'
                raise Exception('Username not found')

            #if not Profile.objects.filter(user=check_user).first().is_verified:
                #response['message'] = 'Your Profile is  not verified'
                #raise Exception('profile not verified')

            user_obj = authenticate(username = check_user.username, password=data.get('password'))
            print(user_obj)
            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'welcome'
            else:
                response['message'] = 'Invalid Password'
                raise Exception('Invalid password')


        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()


class RegisterView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('email') is None:
                response['message'] = 'key email not found'
                raise Exception('key email not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            if data.get('cfpassword') is None:
                response['message'] = 'key password not found'
                raise Exception('key confirm password not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            if data.get('address') is None:
                response['message'] = 'key address not found'
                raise Exception('key addrwess not found')

            check_user = User.objects.filter(username= data.get('username')).first()
            print(check_user)
            if check_user:
                response['message'] = 'Username already taken'
                raise Exception('Username already taken')


            user_obj= User.objects.create(email = data.get('email'), username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            prof_obj=Profile.objects.create(username=user_obj,password=data.get('password'),cfpassword=data.get('cfpassword'),
                                   email=data.get('email'),address=data.get('address'))
            prof_obj.save()
            #send_mail_to_user(token, data.get('username'))

            response['message'] = 'User Created'
            response['status']  = 200



        except Exception as e:
            print(e)

        return Response(response)


RegisterView = RegisterView.as_view()

