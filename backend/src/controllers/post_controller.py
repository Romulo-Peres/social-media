from fastapi import APIRouter, Path, Depends, status, HTTPException
from validations import post as post_validations
from typing import Annotated
from models.utils import UserToken
from services.security import decode_user_token
from dao.post_dao import PostDao
from mariadb import Connection
from database.connection import get_database_connection

post_router = APIRouter()
post_dao = PostDao()

@post_router.post("/post", status_code = status.HTTP_201_CREATED)
def create_post(post: post_validations.CreatePostModel, user: UserToken = Depends(decode_user_token), db: Connection = Depends(get_database_connection)):
    post_dao.create_post(post.title, post.content, user['id'], db);

    
@post_router.put("/post", status_code = status.HTTP_200_OK)
def update_post(post: post_validations.UpdatePostModel, user: UserToken = Depends(decode_user_token), db: Connection = Depends(get_database_connection)):
    publisher = post_dao.find_post_publisher_id(post.post_id, db)

    if publisher == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Post not found');

    if publisher != user['id']:
        raise HTTPException(status.HTTP_403_FORBIDDEN, 'You don\'t have permission to update this post');

    post_dao.update_post(post.post_id, post.title, post.content, db)

    
@post_router.delete("/post", status_code = status.HTTP_200_OK)
def delete_post(post: post_validations.DeletePostModel, user: UserToken = Depends(decode_user_token), db: Connection = Depends(get_database_connection)):
    publisher = post_dao.find_post_publisher_id(post.post_id, db)

    if publisher == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'This post does not exist anymore')
    
    if publisher != user['id']:
        raise HTTPException(status.HTTP_403_FORBIDDEN, 'You don\'t have permission to delete this post');

    post_dao.delete_post(post.post_id, db)

    
@post_router.get("/posts", status_code = status.HTTP_200_OK)
def list_posts(user: UserToken = Depends(decode_user_token), db: Connection = Depends(get_database_connection)):
    posts = post_dao.list_posts(db)

    return { "posts": posts }
