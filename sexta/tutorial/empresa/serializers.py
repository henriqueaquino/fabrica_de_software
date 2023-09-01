from rest_framework import serializers
from .models import Pessoa

#class PessoaSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    nome = serializers.CharField(required=False, allow_blank=True, max_length=100)
#   idade = serializers.IntegerField()
#    email = serializers.EmailField()

#    def create(self, validated_data):
#       return Pessoa.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#       instance.nome = validated_data.get('nome', instance.nome)
#       instance.idade = validated_data.get('idade', instance.idade)
#       instance.email = validated_data.get('email', instance.email)
#       instance.save()
#       return instance

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade', 'email']

#class meta é uma classe de configuração dentro da classe