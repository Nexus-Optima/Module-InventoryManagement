import Constants.constants as cts


def calculate_current_stock_category(row):
    daily_consumption = row[cts.Columns.DAILY_CONSUMPTION]
    categories_thresholds = {
        cts.Categories.UNDERSTOCK: row[cts.Days.MINIMUM_DAYS] * daily_consumption,
        cts.Categories.CRITICAL: row[cts.Days.RE_ORDER_DAYS] * daily_consumption,
        cts.Categories.TO_ORDER: row[cts.Days.RE_INDENT_DAYS] * daily_consumption,
        cts.Categories.TO_INDENT: row[cts.Days.MAXIMUM_DAYS] * daily_consumption
    }
    current_stock = row[cts.Columns.CURRENT_STOCK]
    return next((category for category, threshold in categories_thresholds.items() if current_stock < threshold),
                cts.Categories.OVERSTOCK)


def calculate_action_plan_and_priority(row):
    stock_category = calculate_current_stock_category(row)

    actions = {
        cts.Categories.UNDERSTOCK: {
            True: (cts.Actions.FOLLOW_UP, cts.Priorities.HIGH),
            False: (cts.Actions.PLACE_ORDER if row[cts.Columns.INDENT_RAISED] > 0 else cts.Actions.RAISE_INDENT,
                    cts.Priorities.HIGH)
        },
        cts.Categories.CRITICAL: {
            True: (cts.Actions.FOLLOW_UP, cts.Priorities.MEDIUM),
            False: (cts.Actions.PLACE_ORDER if row[cts.Columns.INDENT_RAISED] > 0 else cts.Actions.RAISE_INDENT,
                    cts.Priorities.HIGH)
        },
        cts.Categories.TO_ORDER: {
            True: (cts.Actions.NO_ACTION, cts.Priorities.LOW),
            False: (cts.Actions.PLACE_ORDER, cts.Priorities.MEDIUM) if row[cts.Columns.INDENT_RAISED] > 0
            else (cts.Actions.RAISE_INDENT, cts.Priorities.HIGH)
        },
        cts.Categories.TO_INDENT: {
            True: (cts.Actions.NO_ACTION, cts.Priorities.LOW),
            False: (cts.Actions.NO_ACTION, cts.Priorities.LOW) if row[cts.Columns.INDENT_RAISED] > 0
            else (cts.Actions.RAISE_INDENT, cts.Priorities.MEDIUM)
        },
        cts.Categories.OVERSTOCK: {
            True: (cts.Actions.NO_ACTION, cts.Priorities.LOW),
            False: (cts.Actions.NO_ACTION, cts.Priorities.LOW)
        }
    }
    return actions[stock_category][row[cts.Columns.PO_RAISED] > 0]
