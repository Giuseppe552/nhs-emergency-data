import pathlib, requests

DATA_URL = "https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/"
OUT = pathlib.Path("data/raw/monthly_ae_time_series_latest.xls")
OUT.parent.mkdir(parents=True, exist_ok=True)

# Simple: fetch landing page, follow the "Monthly A&E Time Series" XLS link manually for now.
print(f"Please download the 'Monthly A&E Time Series' XLS from NHS England and save as: {OUT}")
print(DATA_URL)
