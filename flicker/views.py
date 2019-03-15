import requests
import requests_cache

from django.views.generic import FormView

from .forms import FlickerForm
from .utils import get_flickr_api_url, get_image_urls

requests_cache.install_cache('test_cache', backend='redis', expire_after=300)


class FlickerView(FormView):
    form_class = FlickerForm
    success_url = None
    template_name = 'flicker/index.html'

    def form_valid(self, form):
        response = self.send_query_to_api(form.cleaned_data.get("search", ""))
        image_urls = get_image_urls(response.content.decode("utf-8"))
        context = self.get_context_data(form=form)
        context.update({'image_urls': image_urls})
        return self.render_to_response(context)

    @staticmethod
    def send_query_to_api(query):
        return requests.get(get_flickr_api_url(query))
