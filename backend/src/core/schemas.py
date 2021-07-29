from pydantic import BaseModel


class UserCreateBody(BaseModel):
    username: str
    password: str
    email: str


class NewServerBody(BaseModel):
    name: str


class NewMessageBody(BaseModel):
    server_id: str
    message_content: str


class UserBody(BaseModel):
    uid: str
    password: str
