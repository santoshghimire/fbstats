from django.views.generic import View
from django.shortcuts import render
from newspaper import Article


class NewsParser(View):
    """Module for previewing data from facebook."""
    template_name = 'news_parser.html'

    def get(self, request, *args, **kwargs):
        context = {"method": "get"}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        url = request.POST.get("url")
        context = {}
        a = Article(url, language='en')
        a.download()
        a.parse()
        context["title"] = a.title
        context["text"] = a.text
        context["authors"] = ", ".join(a.authors)
        context["top_image"] = a.top_image
        a.fetch_images()
        context["images"] = a.images
        context["publish_date"] = a.publish_date
        context["movies"] = a.movies
        a.nlp()
        context["keywords"] = ", ".join(a.keywords)
        context["summary"] = a.summary
        context["url"] = url
        context["method"] = "post"
        return render(request, self.template_name, context)
