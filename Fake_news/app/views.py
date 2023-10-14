from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import FakeNews_Serializer
from rest_framework.response import Response 
from .models import FakeNews_model

#import sklearn

import joblib
import pandas as pd

# Create your views here.


class FakeNews_view(APIView):
     


    def get(self, request):
        FN_model=FakeNews_model.objects.all()
        FN=FakeNews_Serializer(FN_model,many=True)
        return Response(FN.data)
    
    def post(self, request):
        filename="D:/ai practice/fake_news/jupeyter/model_gession.joblib"
        guession_model= joblib.load(filename)
        preprocessor_=joblib.load("D:/ai practice/fake_news/jupeyter/preprocessor.joblib")




        FN_ser=FakeNews_Serializer(data=request.data)

        if FN_ser.is_valid():
           
            transform=preprocessor_.transform(pd.DataFrame(FN_ser.data,index=[0]))
            
            pre=guession_model.predict(transform)
            
            
            return Response({'fake(0)/true(1)': pre})
        return Response({'success': False})