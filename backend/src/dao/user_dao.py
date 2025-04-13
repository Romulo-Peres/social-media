from models.user import User
from mariadb import Connection
from typing import Annotated, Optional
from fastapi import Depends

class UserDao:
    _FIND_USER = 'SELECT id, name, password FROM users WHERE name = ?;'
    
    def find_user(self, username: str, db: Connection) -> Optional[User]:
        cursor = db.cursor()

        cursor.execute(self._FIND_USER, (username,))
        found_user = cursor.fetchall()

        cursor.close()
        db.close()
        
        if len(found_user) == 1:
            return User(found_user[0][0], found_user[0][1], found_user[0][2])
        else:
            return None
