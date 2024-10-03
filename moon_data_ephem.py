import ephem
import datetime
import csv


def calculate_moon_phase_category(moon_phase):
    if (moon_phase <= (0.0625)):
        return 0  # New
    elif (moon_phase <= (0.1875)):
        return 1  # Waxing Crescent
    elif (moon_phase <= (0.2625)):
        return 2  # First Quarter
    elif (moon_phase <= (0.4375)):
        return 3  # Waxing Gibbous
    elif (moon_phase <= (0.5625)):
        return 4  # Full Moon
    elif (moon_phase <= (0.6875)):
        return 5  # Waning Gibbous
    elif (moon_phase <= (0.7625)):
        return 6  # Last Quarter
    elif (moon_phase <= (0.9375)):
        return 7  # Waning Crescent
    else:
        return 0  # New


def illuminated_area(moon_phase):
    if moon_phase >= 0.5:
        moon_phase = 1 - moon_phase
    return moon_phase * 2


start_date = datetime.date(1800, 1, 1)
end_date = datetime.date(2050, 1, 1)

filename = f"moon_phases_UTC_{start_date.year}-{end_date.year}.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Area', 'Category', 'Phase']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for date in (start_date + datetime.timedelta(days=n) for n in range((end_date - start_date).days + 1)):
        ephem_date = ephem.Date(date)
        prev_new = ephem.previous_new_moon(date)
        next_new = ephem.next_new_moon(date)
        moon_phase = (ephem_date - prev_new) / (next_new - prev_new)

        writer.writerow({
            'Date': date.strftime('%Y-%m-%d'),  # ISO 8601
            'Area': round(illuminated_area(moon_phase), 4),
            'Category': calculate_moon_phase_category(moon_phase),
            'Phase': round(moon_phase, 4),
        })
