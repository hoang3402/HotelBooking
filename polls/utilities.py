import calendar
from datetime import datetime, timedelta, date
from decimal import Decimal

import requests

from polls.models import Booking


def get_exchange_rate(api_key, from_currency, to_currency, amount=1):
    url = 'https://currency-exchange.p.rapidapi.com/exchange'
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': 'currency-exchange.p.rapidapi.com'
    }
    params = {
        'from': from_currency,
        'to': to_currency,
        'q': str(amount)
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Handle API request error
        return None


def is_room_available(room, check_in_date, check_out_date):
    # Check if the room is available for the specified dates
    existing_bookings = Booking.objects.filter(
        room=room,
        check_in_date__lt=check_out_date,
        check_out_date__gt=check_in_date,
        status__in=['Pending', 'Confirmed', 'Completed']
    )

    return not existing_bookings.exists()


def days_available_of_room(room, year, month):
    # Check if the room is available for the specified dates
    start_date = date(year, month, 1)  # Create the first day of the month
    end_date = start_date + timedelta(
        days=calendar.monthrange(year, month)[1] - 1)  # Last day of the month (excluding next month)

    # Adjust the query based on your data model and booking status definition
    existing_bookings = Booking.objects.filter(
        room=room,
        status__in=['Pending', 'Confirmed'],
        check_out_date__gte=start_date,
        check_in_date__lte=end_date
    )

    # All days in the month
    all_days = [start_date + timedelta(days=i) for i in range(end_date.day)]

    available_days = []
    for day in all_days:
        if not existing_bookings.filter(check_in_date__lte=day, check_out_date__gte=day).exists():
            available_days.append(day)

    return available_days


def calculate_total_cost(check_in_date, check_out_date, foreign_price, exchange_rate):
    # Step 2: Calculate the number of nights
    check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d')
    check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d')
    number_of_nights = (check_out_date - check_in_date).days

    exchange_rate = Decimal(exchange_rate)
    # Step 3: Convert the price to local currency
    local_price = foreign_price * exchange_rate

    # Step 4: Calculate the total cost
    total_cost = local_price * number_of_nights

    return total_cost
