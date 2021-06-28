from pydantic import BaseModel


class UserCreateBody(BaseModel):
    username: str
    password: str


class NewServerBody(BaseModel):
    name: str


class NewMessageBody(BaseModel):
    server_id: str
    message_content: str
