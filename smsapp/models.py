from django.db import models

class Mutualist(models.Model):
    """This class represent a mutualist"""
    
    first_name = models.CharField("Prenoms", max_length=100)
    last_name = models.CharField("Nom", max_length=30)
    phone_number = models.CharField("Numero", max_length=10)

    class Meta:
        verbose_name = "Mutualiste"
        verbose_name_plural = "Mutualistes"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Message(models.Model):
    """This class represent a message sent to a mutualist"""
    
    mutualists = models.ManyToManyField(Mutualist, related_name="messages")
    title = models.CharField("Titre du message", max_length=100)
    content = models.TextField("Contenu du message")

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"Message {self.title}"