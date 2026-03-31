from django.contrib import admin
from .models import Mutualist, Message
from .tasks import send_sms


@admin.register(Mutualist)
class MutualistAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number"]
    list_filter = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name", "phone_number"]
    ordering = ("last_name",)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    list_filter = ["title"]
    search_fields = ["title", "content"]
    ordering = ("title",)
    actions = ['send_message_to_mutualists']

    @admin.action(description="Envoyer ce SMS aux mutualistes")
    def send_message_to_mutualists(self, request, queryset):
        # Optimisation : récupérer les mutualistes en une seule requête
        queryset = queryset.prefetch_related('mutualists')
        
        for message in queryset:
            for mutualist in message.mutualists.all():
                send_sms.delay(mutualist.phone_number, message.content)
        self.message_user(request, "Envoi des messages aux mutualistes.")