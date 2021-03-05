from rest_framework import status
from rest_framework.views import APIView
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.response import Response


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            get_data = Students.objects.get(id=id)
            serializer = StudentsSerializer(get_data)
            return Response(serializer.data)
        get_data = Students.objects.all()
        serializer = StudentsSerializer(get_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serialzer = StudentsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        get_data = Students.objects.get(pk=id)
        serializer = StudentsSerializer(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "full data updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        get_data = Students.objects.get(pk=id)
        serializer = StudentsSerializer(get_data, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial updated successfully"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        get_data = Students.objects.get(pk=id)
        get_data.delete()
        return Response({"msg": "data are delted"})
