from pydantic import Field, BaseModel
from typing import Annotated

class CreatePostModel(BaseModel):
    title: Annotated[str, Field(max_length=256, min_length=4, description='The post title must be between 4 and 256 characters long.')]
    content: Annotated[str, Field(max_length=2048, min_length=8, description='The post content must be between 8 and 2048 characters long.')]

class DeletePostModel(BaseModel):
    post_id: Annotated[int, Field(gt=0, description='The post id must be greater than 0')]

class UpdatePostModel(BaseModel):
    post_id: Annotated[int, Field(gt=0)]
    title: Annotated[str, Field(max_length=256, min_length=4, description='The post title must be between 4 and 256 characters long.')]
    content: Annotated[str, Field(max_length=2048, min_length=8, description='The post content must be between 8 and 2048 characters long."')]

