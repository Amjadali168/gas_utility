from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer  # Assuming user is logged in
            service_request.save()
            return redirect('request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_requests.html', {'requests': requests})

