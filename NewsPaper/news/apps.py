from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        from . import signals

        from .tasks import send_mail
        from .scheduler import news_scheduler
        #print('started')

        news_scheduler.add_job(
            id='send mail',
            func=send_mail,
            trigger='interval',
            seconds=10,
        )
        #news_scheduler.start()
