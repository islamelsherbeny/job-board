import django_filters
from .models import Job
#this is 
class JobFilter(django_filters.FilterSet):
    #this is to search for a certain word in the phrase 
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner','published_at','image','sallary','vacuncy','slug']