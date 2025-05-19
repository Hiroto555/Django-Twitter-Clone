from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class UserSearchView(LoginRequiredMixin, View):
    template_name = 'users/search_result.html'

    def post(self, request):
        query = request.POST.get('search')
        results = User.objects.filter(username__contains=query)
        return render(request, self.template_name, {'results': results})

    def get(self, request):
        return redirect('blog-home')
