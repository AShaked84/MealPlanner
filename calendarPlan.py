from datetime import datetime, timedelta

today = datetime.today().date()

# strftime("%w") returns 0 for Sunday, 1 for Monday... up to 6 for Saturday
days_since_sunday = int(today.strftime("%w"))
start_of_week = today - timedelta(days=days_since_sunday)

# Generate all 7 days of the week
this_week = [start_of_week + timedelta(days=i) for i in range(7)]

print(f"--- Week of {start_of_week} (Sunday Start) ---")
for day in this_week:
    print(f"{day.strftime('%A')}: {day}")

#how many servings do we have of each 