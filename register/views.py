from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		print(form)
		if form.is_valid():
			print("Saving...")
			form.save()
		return redirect("/")
	else:
		print("whoops")
		form = RegisterForm()
	return render(response, "register/register.html", {"form": form})