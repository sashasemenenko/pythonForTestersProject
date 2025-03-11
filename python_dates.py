from datetime import date, datetime, timedelta

d = date(2025, 3, 11)

dt = datetime(2025, 3, 11, 10, 49, 15)

current_dt = datetime.now()

formatted_date = dt.strftime("%B %d, %Y, %H:%M:%S")
print(formatted_date)

dt_string = "2025-03-11 10:54:25"
parsed_date = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)


td = timedelta(days=5)

new_date = current_dt + td
print(current_dt)
print(new_date)
