from rest_framework import serializers
from .models import User,Task, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)#nesting tags
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many = True,
        write_only = True
    )
    class Meta:
        model = Task
        fields = '__all__'

    def create(self,validated_data):
        #extract the ids from validated data
        tags_ids = validated_data.pop('tags_ids',[])
        #create the tasks
        task = Task.objects.create(**validated_data)
        #assign tag to tasks 
        task.tags.set(tags_ids)
        return task
    def update(self,instance,validated_data):
        tags_ids = validated_data.pop('tags_ids',None)
        #update the task field
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        #if tags ids were not provided
        if tags_ids is not None:
            instance.tags.set(tags_ids)
        return instance


class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True,read_only = True)
    class Meta:
        model = User
        fields = '__all__'