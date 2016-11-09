from django.http import JsonResponse
from django.views.generic import View

from user_manager.models import Media, Comment


class PostListView(View):
    def get(self, request):
        """
        Get all photo/videos (Timeline)
        :param request:
        :return:
        """
        # .filter(uploader__public=True)
        all_photos = Media.objects.order_by('-created').all()[:100]
        photos_list = []
        for photo in all_photos:
            photos_list.append({
                'id': photo.id,
                'caption': photo.caption,
                'uploader_name': photo.uploader.get_full_name(),
                'uploader_id': photo.uploader.id,
                'media_address': photo.file.url,
                'likes_count': photo.likes.count(),
                'comments_count': photo.comments.count(),
                'created': photo.created,
                'modified': photo.modified,
            })

        return JsonResponse(photos_list, safe=False)

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
        photo = Media.objects.get(id=post_id)
        latest_comments = []
        for comment in Comment.objects.filter(media=photo).order_by('-created')[:3]:
            latest_comments.append({
                'commenter_name': comment.commenter.get_full_name(),
                'commenter_id': comment.commenter.id,
                'comment_text': comment.comment_text,
                'comment_id': comment.id,
            })
        photo_data = {
            'id': photo.id,
            'caption': photo.caption,
            'uploader_name': photo.uploader.get_full_name(),
            'uploader_id': photo.uploader.id,
            'media_address': photo.file.url,
            'likes_count': photo.likes.count(),
            'comments_count': photo.comments.count(),
            'created': photo.created,
            'modified': photo.modified,
            'latest_comments': latest_comments
        }

        return JsonResponse(photo_data)

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
