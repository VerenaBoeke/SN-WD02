from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

#Von SQL Alchemy um SWLAlchemy Befehle nutzen zu können
Base = declarative_base()


###
# Tables:

# Member
#   - id PK
#   - username TEXT

# Posts
#   - id PK
#   - text TEXT
#   - member_id FK

# Comments
#   - id PK
#   - text TEXT
#   - post_id FK
#   - member_id FK


class Member(Base):
    __tablename__ = 'Member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), nullable=False)


class Posts(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    member_id = Column(Integer, ForeignKey('Member.id'))

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(64000))
    post_id = Column(Integer, ForeignKey('Post.id'))
    member_id = Column(Integer, ForeignKey('Member.id'))
