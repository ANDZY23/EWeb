from django.shortcuts import render, redirect
import csv
from .forms import *
from .models import *
from .forms import UploadCSVForm
from django.utils import timezone
from django.db.models import F
import json


def dashboard(request):
    return render(request, 'display/display.html')

def import_data(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:

                Data.objects.create(
                    room_name_id=row.get('room_name_id'),
                    label=row.get('label'),
                    value=row.get('value'),
                    timestamp=row.get('timestamp'),
                )
            return redirect('import_data')
    else:
        form = UploadCSVForm()

    return render(request, 'display/import_data.html', {'form': form})

