from .models import FT_Catalogue
import django_filters

class FtcatFilter(django_filters.FilterSet):
    class Meta:
        model = FT_Catalogue
        #fields = ['id_nr', 'maker', 'instrument', 'transposition', 'total_num_keys', 'wingjoint_num_keys', ]
        fields = ['id_nr', ]
