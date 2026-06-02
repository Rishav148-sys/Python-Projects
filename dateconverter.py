bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
    "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
]

def ordinal(day):
    """Return day with suffix: 1st, 2nd, 3rd, 4th..."""
    if 11 <= day <= 13:
        return f"{day}th"
    suffix = {1: "st", 2: "nd", 3: "rd"}
    return f"{day}{suffix.get(day % 10, 'th')}"

def convert_date(date_str, from_cal, to_cal):
    """Convert date string between AD and BS calendars."""
    year, month, day = map(int, date_str.split("-"))

    if from_cal == to_cal:
        return date_str

    if from_cal == "AD" and to_cal == "BS":
        year += 56
    elif from_cal == "BS" and to_cal == "AD":
        year -= 56

    return f"{year:04d}-{month:02d}-{day:02d}"

def format_date(date_str, calendar, style, bs_months):
    """Format a date string based on requested style."""
    year, month, day = map(int, date_str.split("-"))

    if style == "iso":
        return f"{date_str} {calendar}"

    elif style == "full":
        if calendar == "BS":
            month_name = bs_months[month - 1]
            return f"{ordinal(day)} {month_name}, {year} {calendar}"
        else:
            import calendar as cal_lib
            ad_months = list(cal_lib.month_name)[1:]  # Jan–Dec
            month_name = ad_months[month - 1]
            return f"{ordinal(day)} {month_name}, {year} {calendar}"

    elif style == "nepali":
        if calendar == "BS":
            month_name = bs_months[month - 1]
            return f"{day} {month_name} {year} {calendar}"
        else:
            import calendar as cal_lib
            ad_months = list(cal_lib.month_name)[1:]
            month_name = ad_months[month - 1]
            return f"{day} {month_name} {year} {calendar}"

    return f"{date_str} {calendar}"


# Customer records
customers = [
    {"name": "Ramesh Thapa",  "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki",  "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai",    "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]

# Process and display each customer
for c in customers:
    converted_str = convert_date(c["date"], c["cal"], c["need"])
    formatted     = format_date(converted_str, c["need"], c["style"], bs_months)
    print(f"{c['name']:<16} | Original: {c['date']} {c['cal']} | Converted: {formatted}")