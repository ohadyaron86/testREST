from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializer import RegisterSerializer


# Register API
class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        user = super().post(request, *args, **kwargs)
        return Response({
            "user": RegisterSerializer(user.data, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
