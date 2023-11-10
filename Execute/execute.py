import pandas as pd
import Constants.constants as cts
from Calculate.calculate_action_plan import calculate_action_plan_and_priority


def execute():
    data = read_data()
    action_plan_priority = data.apply(calculate_action_plan_and_priority, axis=1)
    for i, (action, prio) in enumerate(action_plan_priority):
        data.at[i, cts.Columns.ACTION_PLAN] = action
        data.at[i, cts.Columns.PRIORITY] = prio

    print(data)


def read_data():
    data = pd.read_csv('../Data/Module2.csv')
    return data


execute()
