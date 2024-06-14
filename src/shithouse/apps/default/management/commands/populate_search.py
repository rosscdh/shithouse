import meilisearch
from rest_framework import serializers
from comment.api.serializers import CommentSerializer
from django.core.management.base import BaseCommand, CommandError
from shithouse.apps.agency import models as agency_models
from shithouse.apps.house import models as house_models


class CustomCommentSerializer(CommentSerializer):
    user = serializers.CharField(source='user.username')
    class Meta(CommentSerializer.Meta):
        fields = ["id", "content", "posted", "is_flagged", "user"]


class AgencySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = agency_models.Agency
        fields = ['id', 'name']


class BranchSerializer(serializers.ModelSerializer):
    agency = AgencySerializer()
    address = serializers.CharField()
    class Meta:
        model = agency_models.Branch
        fields = ['id', 'address', 'agency']


class AgentSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    branches = BranchSerializer(many=True)

    class Meta:
        model = agency_models.Agent
        fields = ['id', 'name', 'branches']


class AddressSerializer(serializers.ModelSerializer):
    agents = AgentSerializer(many=True)
    address = serializers.CharField()

    class Meta:
        model = house_models.Address
        fields = ['id', 'address', 'description', 'agents']



class Command(BaseCommand):
    help = "Populate Search"
    client = meilisearch.Client('http://127.0.0.1:7700', 'shithouse123456789')

    def handle(self, *args, **options):
        for serializer in (AddressSerializer, AgentSerializer, BranchSerializer, AgencySerializer, CustomCommentSerializer):
            # if serializer == CommentSerializer:
            #     breakpoint()
            index = self.client.index(serializer.Meta.model.__name__.lower())
            for row in serializer.Meta.model.objects.all():
                try:
                    index.add_documents(serializer(row).data)
                except:
                    breakpoint()
