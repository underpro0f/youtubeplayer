from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)
  
    

    #add roomfriend
    @classmethod
    def make_friend(cls,current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    #remove roomfriend
    @classmethod
    def remove_friend(cls,current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

    #your followers
    @classmethod
    def who_added_user(cls, user):
        users = []
        for friend in cls.objects.all():
            if user in friend.users.all():
                users.append(friend.current_user)
        return users




