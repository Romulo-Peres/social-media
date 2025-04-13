from typing import Annotated, Optional
from database.connection import get_database_connection
from mariadb import Connection
from fastapi import Depends
from models.post import Post

class PostDao:
    _CREATE_QUERY = 'INSERT INTO posts (title, content, publisher_id) VALUES (?, ? , ?);'
    _DELETE_QUERY = 'DELETE FROM posts WHERE id = ?;'
    _LIST_POSTS_QUERY = 'SELECT p.id, p.title, p.content, u.name as publisher_name FROM posts AS p INNER JOIN users AS u ON p.publisher_id = u.id;'
    _UPDATE_POST_QUERY = 'UPDATE posts SET title = ?, content = ? WHERE id = ?;'
    _FIND_POST_PUBLISHER = 'SELECT publisher_id FROM posts WHERE id = ?;'
    
    def create_post(self, name: str, content: str, publisher_id: int, db: Connection):
        cursor = db.cursor()
        
        cursor.execute(self._CREATE_QUERY, (name, content, publisher_id))
        cursor.close()

        db.commit()
        db.close()

    def update_post(self):
        pass

    def delete_post(self, post_id: int, db: Connection):
        cursor = db.cursor()

        cursor.execute(self._DELETE_QUERY, (post_id,))
        cursor.close()

        db.commit()
        db.close()

    def list_posts(self, db: Connection) -> list[Post]:
        cursor = db.cursor()

        cursor.execute(self._LIST_POSTS_QUERY)
        fetched_data = cursor.fetchall()

        cursor.close()
        db.commit()
        db.close()

        return [Post(post[0], post[1], post[2], post[3]) for post in fetched_data]

    def update_post(self, post_id: int, title: str, content: str, db: Connection):
        cursor = db.cursor()

        cursor.execute(self._UPDATE_POST_QUERY, (title, content, post_id))
        cursor.close()

        db.commit()
        db.close()

    def find_post_publisher_id(self, post_id: int, db: Connection) -> Optional[int]:
        cursor = db.cursor()

        cursor.execute(self._FIND_POST_PUBLISHER, (post_id,))
        fetch_result = cursor.fetchall()

        cursor.close()

        db.close()
        
        if len(fetch_result) == 1:
            return fetch_result[0][0]
        else:
            return None
        
