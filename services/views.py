from django.views.generic import ListView
from .models import Services

class ServicesView(ListView):
    model = Services
    template_name = "services/services.html"
    context_object_name = "services"
    paginate_by = 3  

    def get_queryset(self):
        return Services.objects.filter(status=True).order_by("id")  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = context["page_obj"] 
        return context
