from django.forms import ValidationError
from django.shortcuts import render
from .forms import UserForm

def index(request):
    return render(request, 'users/index.html')
def user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/success.html')
        else:
            return render(request, 'users/error.html')
    form = UserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

