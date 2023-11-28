# views.py in your media_upload app

from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save()  # This assumes UploadFileForm is a ModelForm
            return render(request, 'success.html', {'file': new_file})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
