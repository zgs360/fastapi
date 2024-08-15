
from tortoise.models import Model
from tortoise import fields

class LawModel(Model):
    id = fields.IntField(pk=True)
    xfa_id = fields.CharField(max_length=10)
    title = fields.CharField(max_length=500)
    body = fields.TextField()
    learn = fields.BooleanField()
    plzy = fields.BooleanField()
    xinlaw = fields.BooleanField()
    class Meta:
        table = "xinlaw_xfa"