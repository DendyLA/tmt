from django.shortcuts import render, get_object_or_404

from .models import Project, ProjectImage, AboutServices, Statistic

def about(request):
	project = Project.objects.all()
	services = AboutServices.objects.all()

	return render(request, 'about/about.html', { 'project' : project, 'services' : services })


def gallery(request, pk):
	project = get_object_or_404(Project, pk=pk) 
	image = project.images.all()
	statistic = Statistic.objects.all()

	return render(request, 'about/gallery.html', { 'image' : image , 'project' : project, 'statistic' : statistic})
