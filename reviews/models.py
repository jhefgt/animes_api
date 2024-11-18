from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from animes.models import Animes


class Review(models.Model):
    anime = models.ForeignKey(Animes, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'Avaliação não pode ser menor que 0 estrelas.'),
        MaxValueValidator(5, 'Avaliação não pode ser maior que 5 estrelas.'),])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.anime)
