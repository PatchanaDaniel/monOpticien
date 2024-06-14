from django.db import models

# Create your models here.
class Client (models.Model):
    choix= (
        ('EV','EXAMEN DE LA VUE'), ('CL','CHOIX DE LUNETTES '),
        ('AL','AJUSTEMENT DE LUNETTES'),('SC','SUIVI ET CONTRÔLE'),
        # ...more options
    )
   
    default_choix='EXAMEN DE LA VUE'
    nom=models.CharField(max_length=25)
    prenom=models.CharField(max_length=45)
    motifs=models.CharField(max_length=60, choices=choix, default=default_choix)

  

    date=models.DateField()
    heure=models.TimeField()
