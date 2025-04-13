from fastapi import APIRouter, HTTPException, status, Depends
from validations import user
from dao.user_dao import UserDao
from mariadb import Connection
from services import security
from database.connection import get_database_connection

user_router = APIRouter()
user_dao = UserDao()

@user_router.post("/login", status_code=status.HTTP_200_OK)
def user_login(user: user.UserLoginModel, db: Connection = Depends(get_database_connection)):
    database_user = user_dao.find_user(user.username, db)

    if database_user == None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Incorrect username or password')

    if security.compare_password(user.password, database_user.password) == False:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Incorrect username or password')
    
    jwt_token = security.encode_user_token(database_user.id, database_user.name)

    return { "token": jwt_token }
