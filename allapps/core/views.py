from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HomeView(APIView):
    def get(self, request):
        return Response(
            {"message": "Hello from Fafadia Tech!"}, status=status.HTTP_200_OK
        )
