from bikes.models import Bike, Category
from bikes.serializers import BikeSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters




class PaginationWithCatIndices (LimitOffsetPagination):
    def get_category_indices(self):
        categories = Category.objects.all()
        cat_indices = {}
        for category in categories:
            cat_indices[category.cat] = category.id
        return cat_indices 




    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'cat_indices': self.get_category_indices(),
            'results': data,
        })

def resolve_csvfilter(self, queryset, name, value):
    lookup = {f"{name}__in": value.split(",")}
    queryset = queryset.filter(**lookup)
    return queryset

class BikeFilter(filters.FilterSet):

    cat = filters.CharFilter(method=resolve_csvfilter)

    class Meta:
        model = Bike
        fields = ("cat", "mfg")



class BikeList(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    filterset_class = BikeFilter
    filter_backends = (
        filters.DjangoFilterBackend,
        drf_filters.OrderingFilter,
        drf_filters.SearchFilter,
    )
    pagination_class = PaginationWithCatIndices
    # Request need the following signature ?limit=10&offset=1
    search_fields = ["title", "first_post"]
    ordering_fields = ["post_date", "id"]
    ordering = ["id"]

    def get_queryset(self):
        queryset = Bike.objects.all()
        selected_categories = self.request.query_params.get("cat")
        if selected_categories == "":
            return Bike.objects.none()

        return queryset

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
