from django.shortcuts import render


def admin_dashboard_view(request):
    return render(request, "crm/admin_dashboard.html", {})


def add_pet_view(request):
    return render(request, "crm/add_pet.html")
