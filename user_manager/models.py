from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel


class Member(AbstractUser):
    phone = models.CharField(max_length=15)  # TODO: add validator
    bio = models.TextField(max_length=500)
    profile_picture = models.ImageField()


class Follow(TimeStampedModel):
    who = models.ForeignKey(Member, null=False, related_name='following')
    whom = models.ForeignKey(Member, null=False, related_name='followers')


class Comment(TimeStampedModel):
    commenter = models.ForeignKey(Member, null=False)
    media = models.ForeignKey('Media', null=False)
    comment_text = models.TextField(null=False)


class Like(TimeStampedModel):
    liker = models.ForeignKey(Member, null=False)
    media = models.ForeignKey('Media', null=False)


class HashTag(models.Model):
    caption = models.CharField(max_length=60)


class Media(TimeStampedModel):
    uploader = models.ForeignKey(Member, null=False, related_name='posts')
    file = models.FileField(null=False)
    caption = models.TextField()
    hash_tags = models.ManyToManyField(HashTag)
    comments = models.ManyToManyField(Member, through=Comment, related_name='comments')
    likes = models.ManyToManyField(Member, through=Like, related_name='likes')
