from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_app.serializers import FancyCatSerilizer, FancyCatListSerilizer
from rest_app.models import FancyCat
from rest_app.permissions import AllowGetMethod


class FanctCatListView(APIView):

    permission_classes = (AllowGetMethod, )

    def get(self, request, format=None):
        fancy_cats = FancyCat.objects.all()
        serializer = FancyCatListSerilizer(fancy_cats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FancyCatSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FanctCatDetailView(APIView):

    def get_object(self, pk):
        try:
            return FancyCat.objects.get(id=pk)
        except FancyCat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        serializer = FancyCatSerilizer(fancy_cat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        serializer = FancyCatSerilizer(fancy_cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fancy_cat = self.get_object(pk)
        fancy_cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

