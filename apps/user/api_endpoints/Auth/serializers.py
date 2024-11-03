from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 128)
    password = serializers.CharField(max_length = 128)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username = username)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'user_id': user.id,
                    'refresh': str(refresh),
                    'accesss': str(refresh.access_token)
                }
            
            raise serializers.ValidationError('Password did not mutch')
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('id', 'password')
    
    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
    
        try:
            user = User.objects.get(email = attrs.get('email'))
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')
    

        return super().validate(attrs)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128)
    code = serializers.CharField(max_length = 50)

    def validate(self, attrs):
        password = attrs.get('password')
        email = attrs.get('email')

        try:
            user = User.objects.get(email = email)
            user.set_password(password)
            user.save()
            return {
                'email': email,
                'code': attrs.get('code')
            }
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')
    
