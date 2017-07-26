from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User


class FriendManager(models.Manager):
    def addFriend(self, id, user_id):
        f = User.objects.get(id=id)
        u = User.objects.get(id=user_id)
        self.create( user=u, friend=f)
        return self.all()

    def deleteFriend(self, postData):
        pass
        return self.all()


class Friend(models.Model):
    created_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name='user_friends')
    friend = models.ForeignKey(User, related_name='friend_of_user')
    objects = FriendManager()
    
    def __str__(self):
        return self.id + ' - ' + self.name + '(Friend)'
