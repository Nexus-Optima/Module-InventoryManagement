import pandas as pd
import requests
from pathlib import Path

import Constants.constants as cts
from Calculate.calculate_action_plan import calculate_action_plan_and_priority


def execute():
    data = read_data()
    action_plan_priority = data.apply(calculate_action_plan_and_priority, axis=1)
    for i, (action, prio) in enumerate(action_plan_priority):
        data.at[i, cts.Columns.ACTION_PLAN] = action
        data.at[i, cts.Columns.PRIORITY] = prio
    return data


def read_data():
    current_dir = Path(__file__).parent
    csv_path = current_dir / '..' / 'Data' / 'Module2.csv'
    data = pd.read_csv(csv_path)
    return data


def fetch_data(url, params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


execute()
