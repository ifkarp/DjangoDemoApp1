from rest_framework import serializers
from codekeeper.models.person import Person
from codekeeper.models.snippet import Snippet


class SnippetPersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet



class PersonSerializer(serializers.HyperlinkedModelSerializer):
    snippets = SnippetPersonSerializer(many=True)
    class Meta:
        model = Person