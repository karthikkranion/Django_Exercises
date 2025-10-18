from django.shortcuts import redirect, render
from .forms import ProfileForm
from .models import Profile



def home(request):
    candidates = Profile.objects.all()
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            saved_profile = form.save()
            form = ProfileForm(instance=saved_profile)  # bind saved instance
            return redirect('home')  # optional: redirect to avoid resubmission

    return render(request, 'students/home.html', {'form': form, 'candidates': candidates})

def candidate_detail(request, candidate_id):
    candidate = Profile.objects.get(id=candidate_id)
    return render(request, 'students/candidate.html', {'candidate': candidate})