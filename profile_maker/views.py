from django.shortcuts import render
from .forms import UserProfileForm
from .models import Profile_User

# Create your views here.

IMAGE_FILES_TYPES = ['png','jpg','jpeg']


def create_profile(request):
    form = UserProfileForm()
    if request.method == "POST":
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILES_TYPES:
                return render(request,'error.html')
            user_pr.save()
            return render(request,'user_details.html',{'user_pr':user_pr})
    context = {'form':form}
    return render(request,'profile_create.html',context)

            