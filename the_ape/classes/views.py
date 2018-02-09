from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import UserProfile, ClassMember
from classes.forms import ApeClassRegistrationForm
from classes.models import ApeClass


@login_required
def register_for_class(request, ape_class_id):
    user = request.user
    ape_class = ApeClass.objects.get(id=ape_class_id)
    if request.method == 'GET':
        form = ApeClassRegistrationForm()
        return render(request, 'classes/ape_class_registration.html', {'ape_class': ape_class, 'form': form})

    if request.method == 'POST':
        form = ApeClassRegistrationForm(data=request.POST)
        if form.is_valid():
            profile, created = UserProfile.objects.get_or_create(user=user)
            has_paid = form.cleaned_data['pay_now']
            ClassMember.objects.create(ape_class=ape_class, student=profile, has_paid=has_paid)

    return render(request, 'classes/ape_class.html', {'ape_class': ape_class})
