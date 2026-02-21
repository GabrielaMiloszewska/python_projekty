from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def length(self):
        return len(self.content)

    def get_snippet(self, max_len=100):
        if len(self.content) <= max_len:
            return self.content
        return self.content[:100] + "..."



