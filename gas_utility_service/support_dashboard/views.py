from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from service_requests.models import ServiceRequest

@staff_member_required
def dashboard(request):
    all_requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'support_dashboard/dashboard.html', {'all_requests': all_requests})
