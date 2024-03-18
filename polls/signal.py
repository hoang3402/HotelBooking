from datetime import datetime

from django.dispatch import Signal

booking_status_changed = Signal()


def update_booking_status(sender, instance, **kwargs):
    if datetime.now().date() > instance.check_out_date and instance.status == 'Confirmed':
        instance.status = 'Completed'
        instance.save()
    booking_status_changed.send(sender, instance=instance)
