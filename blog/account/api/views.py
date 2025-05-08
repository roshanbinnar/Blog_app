from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from account.api.serializers import RegistrationSerializer
from account import models

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except AttributeError:
        return Response({'detail': 'User is not authenticated or no token found.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)



@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer =  RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            # For basic token
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)

