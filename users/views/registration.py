from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from ..forms import UserRegisterForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}.')
        return super().form_valid(form)
