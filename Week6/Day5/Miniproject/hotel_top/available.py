import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')
django.setup()


from datetime import date, timedelta
from visitors.models import Room, Availability

# Получить список всех комнат
rooms = Room.objects.all()

# Определить период дат, для которых нужно заполнить доступность
start_date = date.today()
end_date = start_date + timedelta(days=180)

# Создать записи в таблице Availability для каждой комнаты и даты
for room in rooms:
    current_date = start_date
    while current_date <= end_date:
        availability = Availability(room=room, date=current_date, available=True)
        availability.save()
        current_date += timedelta(days=1)

print("Data added")

