from django.conf.urls import url

from webservice.views import PostLikeView, PostReportView
from .views import PostListView, SinglePostView, CommentListView, SingleCommentView

# RESTful

url_patterns = [
    url('/post/', PostListView.as_view()),
    url('/post/:post_id', SinglePostView.as_view()),
    url('/post/:post_id/comment/', CommentListView.as_view()),
    url('/post/:post_id/comment/:comment_id', SingleCommentView.as_view()),
    url('/post/:post_id/like/', PostLikeView.as_view()),
    url('/post/:post_id/report/', PostReportView.as_view()),
    # TODO: create views for users
    # url('/user/', v),
    # url('/user/:user_id', v),
    # url('/user/:user_id/follow', v),
    # url('/user/:user_id/block', v),
    # url('/user/:user_id/report', v),
]