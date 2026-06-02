def check_water_level(location, level_metres):
    if level_metres < 3:
        status = "Safe"
    elif 3 <= level_metres <= 5:
        status = "Warning — Alert nearby villages"
    else:
        status = "DANGER — Evacuate immediately!"
    
    return status


# Given data
sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]

# Check each sensor and print the result
for location, level in sensors:
    status = check_water_level(location, level)
    print(f"{location} ({level} m): {status}")