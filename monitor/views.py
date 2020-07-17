from django.shortcuts import render, redirect
from .forms import RegisterForm
from django import forms
from main.models import Temperature, Humidity
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta

# Create your views here.
def HomeView(response):
    data_temperature = Temperature.objects.all()
    data_humidity = Humidity.objects.all()
    return render(response, "monitor/monitor.html", {"data_humidity":data_humidity})


# class DataList(APIView):
#     """
#     List all datas, or create a new data.
#     """
#     def get(self, request, format=None):
#         # api_key= request.GET['api_key']
#         # device = get_object_or_404(Device, api_key=api_key, enable=True)
#         try:
#             if request.GET['last']:
#                 datas = Data.objects.all()[:1]
#         except:
#             datas = Temperature.objects.all()
#         serializer = DataSerializer(datas, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         try:
#             api_key = request.data['api_key']
#             device = get_object_or_404(Device, api_key=api_key, enable=True)
#             request.data['device'] = device.pk
#             request.data['remote_address'] = ip_address(request)
#             serializer = DataSerializer(data=request.data)
#             debug(serializer)

#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except:
#             msg_err = {'err': 'API KEY not found!'}
#             return Response(msg_err, status=status.HTTP_400_BAD_REQUEST)


# class DataDetail(APIView):
#     """
#     Retrieve, update or delete a datas instance.
#     """

#     def get_object(self, pk):
#         try:
#             return Temperature.objects.get(pk=pk)
#         except Data.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         datas = self.get_object(pk)
#         serializer = DataSerializer(datas)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         datas = self.get_object(pk)
#         serializer = DataSerializer(datas, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         datas = self.get_object(pk)
#         datas.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

