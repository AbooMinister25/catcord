from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, nullable=False)
    token = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationships
    server = relationship("Server")
    message = relationship("Message")


class Server(Base):
    __tablename__ = "servers"

    server_id = Column(String, primary_key=True, nullable=False)
    server_name = Column(String, nullable=False)
    owner = Column(String, ForeignKey("users.user_id"))

    # Relationships
    messages = relationship("Message")


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(String, primary_key=True, nullable=False)
    time_sent = Column(BigInteger, nullable=False)
    message_content = Column(String, nullable=False)
    sender_id = Column(String, ForeignKey("users.user_id"))
    server_id = Column(String, ForeignKey("servers.server_id"))
