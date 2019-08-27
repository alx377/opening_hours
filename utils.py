from typing import Dict, List
import datetime

def parse_data(data: Dict[str, List[Dict[str, str]]]) -> str:
    opening_hours = []
    current_day_index = 0
    for day_name in data:
        day = data.get(day_name)

        # Handle if closed whole day
        if not day:
            opening_hours.append(f"{day_name.capitalize()}: Closed")
            current_day_index += 1
            continue

        # Handle closing the next day
        day_opening_hours_str = f"{day_name.capitalize()}: "
        if day[0].get("type") == "close":
            seconds = day[0].get("value")
            closed_time = (datetime.datetime(2019, 1, 1) + datetime.timedelta(seconds=seconds)).strftime("%I %p")
            if current_day_index == 0 or opening_hours[current_day_index - 1].endswith("Closed"):
                raise ValueError(f"No data from yesterday can not insert the closing time. Day: {day}")
            opening_hours[current_day_index-1] += f" - {closed_time}"
            day.pop(0)

        for obj in day:
            obj_type = obj.get("type")
            if obj_type == "open":
                seconds = obj.get("value")
                opened_time = (datetime.datetime(2019, 1, 1) + datetime.timedelta(seconds=seconds)).strftime("%I %p")
                day_opening_hours_str += opened_time
            elif obj_type == "close":
                seconds = obj.get("value")
                closed_time = (datetime.datetime(2019, 1, 1) + datetime.timedelta(seconds=seconds)).strftime("%I %p")
                day_opening_hours_str += f" - {closed_time}"
            else:
                raise ValueError(f"Invalid type only close and open are valid tried {obj_type}")

        opening_hours.append(day_opening_hours_str)
        current_day_index += 1
    return "\n".join(opening_hours)