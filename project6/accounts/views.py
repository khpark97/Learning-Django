from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Save the user first
        response = super().form_valid(form)
        # Get the username and password
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        # Authenticate and login
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response