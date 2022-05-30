from django.db import models

# Model for the database schema
# 1. Keys: PK, used for storing the keys
# 2. Values: Storing the values
class KeyDatabase(models.Model):
    keys = models.CharField(max_length=500, primary_key=True)
    values = models.CharField(max_length=500)

    def __str__(self):
        return self.keys