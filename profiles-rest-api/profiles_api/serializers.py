from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    # define a meta class that configure the serializer to point to a specific model (UserProfile model)using model serializer
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # here we need to set an exception for password field because
        #we only wanna use this when creating new user + no retrieving(write only)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        # only field that is writable is status_text
        # read only: id, user_profile, created_on
        extra_kwargs = {'user_profile': {'read_only':True}}
