from django.db.models.query import QuerySet
import meilisearch
from typing import Any
from django.views.generic import TemplateView, ListView
from shithouse.apps.agency import models as agency_models
from shithouse.apps.house import models as house_models


class IndexView(TemplateView):
    template_name = "home.html"


class SearchView(ListView):
    template_name = "search.html"
    model = house_models.Address
    def search(self, query: str) -> dict:
        indexes = (
            "address",
            "agent",
            "agency",
        )
        hits = dict()
        client = meilisearch.Client('http://127.0.0.1:7700', 'shithouse123456789')
        for index_name in indexes:
            index = client.index(index_name)
            hits[index_name] = []
            for row in index.search(query).get("hits"):
                hits[index_name].append(row.get("id"))
        return hits

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        search_matches = dict()
        headings: dict = dict()
        query = self.request.GET.get("q")
        hits: dict = self.search(query=query)
        for key, hits in hits.items():
            if key == "address":
                search_matches[f"{key}_objects"] = house_models.Address.objects.filter(id__in=hits)
            elif key == "agency":
                search_matches[f"{key}_objects"] = agency_models.Agency.objects.filter(id__in=hits)
            elif key == "agent":
                search_matches[f"{key}_objects"] = agency_models.Agent.objects.filter(id__in=hits)

        data = super().get_context_data(**kwargs)
        data.update({
            "object_list": search_matches,
            "query":  query,
        })
        return data