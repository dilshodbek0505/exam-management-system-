from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import LoginSerializer, RegisterSerializer,\
    ForgotPasswordSerializer, ResetPasswordSerializer
from apps.user.tasks import send_verification_code
from apps.user.utils import verification_code

from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()


class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

class LoginApi(GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=200)
    
class ForgotPasswordApi(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = self.request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')

        if cache.get(f'email_{email}'):
            return Response({'code already sent'})
        
        verfiy_code = verification_code()
        cache.set(f'email_{email}', verfiy_code, timeout=60*2)

        send_verification_code.delay(email, verfiy_code)
        
        return Response({'success'}, status=200)

class ResetPasswordApi(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']
        verfiy_code = cache.get(f'email_{email}')

        if code != verfiy_code:
            return Response({'code did not mutch!'}, status=400)
        
        cache.delete(f'email_{email}')

        return Response(serializer.validated_data, status=200)



__all__ = [
    'RegisterApi',
    'LoginApi',
    'ForgotPasswordApi',
    'ResetPasswordApi',
]