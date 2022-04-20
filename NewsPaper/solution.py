from news.models import *

# 1
first_user = User.objects.create(
    username="Scampish", first_name="Alena", last_name="Ermishina"
)
second_user = User.objects.create(
    username="Godzilla", first_name="Harry", last_name="Potter"
)

# 2
Author.objects.create(user=first_user)
Author.objects.create(user=second_user)

# 3
Category.objects.create(name="Education")
Category.objects.create(name="Health")
Category.objects.create(name="Politics")
Category.objects.create(name="Pets")

# 4
Post.objects.create(
    author=Author.objects.get(user=first_user),
    type=Post.NEWS,
    title="Title",
    text="Text",
)
Post.objects.create(
    author=Author.objects.get(user=first_user),
    type=Post.ARTICLE,
    title="Title Article 1",
    text="Text",
)
Post.objects.create(
    author=Author.objects.get(user=second_user),
    type=Post.ARTICLE,
    title="Title Article 2",
    text="Text",
)

# 5
first_post = Post.objects.get(pk=1)
second_post = Post.objects.get(pk=2)
third_post = Post.objects.get(pk=3)

first_post.categories.add(Category.objects.get(name="Education"))
first_post.categories.add(Category.objects.get(name="Health"))

second_post.categories.add(Category.objects.get(name="Politics"))

third_post.categories.add(Category.objects.get(name="Pets"))

# 6
first_post = Post.objects.get(pk=1)
second_post = Post.objects.get(pk=2)
third_post = Post.objects.get(pk=3)

first_user = User.objects.get(username="Scampish")
second_user = User.objects.get(username="Godzilla")

Comment.objects.create(post=first_post, user=first_user, text="Author comment")
Comment.objects.create(post=first_post, user=second_user, text="Other user comment")

Comment.objects.create(post=second_post, user=second_user, text="Other user comment")

Comment.objects.create(post=third_post, user=second_user, text="Author comment")

# 7
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=3).like()

Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()

# 8
Author.objects.get(user=User.objects.get(username="Scampish")).update_rating()
Author.objects.get(user=User.objects.get(username="Godzilla")).update_rating()

# 9
best_author = Author.objects.all().order_by("-rating").first()
best_author.user.username
best_author.rating

# 10
best_article = Post.objects.all().order_by("-rating").first()
print(best_article.created_at)
best_article.author.user.username
best_article.rating
best_article.title
best_article.preview()

# 11
for comment in best_article.comment_set.all():
    print(comment.created_at)
    print(comment.user.username)
    print(comment.rating)
    print(comment.text)
    print()
