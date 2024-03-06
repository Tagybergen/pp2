from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера было:", yesterday)
print("Сегодня:", today)
print("Завтра будет:", tomorrow)