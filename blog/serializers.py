

from rest_framework.serializers import ModelSerializer

from .models import Post


class LocalizedModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        print("instance:", instance)
        data = super().to_representation(instance)
        print('data:', data)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', 'ru')
        for field in self.Meta.translated_fields:
            data[field] = getattr(instance, f"{field}_{lang}")
        data['title'] = f"Title: {data['title'].upper()}"
        return data


class PostSerializer(LocalizedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body',]
        translated_fields = ['title', 'body',]