import pandas as pd
import boto3
import io
from pathlib import Path
import Constants.constants as cts
from Calculate.calculate_action_plan import calculate_action_plan_and_priority

bucket_name = cts.bucket_name.INVENTORY_MANAGEMENT
folder_name = cts.folder_name.DATA

def execute():
    data = read_data()
    action_plan_priority = data.apply(calculate_action_plan_and_priority, axis=1)
    for i, (action, prio) in enumerate(action_plan_priority):
        data.at[i, cts.Columns.ACTION_PLAN] = action
        data.at[i, cts.Columns.PRIORITY] = prio
    return data

def post_data(data,client_name):
    csv_data = data.to_csv(index=False)  
    s3 = boto3.client('s3')
    file_name = f"{client_name}.csv"
    s3.put_object(Bucket=bucket_name, Key=folder_name + file_name, Body=csv_data)

def fetch_data(client_name):
    try:
        s3 = boto3.client('s3')
        file_name = f"{client_name}.csv"
        response = s3.get_object(Bucket=bucket_name, Key=folder_name + file_name)
        csv_data = response['Body'].read().decode('utf-8')
        df = pd.read_csv(io.StringIO(csv_data))
        return df
    except Exception as e:
        return {"error": str(e)}
    
def read_data():
    current_dir = Path(__file__).parent
    csv_path = current_dir / '..' / 'Data' / 'Module2.csv'
    data = pd.read_csv(csv_path)
    return data

