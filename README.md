# moon-data
Daily moon phases in csv and scripts to calculate lunar data.

## moon_phases_UTC_1800-2050.csv
Clone this repository or [download it as a ZIP file](https://github.com/isaacbernat/moon-data/archive/refs/heads/main.zip) or [download `moon_phases_UTC_1800-2050.csv` file](https://raw.githubusercontent.com/isaacbernat/moon-data/refs/heads/main/moon_phases_UTC_1800-2050.csv)

Implementation used to calculate data available in this repo, see [moon_data_ephem.py](https://github.com/isaacbernat/moon-data/blob/main/moon_data_ephem.py)

The csv has one entry per day from 1800 until 2050. Each daily entry has 4 columns with the following info:
### Date
In UTC following ISO 8601 format (YEAR-MONTH-DAY), e.g. 2024-10-04 for the 4rd of October of 2024.
### Area
Ratio of illuminated area of moon's surface. 1.0 means maximum (full), and 0.0 means completely dark (new).
### Category
Numerical description of moon's phase. Its range is 0-7 and matches this description.
- 0 = 🌑 (New Moon).
- 1 = 🌒 (Waxing Crescent Moon).
- 2 = 🌓 (First Quarter Moon).
- 3 = 🌔 (Waxing Gibbous Moon).
- 4 = 🌕 (Full Moon).
- 5 = 🌖 (Waning Gibbous Moon).
- 6 = 🌗 (Last Quarter Moon).
- 7 = 🌘 (Waning Crescent Moon).
### Phase
Ratio of current moon cycle using `next_new_moon` relative to `previous_new_moon` and [ephem](https://pypi.org/project/ephem/) Python's library. 0.0 would mean the phase just started and 1.0 it ended. Therefore, 0.5 means full moon, 0.25 First Quarter Moon and 0.75 Last Quarter Moon.

## Python scripts
### moon_data_ephem.py
Script used to calculate `moon_phases_UTC_1800-2050.csv`. It relies on [ephem](https://pypi.org/project/ephem/) Python's library.
### moon_data_no_libs.py
Script which does not depend on external libraries. Its calculations for moon phases may not be as accurate as those above, but are useful if there's no access to pip and/or faster calculations are needed.
