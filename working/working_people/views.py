from django.shortcuts import render
from .models import WorkingProfile


def view_working_profile(request):
    all_working_profile = WorkingProfile.objects.all()
    context = {'all_working_profile': all_working_profile}
    return render(request, 'index.html', context)


# def view_working_profile_message(request):
#     context = {'message': 'This is finaly!!!'}
#     return render(request, 'finaly.html', context)

