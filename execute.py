import pandas as pd

data = pd.read_csv('Data/Module2.csv')


def get_current_stock_category(data):
    current_stock_category = []
    for i in range(len(data)):
        minimum_stock = data.iloc[i]['Minimum days'] * data.iloc[i]['Daily consumption']
        maximum_stock = data.iloc[i]['Maximum days'] * data.iloc[i]['Daily consumption']
        reorder_stock = data.iloc[i]['Re order days'] * data.iloc[i]['Daily consumption']
        reindent_stock = data.iloc[i]['Re indent days'] * data.iloc[i]['Daily consumption']
        current_stock = data.iloc[i]['Current Stock']
        if current_stock < minimum_stock:
            current_stock_category.append('Understock')
        elif current_stock < reorder_stock:
            current_stock_category.append('Critical')
        elif current_stock < reindent_stock:
            current_stock_category.append('To order')
        elif current_stock < maximum_stock:
            current_stock_category.append('To indent')
        else:
            current_stock_category.append('Overstock')
    return current_stock_category


def get_action_plan_and_priority(data):
    action_plan = []
    priority = []
    for i in range(len(data)):
        current_stock_category = data.iloc[i]['Current Stock Category']
        po_qty_raised = data.iloc[i]['PO raised']
        indent_qty_raised = data.iloc[i]['Indent raised']
        if current_stock_category == "Understock":
            priority.append("High")
            if po_qty_raised > 0:
                action_plan.append("Follow up with Vendor")
            elif po_qty_raised == 0 and indent_qty_raised > 0:
                action_plan.append("Place Order")
            else:
                action_plan.append("Raise Indent")
        elif current_stock_category == "Critical":
            if po_qty_raised > 0:
                priority.append("Medium")
                action_plan.append("Follow up with Vendor")
            elif po_qty_raised == 0 and indent_qty_raised > 0:
                priority.append("High")
                action_plan.append("Place Order")
            else:
                priority.append("High")
                action_plan.append("Raise Indent")
        elif current_stock_category == "To order":
            if po_qty_raised == 0 and indent_qty_raised > 0:
                priority.append("Medium")
                action_plan.append("Place Order")
            elif po_qty_raised == 0 and indent_qty_raised == 0:
                priority.append("High")
                action_plan.append("Raise Indent")
            else:
                priority.append("Low")
                action_plan.append("No action")
        elif current_stock_category == "To indent":
            if po_qty_raised == 0 and indent_qty_raised == 0:
                priority.append("Medium")
                action_plan.append("Raise Indent")
            else:
                priority.append("Low")
                action_plan.append("No action")
        else:
            priority.append("Low")
            action_plan.append("No action")

    return action_plan, priority


data['Current Stock Category'] = get_current_stock_category(data)
actionPlan, priority = get_action_plan_and_priority(data)
data['Action Plan'] = actionPlan
data['Priority'] = priority
print(data)
