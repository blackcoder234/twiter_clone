from django.shortcuts import render


def project_website(request):
    return render(request, "website.html")
