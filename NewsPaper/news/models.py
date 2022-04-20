from django.db import models

from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        posts = self.post_set.all()

        post_rating = posts.aggregate(total_rating=models.Sum("rating")).get(
            "total_rating"
        )
        author_comment_rating = (
            self.user.comment_set.all()
            .aggregate(total_rating=models.Sum("rating"))
            .get("total_rating")
        )
        comment_rating = 0
        for post in posts:
            comment_rating += (
                post.comment_set.all()
                .aggregate(total_rating=models.Sum("rating"))
                .get("total_rating")
            )

        self.rating = post_rating * 3 + author_comment_rating + comment_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    NEWS = "NW"
    ARTICLE = "AR"
    TYPE_CHOICES = [
        (NEWS, "news"),
        (ARTICLE, "article"),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=ARTICLE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Category, through="PostCategory")

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self) -> str:
        return self.text[:124] + "..."


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
