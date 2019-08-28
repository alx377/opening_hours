import datetime


def get_formatted_time(seconds):
    # If not full hour show also minutes
    if (seconds % 3600) == 0:
        time_str = (datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=seconds)).strftime("%I %p")
    else:
        time_str = (datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=seconds)).strftime("%I.%M %p")
    return time_str

def parse_data(data):
    opening_hours = []
    current_day_index = 0
    for day_name in data:
        day = data.get(day_name)

        # Handle if restaurant is closed the whole day
        if not day:
            opening_hours.append(f"{day_name.capitalize()}: Closed")
            current_day_index += 1
            continue

        # Handle closing of the restaurant on the next day
        day_opening_hours_str = f"{day_name.capitalize()}: "
        if day[0].get("type") == "close":
            seconds = day[0].get("value")
            closed_time = get_formatted_time(seconds)
            if current_day_index == 0 or opening_hours[current_day_index - 1].endswith("Closed"):
                raise ValueError(f"No data from yesterday, can not insert the closing time for day without data. Day: {day}")
            opening_hours[current_day_index-1] += f" - {closed_time}"
            day.pop(0)

        # Handle the normal open or close entry.
        for obj in day:
            obj_type = obj.get("type")
            if obj_type == "open":
                seconds = obj.get("value")
                opened_time = get_formatted_time(seconds)
                day_opening_hours_str += opened_time
            elif obj_type == "close":
                seconds = obj.get("value")
                closed_time = get_formatted_time(seconds)
                day_opening_hours_str += f" - {closed_time}"
            else:
                raise ValueError(f"Invalid type, only close and open are valid types. Tried {obj_type} as type.")

        opening_hours.append(day_opening_hours_str)
        current_day_index += 1

    return "\n".join(opening_hours)
