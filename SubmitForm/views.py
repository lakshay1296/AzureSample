# -*- coding: utf-8 -*-

import os
import re
import sys
import pandas as pd
from .models import Vendor as vendor_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django import db

# Set default encoding to 'UTF-8'
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.

def SubmitForm(request):

    context = {
        'response': 'Hello World',
     }


    return render(request, "SubmitForm/submitForm.html", context)

def upload_csv(request):

        context = {}

        if request.method == "GET":
                return render(request, "upload_csv/upload_csv.html", context)

        try:
                csv_file = request.FILES["csv_file"]
                print "File uploaded is named as: ", csv_file
                if not csv_file.name.endswith('.csv'):
                        # messages.error(request,'File is not CSV type')
                        return HttpResponseRedirect(reverse("SubmitForm:upload_csv"))

                csv_data = pd.read_csv(csv_file)

                df = pd.DataFrame(csv_data)  
                print df

                vendor = vendor_model.objects.create(vendorID = "vendor4", firstName="Jhon",
                 lastName="Batista", phoneNumber="984308512", email="jhon.b@test.com")
                db.connections.close_all()

                content = vendor_model.objects.all()

        except Exception as e:
                print e
                content = "fail"

        context = {'content': content,}

        return render(request,'upload_csv/upload_csv.html', context)
