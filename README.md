# Instructions to run
1. Inside, cloned repo folder: `python -m venv env`
1. Activate venv: `source env/bin/activate`
1. Install requirements: `pip install -r requirements.txt`
1. `python csv_generator.py`

# Variables
- `hostel`: Will fetch mess menu PDF from `/PDFs/<hostel>`. Make **`PDFs/`** folder
- `timings`: Self explanatory
- `use_holiday_time`: Some mess menus don't provide any holiday timings. Set this to `False` in this case and weekday timings will be used for all days.
- `merge_tables`: If the PDF is more than one page, set this variable to `True`
