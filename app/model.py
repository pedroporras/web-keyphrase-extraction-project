from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None, title="Post ID")
    title: str = Field(default=None, title="Post Title")
    content: str = Field(default=None, title="Post Content")

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Post Demo",
                "content": "This is a demo post"
            }
        }
    
class UserSchema(BaseModel):
    fullname: str = Field(default=None, title="User Fullname")
    email: EmailStr = Field(default=None, title="User Email")
    password: str = Field(default=None, title="User Password")

    class Config:
        the_schema = {
            "name": "Bek",
            "email": "help@mail.com",
            "password": "12345"
        }

class UserLoginSchema(BaseModel):
    fullname: str = Field(default=None, title="User Fullname")
    email: EmailStr = Field(default=None, title="User Email")
    password: str = Field(default=None, title="User Password")

    class Config:
        the_schema = {
            "email": "help@mail.com",
            "password": "12345"
        }
