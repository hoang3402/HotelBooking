from datetime import datetime

from django.dispatch import Signal

booking_status_changed = Signal()


def update_booking_status(sender, instance, **kwargs):
    if datetime.now().date() > datetime.strptime(instance.check_out_date,
                                                 "%Y-%m-%d").date() and instance.status == 'Confirmed':
        instance.status = 'Completed'
        instance.save()
    booking_status_changed.send(sender, instance=instance)
