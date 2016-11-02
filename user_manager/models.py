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

    def save(self, *args, **kwargs):
        if self.who != self.whom:
            super(Follow, self).save(*args, **kwargs)
        else:
            raise ValueError('One cannot follow him/her self')

    class Meta:
        unique_together = ('who', 'whom')
        verbose_name = 'دنبال کردن'
        verbose_name_plural = 'دنبال کردن‌ها'


class Comment(TimeStampedModel):
    commenter = models.ForeignKey(Member, null=False, verbose_name=u'کامنت دهنده')
    media = models.ForeignKey('Media', null=False, verbose_name=u'تصویر')
    comment_text = models.TextField(null=False)

    def __str__(self):
        return '{name} commented {text} on {caption}'.format(
            name=self.commenter.get_full_name(),
            text=self.comment_text,
            caption=self.media.caption
        )



class Like(TimeStampedModel):
    liker = models.ForeignKey(Member, null=False)
    media = models.ForeignKey('Media', null=False)

    def __str__(self):
        return '%s likes %s' % (
            self.liker.get_full_name(),
            self.media.caption
        )

    class Meta:
        unique_together = ('liker', 'media')


class HashTag(models.Model):
    caption = models.CharField(max_length=60, verbose_name='عنوان برچسب')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب‌ها'


class Media(TimeStampedModel):
    uploader = models.ForeignKey(Member, null=False, related_name='posts')
    file = models.FileField(null=False)
    caption = models.TextField()
    hash_tags = models.ManyToManyField(HashTag)
    comments = models.ManyToManyField(Member, through=Comment, related_name='comments')
    likes = models.ManyToManyField(Member, through=Like, related_name='likes')

    def __str__(self):
        return '{caption} by {name}'.format(
            caption=self.caption,
            name=self.uploader.get_full_name()
        )
