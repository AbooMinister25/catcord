CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    token TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE servers (
    server_id TEXT PRIMARY KEY,
    owner_id TEXT NOT NULL,
    server_name TEXT NOT NULL,
    FOREIGN KEY(owner_id) REFERENCES USERS(user_id)
);

CREATE TABLE messages (
    message_id TEXT PRIMARY KEY,
    time_sent BIGINT NOT NULL,
    sender_id TEXT NOT NULL,
    server_id TEXT NOT NULL,
    message_content VARCHAR(1000) NOT NULL,
    FOREIGN KEY(sender_id) REFERENCES USERS(user_id),
    FOREIGN KEY(server_id) REFERENCES SERVERS(server_id)
)
