from django.db import  models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from .managers import PostModelManager


class PostModel(BaseModel):
    """
    This is the model for Posts of the blog
    """
    category = models.ForeignKey(
        'blog.CategoryModel',
        verbose_name=_('Category'),
        help_text=_('Select a Category Name.'),
        related_name='post_model_category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=256,
        verbose_name=_('Post Title'),
        help_text=_('Title of the Post.'),
        null = True,
        blank=True,
    )
    text = models.TextField(
        verbose_name=_('Post Text'),
        help_text=_('Text of the Post.'),
        null=True,
        blank=True,
    )

    def __str__(self):
        return "{category}-{title}".format(category=self.category, title=self.title)

    objects = PostModelManager()

    class Meta:
        db_table = 'blog_posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
