from django.conf.urls import url

from webservice.views import PostLikeView, PostReportView
from .views import PostListView, SinglePostView, CommentListView, SingleCommentView

# RESTful

urlpatterns = [
    url('^post/$', PostListView.as_view()),
    url('^post/(?P<post_id>[0-9]+)/$', SinglePostView.as_view()),
    url('^post/(?P<post_id>[0-9]+)/comment/$', CommentListView.as_view()),
    url('^post/(?P<post_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/$', SingleCommentView.as_view()),
    url('^post/(?P<post_id>[0-9]+)/like/$', PostLikeView.as_view()),
    url('^post/(?P<post_id>[0-9]+)/report/$', PostReportView.as_view()),
    # TODO: create views for users
    # url('/user/', v),
    # url('/user/(?P<user_id>[0-9]+)', v),
    # url('/user/(?P<user_id>[0-9]+)/follow', v),
    # url('/user/(?P<user_id>[0-9]+)/block', v),
    # url('/user/(?P<user_id>[0-9]+)/report', v),
]