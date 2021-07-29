from tortoise import fields
from tortoise.models import Model


class Users(Model):
    user_id = fields.CharField(pk=True, null=False, max_length=255)
    token = fields.CharField(null=False, max_length=255)
    username = fields.CharField(null=False, max_length=255)
    password = fields.CharField(null=False, max_length=255)
    email = fields.CharField(null=False, max_length=255)

    def __str__(self):
        return self.name


class Servers(Model):
    server_id = fields.CharField(null=False, max_length=255, pk=True)
    server_name = fields.CharField(null=False, max_length=255)
    owner = fields.ForeignKeyField("models.Users", to_field="user_id")

    def __str__(self):
        return self.name


class Messages(Model):
    messages_id = fields.CharField(null=False, max_length=255, pk=True)
    time_sent = fields.BigIntField(null=False)
    message_content = fields.CharField(null=False, max_length=1000)
    sender_id = fields.ForeignKeyField("models.Users", to_field="user_id")
    server_id = fields.ForeignKeyField("models.Servers", to_field="server_id")

    def __str__(self):
        return self.name
