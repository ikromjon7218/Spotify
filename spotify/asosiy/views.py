from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters

from .serializers import *
from .models import *

class QoshiqchiViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    def get_queryset(self):
        soz = self.request.query_params.get("qidirish")
        if soz is None or soz == "":
            natija = Qoshiqchi.objects.all()
        else:
            natija = Qoshiqchi.objects.filter(ism__contains=soz)
        return natija

    @action(detail=True, methods=["GET", "POST"])
    def albomlar(self, request, pk):
        if request.method == "POST":
            serializer = AlbomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(qoshiqchi=Qoshiqchi.objects.get(id=pk))
                return Response(serializer.data)

        albums = Albom.objects.filter(qoshiqchi=Qoshiqchi.objects.get(id=pk))
        serializer = AlbomSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        qoshiqchi = request.data
        serializer = QoshiqchiSerializer(data=qoshiqchi)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        qoshiqchilar = Qoshiq.objects.all()
        serializer = QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

class AlbomViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True, methods=["GET", "POST"])
    def qoshiqchi(self, request, pk):
        if request.method == "POST":
            serializer = QoshiqchiSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        qoshiqchis = Albom.objects.get(id=pk).qoshiqchi
        serializer = QoshiqchiSerializer(qoshiqchis)
        return Response(serializer.data)

    def qoshiq(self, request, pk):
        if request.method == "POST":
            serializer = QoshiqSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        qoshiqs = Qoshiq.objects.filter(albom=Albom.objects.get(id=pk))
        serializer = QoshiqSerializer(qoshiqs, many=True)
        return Response(serializer.data)

    def post(self, request):
        albom = request.data
        serializer = AlbomSerializer(data=albom)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        albomlar = Albom.objects.all()
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)


class QoshiqViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer

class QoshiqchiDetailAPIView(APIView):
    def get(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi)
        return Response(serializer.data)

    def put(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
        if serializer.is_valid():
            qoshiqchi.ism = serializer.validated_data.get('ism')
            qoshiqchi.tugilgan_yil = serializer.validated_data.get('tugilgan_yil')
            qoshiqchi.davlat = serializer.validated_data.get('davlat')
            qoshiqchi.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        qoshiqchi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class QoshiqlarAPIView(APIView):
#     def get(self, request):
#         qoshiqlar = Qoshiq.objects.all()
#         serializer = QoshiqSerializer(qoshiqlar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         qoshiq = request.data
#         serializer = QoshiqSerializer(data=qoshiq)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class AlbomlarAPIView(APIView):
#     def get(self, request):
#         albomlar = Albom.objects.all()
#         serializer = AlbomSerializer(albomlar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         albom = request.data
#         serializer = AlbomSerializer(data=albom)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class AlbomViewSet(ModelViewSet):
#     queryset = Albom.objects.all()
#     serializer_class = AlbomSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ("nom", "qoshiqchi__ism")
#     ordering_filds = "nom", "sana"
