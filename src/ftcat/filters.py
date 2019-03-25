from .models import FT_Catalogue
from .models import JointLengths
from .models import ToneholeDistanceAxis
from .models import ToneholeAngleDiamLengthOut, InnerBoreLength,InnerBoreBeginningDiamNotSocket, CompleteOutside, ToneHoleAngleDiamLengthIn, CompleteInside  

import django_filters

class FtcatFilter(django_filters.FilterSet):
    class Meta:
        model = FT_Catalogue
        #fields = ['id_nr', 'maker', 'instrument', 'transposition', 'total_num_keys', 'wingjoint_num_keys', ]
        fields = ['id_nr', ]

class MeasurementsFilter(django_filters.FilterSet):
    class Meta:
        model = FT_Catalogue
        fields = ['id_nr', ]

	# 1: JointLengths
class JointLenFilter(django_filters.FilterSet):
    class Meta:
        model = JointLengths
        fields = ['id_nr', ]

# 2: ToneholeDistanceAxis        
class ToneholeDistanceAxisFilter(django_filters.FilterSet):
    class Meta:
        model = ToneholeDistanceAxis
        fields = ['id_nr', ]

# 3: ToneholeAngleDiamLengthOut
class ToneholeAngDiamLenOutFilter(django_filters.FilterSet):
    class Meta:
        model = ToneholeAngleDiamLengthOut 
        fields = ['id_nr',]

# 4: InnerBoreLength
class InnerBoreLengthFilter(django_filters.FilterSet):
    class Meta:
        model = InnerBoreLength
        fields = ['id_nr',]


# 5: InnerBoreBeginningDiamNotSocket
class InnerBoreBeginningDiamNotSocketFilter(django_filters.FilterSet):
    class Meta:
        model = InnerBoreBeginningDiamNotSocket
        fields = ['id_nr',]


# 6: CompleteOutside
class CompleteOutsideFilter(django_filters.FilterSet):
    class Meta:
        model = CompleteOutside
        fields = ['id_nr',]


# 7: ToneHoleAngleDiamLengthIn
class ToneHoleAngleDiamLengthInFilter(django_filters.FilterSet):
    class Meta:
        model = ToneHoleAngleDiamLengthIn
        fields = ['id_nr',]

# 8: CompleteInside
class CompleteInsideFilter(django_filters.FilterSet):
    class Meta:
        model = CompleteInside
        fields = ['id_nr',]




