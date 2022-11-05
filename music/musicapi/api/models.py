from django.db import models

# Create your models here.

# declare a new model with a name "Artiste"

class ArtisteModel(models.Model):
 
    # Attributes for Artiste
    #song = models.OneToOneField(ArtisteModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.TextField()
 
    # renames the instances of this model with their first and last name
    def __str__(self):
        return self.first_name + " " + self.last_name


# declare a new model with a name "Song"

class SongModel(models.Model):
 
    # Attributes for Song
    artiste = models.ForeignKey(ArtisteModel, on_delete=models.CASCADE)
    #lyric = models.OneToOneField(LyricModel, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    date_released = models.DateField()
    likes = models.IntegerField()
    
 
    # renames the instances of this model with their title
    def __str__(self):
        return self.title


# declare a new model with a name "Lyric"

class LyricModel(models.Model):
 
    # Attributes for Lyric
    song_id = models.ForeignKey(SongModel, on_delete=models.CASCADE)
    content = models.TextField()
 