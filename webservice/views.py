from django.http import JsonResponse
from django.views.generic import View


class PostListView(View):
    def get(self, request):
        """
        Get all photo/videos (Timeline)
        :param request:
        :return:
        """
        pass

    def post(self, request):
        """
        Upload a new photo/video
        :param request:
        :return:
        """
        pass

class SinglePostView(View):
    def get(self, request, post_id):
        """
        Show post details
        :param request:
        :param post_id:
        :return:
        """
        pass

    def post(self, request, post_id):
        """
        Edit post details
        :param request:
        :param post_id:
        :return:
        """
        pass

    def delete(self, request, post_id):
        """
        Remove post
        :param request:
        :param post_id:
        :return:
        """
        pass


class CommentListView(View):
    def get(self, request, post_id):
        """
        Get a post's comments
        :param request:
        :param post_id:
        :return:
        """
        pass

    def post(self, request, post_id):
        """
        Add a new comment under the post
        :param request:
        :param post_id:
        :return:
        """
        pass


class SingleCommentView(View):
    def get(self, request, post_id, comment_id):
        """
        Get a comment detail
        :param request:
        :param post_id:
        :param comment_id:
        :return:
        """
        pass


    def post(self, request, post_id, comment_id):
        """
        Edit a comment
        :param request:
        :param post_id:
        :param comment_id:
        :return:
        """
        pass


    def delete(self, request, post_id, comment_id):
        """
        Remove a comment
        :param request:
        :param post_id:
        :param comment_id:
        :return:
        """
        pass

class PostLikeView(View):
    def post(self, request, post_id):
        """
        Like a post
        :param request:
        :param post_id:
        :return:
        """
        pass

class PostReportView(View):
    def post(self, request, post_id):
        """
        Flag a post for review
        :param request:
        :param post_id:
        :return:
        """
        pass


# TODO: create views for users
