from django.shortcuts import render

from .models import Place

# Create your views here.
def index(request):
	"""The home page for outdoorx"""
	return render(request, 'master/index.html')

def place(request):
	"""Show all place."""
	place = Topic.objects.filter(owner=request.user).order_by('date_added')
	place = Topic.objects.order_by('date_added')
	context = {'place': place}
	return render(request, 'master/place.html', context)