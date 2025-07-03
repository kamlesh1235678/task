
from django.shortcuts import render
from .utils import fetch_flight_data, analyze


def dashboard(request):
    raw_data = fetch_flight_data()
    route_data, price_data = analyze(raw_data)
    return render(request, 'dashboard.html', {
        'route_data': route_data.to_dict(),
        'price_data': price_data.to_dict(),
    })