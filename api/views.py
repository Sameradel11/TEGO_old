from django.shortcuts import render
from .models import CustomUser, Company
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, CompanySerializer
from rest_framework import generics


@api_view(['POST'])
def UserView(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(
            email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        print(user)
        token = Token.objects.create(user=user)
        return Response({'token': token.key,
                         })
    else:
        return Response(serializer.errors)


class CompanyView(generics.ListAPIView, generics.CreateAPIView,
 generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is None:
            return self.list(request, *args, **kwargs)
        else:
            return self.retrieve(request, *args, **kwargs)

    def post(self, request,id=None):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




# class Stakeholders(generics.ListAPIView,generics.CreateAPIView):
#     queryset=Stakeholders.objects.all()
#     serializer_class=StakeholdersSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
