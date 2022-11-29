from django.views.generic import TemplateView


""" View that loads the system home page """
class IndexView(TemplateView):
    # Name of the template associated with this view
    template_name = 'index.html'
    
