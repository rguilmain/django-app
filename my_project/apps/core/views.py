from django.shortcuts import render
from .forms import TextForm


def index(request):
    form = TextForm()
    context = {"form": form}

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            context["submitted_text"] = form.cleaned_data["text_field"]
        context["form"] = form

    return render(request, "index.html", context)
