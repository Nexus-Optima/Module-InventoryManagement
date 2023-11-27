import pandas as pd


def process_data():
    file_path_me2l = '../sample_data/PO_LIST.XLSX'
    file_path_me5a = '../sample_data/PR_LIST.XLSX'
    file_path_mb51 = '../sample_data/MB51.XLSX'

    me2l_data = pd.read_excel(file_path_me2l)
    me5a_data = pd.read_excel(file_path_me5a)
    mb51_data = pd.read_excel(file_path_mb51)
    me2l_data = me2l_data.rename(columns={'Document Date': 'PO Date'})
    me5a_data_renamed = me5a_data.rename(columns={'Purchase order': 'Purchasing Document'})
    mb51_data_renamed = mb51_data.rename(columns={'Purchase order': 'Purchasing Document'})

    merged_data_2l_5a = pd.merge(me2l_data, me5a_data_renamed, on=['Material', 'Purchasing Document'], how='left')
    merged_data_2l_51 = pd.merge(me2l_data, mb51_data_renamed, on=['Material', 'Purchasing Document'], how='left')

    merged_data_2l_5a = merged_data_2l_5a.loc[:, ~merged_data_2l_5a.columns.str.endswith('_y')]
    merged_data_2l_5a.columns = merged_data_2l_5a.columns.str.rstrip('_x')
    merged_data_2l_5a = merged_data_2l_5a.dropna(subset=['Requisition date'])

    merged_data_2l_51 = merged_data_2l_51.loc[:, ~merged_data_2l_51.columns.str.endswith('_y')]
    merged_data_2l_51.columns = merged_data_2l_51.columns.str.rstrip('_x')
    merged_data_2l_51 = merged_data_2l_51.dropna(subset=['Document Date'])
    columns_to_display_2l_5a = [
        'PO Date', 'Purchasing Document', 'Material', 'Short Text',
        'Supplier/Supplying Plant', 'Purchase Requisition', 'Quantity requested',
        'Requisition date', 'Material Group', 'Quantity ordered',
        'Total Value', 'Valuation Price'
    ]

    columns_to_display_2l_51 = ['PO Date', 'Purchasing Document', 'Material', 'Short Text',
                                'Supplier/Supplying Plant', 'Material Document', 'Document Date']
    pr_dict = {}
    grn_dict = {}
    for index, row in merged_data_2l_5a.iterrows():
        if row['Material'] not in pr_dict:
            pr_dict[row['Material']] = [(row['PO Date'] - row['Requisition date']).days]
        else:
            pr_dict[row['Material']].append((row['PO Date'] - row['Requisition date']).days)
    print(pr_dict)
    for index, row in merged_data_2l_51.iterrows():
        if row['Material'] not in grn_dict:
            grn_dict[row['Material']] = [(row['Document Date'] - row['PO Date']).days]
        else:
            grn_dict[row['Material']].append((row['Document Date'] - row['PO Date']).days)
    print(grn_dict)
    print(len(pr_dict))

    result_dict = {}
    for i in pr_dict.keys():
        if i in grn_dict:
            temp_dict = {i: {'PRDAYS': round(sum(pr_dict.get(i))/len(pr_dict.get(i)),2), 'GRNDAYS': round(sum(grn_dict.get(i))/len(grn_dict.get(i)),2)}}
            result_dict.update(temp_dict)
    print(result_dict)
    # print(merged_data_2l_5a[columns_to_display_2l_5a].tail(500).to_string())
    # print(merged_data_2l_51[columns_to_display_2l_51].tail(500).to_string())


process_data()