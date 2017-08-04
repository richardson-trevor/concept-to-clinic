from rest_framework import serializers

from backend.cases.models import (
    Case,
    Candidate,
    Nodule,
)
from backend.images.models import (
    ImageSeries,
    ImageLocation
)


class ImageSeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageSeries
        fields = '__all__'


class ImageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLocation
        fields = '__all__'


class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'
        read_only_fields = ('created',)

    series = ImageSeriesSerializer()


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        read_only_fields = ('created',)

    centroid = ImageLocationSerializer()


class NoduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nodule
        fields = '__all__'
        read_only_fields = ('created',)

    centroid = ImageLocationSerializer()
