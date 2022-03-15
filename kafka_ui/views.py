from django.shortcuts import render
import kafka_ui.backend.kafka_client as client

# Create your views here.

def view_landing_page(request):
    topics = client.list_topics()
    return render(request, 'landing_page.html', {'topics': topics})