from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'