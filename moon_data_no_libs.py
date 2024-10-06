# For more accurate results check moon_data_ephem.py
# This file doesn't use external libraries and algorithms are based on:
# - https://nethack.fandom.com/wiki/Source:Hacklib.c#phase_of_the_moon
# - https://www.reddit.com/r/datasets/comments/au7e0n/moonlunar_phases_data_from_the_last_50_years/

import datetime
import csv


YEAR_MONTH_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year(year):
  return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))


def month_max_days(month, year):
  if month == 2 and is_leap_year(year):
    return 29
  else:
    return YEAR_MONTH_DAYS[month - 1]


def day_in_year(day, month, year):
  """Calculates the day of the year (1-based) for a given date."""
  days_sum = 0
  for month_test in range(1, month):
    days_sum += month_max_days(month_test, year)
  return day + days_sum


def phase_of_the_moon(day, month, year):
  """Calculates the phase of the moon for a given date (UTC)."""
  # moon period = 29.53058 days ~= 30, year = 365.2422 days
  # days moon phase advances on first day of year compared to preceding year
  #    = 365.2422 - 12*29.53058 ~= 11
  # years in Metonic cycle (time until same phases fall on the same days of
  #    the month) = 18.6 ~= 19
  # moon phase on first day of year (epact) ~= (11*(year%19) + 29) % 30
  #    (29 as initial condition)
  # current phase in days = first day phase + days elapsed in year
  # 6 moons ~= 177 days
  # 177 ~= 8 reported phases * 22
  # + 11/22 for rounding
  
  diy = day_in_year(day, month, year)
  golden_number = (year % 19) + 1
  epact = (11 * golden_number + 18) % 30
  if ((epact == 25 and golden_number > 11) or epact == 24):
    epact += 1

  category = int((((diy + epact) * 6 + 11) % 177) / 22) % 8
  phase = ((((diy + epact) * 6 + 11) % 177) / 22) / 8
  return category, phase


def illuminated_area(moon_phase):
    if moon_phase >= 0.5:
        moon_phase = 1 - moon_phase
    return moon_phase * 2


start_year = 1800
end_year = 2050

filename = f"moon_phases_{start_year}-{end_year}_UTC_no_lib.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Area', 'Category', 'Phase']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for year in range(start_year, end_year):
        for month in range(1, 13):
            for day in range(1, month_max_days(month, year) + 1):
                date = datetime.date(year, month, day)
                category, moon_phase = phase_of_the_moon(day, month, year)

                writer.writerow({
                    'Date': date.strftime('%Y-%m-%d'),  # ISO 8601
                    'Area': round(illuminated_area(moon_phase), 4),
                    'Category': category,
                    'Phase': round(moon_phase, 4),
                })
