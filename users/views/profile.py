from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import UserUpdateForm, ProfileUpdateForm


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request):
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
        context = {'uform': uform, 'pform': pform}
        return render(request, self.template_name, context)

    def post(self, request):
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Account has been updated.')
            return redirect('profile')
        context = {'uform': uform, 'pform': pform}
        return render(request, self.template_name, context)
