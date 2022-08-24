import random
from unittest import result
from .models import UserLog
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import views, response, generics, status
from rest_framework.utils import json
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

def send_otp(phone, otp):
    pass
    

class SignInUp(generics.ListAPIView):
    permission_classes = []

    def post(self, request):
        result = {}

        try:
            data = json.loads(request.body)

            if 'phone' not in data or data['phone'] =='':
                result['message'] = "You have to give phone number"
                result['error'] = "phone"
                return response.Response(result, status=status.HTTP_400_BAD_REQUEST)

            generated_otp = str(random.randint(1000, 9999))

            try:
                phone_number = UserLog.objects.get(phone=data['phone'])
                user = UserLog.objects.filter(phone=phone_number).first()
                user.otp = generated_otp
                result = {
                    "status": status.HTTP_200_OK,
                    'message': 'success',
                    'user': user.phone,
                    'reotp': user.otp,
                }
                user.save()
                return response.Response(result)

            except ObjectDoesNotExist:
                user = UserLog()
                user.phone = data['phone']
                user.otp = generated_otp
                user.save()
                send_otp(user.phone, user.otp)
                result = {
                    "status": status.HTTP_200_OK,
                    'message': 'success',
                    'phone': user.phone,
                    'otp': user.otp
                }
                return response.Response(result)

        except Exception as e:
            result["status"] = status.HTTP_400_BAD_REQUEST
            result['message'] = str(e)
            return response.Response(result)


class CheckOtp(generics.ListAPIView):
    permission_classes = []

    def put(self, request):
        result = {}

        try:
            data = json.loads(request.body)
            if 'phone' not in data or data['phone'] == '':
                result["message"] = 'Phone can not be null'
                result['error'] = 'Phone'
                return response.Response(result, status=status.HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp'] == '':
                result["message"] = 'please provide otp'
                result['error'] = 'otp'
                return response.Response(result, status=status.HTTP_400_BAD_REQUEST)

            else:
                user = UserLog.objects.filter(phone=data['phone']).first()
                if user.otp == data['otp']:
                    user.isVarified = True
                    user.otp = ' '
                    user.save()
                    token = RefreshToken.for_user(user)
                    result = {
                        'access': str(token.access_token),
                        'token': str(token),
                        'message': 'success',
                        'status': status.HTTP_200_OK
                    }
                    return response.Response(result)
                
                else:
                    result ={
                        'message': 'OTP did not match',
                        'status': status.HTTP_400_BAD_REQUEST,
                        'error': 'otp'
                    }
                    return response.Response(result)

        except Exception as e:
            result['message'] = str(e)
            return response.Response(result)

