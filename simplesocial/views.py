from django.views.generic import TemplateView
import requests
import requests_cache


class HomePage(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     is_cached = ('data' in self.request.session)

    #     if not is_cached:
    #         response = requests.get(
    #             'http://api.ipstack.com/49.36.134.31?access_key=2268e44368de9bd6a6749c84b3a01c4f')
    #         self.request.session['data'] = response.json()

    #     data = self.request.session['data']
    #     context["ip"] = data['ip']
    #     print(is_cached)
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # is_cached = ('aopd_data' in self.request.session)
        requests_cache.install_cache()

        # if not is_cached:
        aopd_url = 'https://api.nasa.gov/planetary/apod?api_key=38BkrjWunel5PtPWfAIOLGhrCo41AYeOUFL14YiY'
        mars_url = 'https://api.nasa.gov/insight_weather/?api_key=38BkrjWunel5PtPWfAIOLGhrCo41AYeOUFL14YiY&feedtype=json&ver=1.0'
        rss_feed_url = 'http://hubblesite.org/api/v3/external_feed/esa_feed'
        news_url = 'http://hubblesite.org/api/v3/news'
        featured_news_url = 'http://hubblesite.org/api/v3/news_release/last'
        aopd_response = requests.get(aopd_url)
        mars_response = requests.get(mars_url)
        news_response = requests.get(news_url)
        featured_response = requests.get(featured_news_url)
            # self.request.session['aopd_data'] = aopd_response.json()
            # self.request.session['mars_data'] = mars_response.json()
            # self.request.session['news_data'] = news_response.json()
            # self.request.session['featured_data'] = featured_response.json()

        # aopd_data = self.request.session['aopd_data']
        # mars_data = self.request.session['mars_data']
        # news_data = self.request.session['news_data']
        # featured_data = self.request.session['featured_data']

        aopd_data = aopd_response.json()
        mars_data = mars_response.json()
        news_data = news_response.json()
        featured_data = featured_response.json()

        context["aopd_data"] = aopd_data
        context["mars_data"] = mars_data
        context["news_data"] = news_data
        context["featured_data"] = featured_data
        print(aopd_response.from_cache)
        return context


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
