from django.shortcuts import render, get_object_or_404

from .models import Project, ProjectImage, AboutServices

def about(request):
	project = Project.objects.all()
	services = AboutServices.objects.all()

	return render(request, 'about/about.html', { 'project' : project, 'services' : services })


def gallery(request, pk):
	gallery = get_object_or_404(ProjectImage, pk=pk) 
	item = gallery.project
	image = item.images.all()

	return render(request, 'about/gallery.html', { 'image' : image })
