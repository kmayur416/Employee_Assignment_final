from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from employeeapi2.serializers import employeeapi2Serializer,PunchInOutSerializer
from employeeapi2.models import Employee,PunchInOut
from rest_framework import status
from django.db.models import Max,Min
from datetime import datetime
# Create your views here.

class ListAPIView(APIView):

    def get(self,request, pk=None, format=None):
        id=pk
        if id is not None:
            queryset = Employee.objects.get(emp_id=pk)
            serializer_class = employeeapi2Serializer(queryset)
            return Response(serializer_class.data)

        queryset = Employee.objects.all()
        serializer_class = employeeapi2Serializer(queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request,format=None):
        serializer_class = employeeapi2Serializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data Created'})
        return Response(serializer_class.errors)

    def put(self,request, pk, format=None):
        id=pk
        queryset = Employee.objects.get(pk=emp_id)
        serializer_class = employeeapi2Serializer(queryset,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data Updated'})
        return response(serializer_class.errors)

    def delete(self,request,pk,format=None):
        id=pk
        queryset = Employee.objects.get(pk=emp_id)
        queryset.delete()
        return Response({'msg':'Data Deleted'})


class InOutview(APIView):

    def get(self,request,format=None):
        id=request.data.get('emp')
        if id is not None:
            queryset=PunchInOut.objects.filter(emp=id)
            serializer_class = PunchInOutSerializer(queryset,many=True)

            return Response(serializer_class.data)
        queryset=PunchInOut.objects.all()
        serializer_class = PunchInOutSerializer(queryset,many=True)
        return Response(serializer_class.data)


    def post(self,request,format=None):
        serializer_class = PunchInOutSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Data Created'})
        return Response(serializer_class.errors)

class displayemp(APIView):

    def get(self,request):
        queryset = Employee.objects.all()

        empinout={}
        FMT = '%H:%M:%S'
        for i in range(1,PunchInOut.objects.values('emp').distinct().count()+1):#aggregate(Max("emp_id"))+1):

            emp_in_time = str(list((PunchInOut.objects.filter(emp_id__exact=i).aggregate(Min('p_in')).values()))[0])
            emp_out_time = str(list((PunchInOut.objects.filter(emp_id__exact=i).aggregate(Max('p_out')).values()))[0])



            tdelta= str(datetime.strptime(emp_out_time, FMT) - datetime.strptime(emp_in_time, FMT))

            empinout[i-1]=(queryset[i-1].fullname,tdelta)

        return Response(empinout)
