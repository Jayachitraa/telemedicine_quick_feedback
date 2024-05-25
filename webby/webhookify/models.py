from django.db import models
import uuid

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    app_secret_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.account_id}"

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return f"{self.url}-{self.account.account_id}"
