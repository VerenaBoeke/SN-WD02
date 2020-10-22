from blog_db_model import User, db, Post, Comment


def init_user():
    username = "User002"

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        print(f"Add user {username}")
        new_user = User(username=username)
        db.add(new_user)
        db.commit()
    else:
        print(f"User: {username} already in DB")

    return db.query(User).filter(User.username == username).one()


def init_posts(user):
    title = "Best title you've ever read"
    content = "This is the content you never read before. Deep and true words."

    post = db.query(Post).filter(Post.content == content).first()

    if post is None:
        print(f"Add post {title}")
        new_post = Post(title=title, content=content, user=user)
        db.add(new_post)
        db.commit()
    else:
        print(f"Post: {post.title} already in DB")

# Homework 1  "Erweitern des Skripts blog_db_inserts.py um init_comments erweitern"
def init_comments(user):
    content = "The Post is _the_ *hit!"

    comment = db.query(Comment).filter(Comment.content == content).first()

    if comment is None:
        print(f"Add comment {content}")
        new_comment = Comment(content=content, user=user)
        db.add(new_comment)
        db.commit()
    else:
        print(f"Comment: {comment.content} already in DB")


def start():
    #Insert a User, insert a first Post
    user = init_user()
    # idea: pass user_id to init_posts!
    init_posts(user)
    init_comments(user)

def queries():
    # find post with content "lorem ipsum", and output the username of the user who wrote it
    filter_content = "lorem ipsum"
    post = db.query(Post).filter(Post.content == filter_content).first()
    if post is not None:
        print(f"The Post '{filter_content}' has been written by: '{post.user.username}'")
    else:
        print(f"Could not find post with content {filter_content}")

# Homework 2  "Hinzufügen von Query um Kommentare zu finden"

def comment_queries():
    filter_comments = "The Post is shit!"
    comment = db.query(Comment).filter(Comment.content == filter_comments).first()

    if comment is not None:
        print(f"The Comment '{filter_comments}'' has been written by '{comment.user.username}' ")

    else:
        print(f"Could not find the comment '{filter_comments}'")


if __name__ == '__main__':
    start()
    queries()
    comment_queries()



"""
Hausaufgabe

- Erweitern des Skripts blog_db_inserts.py um ein hinzufügen von init_comments
- hinzufügen von queries um kommentare zu finden

"""
