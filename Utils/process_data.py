import pandas as pd


def process_data():
    file_path_me2l = '../sample_data/PO_LIST.XLSX'
    file_path_me5a = '../sample_data/PR_LIST.XLSX'
    file_path_mb51 = '../sample_data/MB51.XLSX'

    me2l_data = pd.read_excel(file_path_me2l)
    me5a_data = pd.read_excel(file_path_me5a)
    mb51_data = pd.read_excel(file_path_mb51)

    me5a_data_renamed = me5a_data.rename(columns={'Purchase order': 'Purchasing Document'})
    mb51_data_renamed = mb51_data.rename(columns={'Purchase order': 'Purchasing Document'})

    merged_data_2l_5a = pd.merge(me2l_data, me5a_data_renamed, on=['Material', 'Purchasing Document'], how='outer')
    merged_data_2l_51 = pd.merge(me2l_data, mb51_data_renamed, on=['Material', 'Purchasing Document'], how='outer')

    merged_data_2l_5a = merged_data_2l_5a.loc[:, ~merged_data_2l_5a.columns.str.endswith('_y')]
    merged_data_2l_5a.columns = merged_data_2l_5a.columns.str.rstrip('_x')

    merged_data_2l_51 = merged_data_2l_51.loc[:, ~merged_data_2l_51.columns.str.endswith('_y')]
    merged_data_2l_51.columns = merged_data_2l_51.columns.str.rstrip('_x')

    columns_to_display_2l_5a = [
        'Document Date', 'Purchasing Document', 'Material', 'Short Text',
        'Supplier/Supplying Plant', 'Purchase Requisition', 'Quantity requested',
        'Requisition date', 'Material Group', 'Quantity ordered',
        'Total Value', 'Valuation Price'
    ]

    columns_to_display_2l_51 = ['Document Date', 'Purchasing Document', 'Material', 'Short Text',
                                'Supplier/Supplying Plant', 'Material Document', 'Document Date']

    print(merged_data_2l_5a[columns_to_display_2l_5a].head(500).to_string())
    print(merged_data_2l_51[columns_to_display_2l_51].head(500).to_string())


process_data()