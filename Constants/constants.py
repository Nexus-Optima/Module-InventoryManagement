class Categories:
    UNDERSTOCK = 'Understock'
    CRITICAL = 'Critical'
    TO_ORDER = 'To order'
    TO_INDENT = 'To indent'
    OVERSTOCK = 'Overstock'


class Actions:
    FOLLOW_UP = 'Follow up with Vendor'
    PLACE_ORDER = 'Place Order'
    RAISE_INDENT = 'Raise Indent'
    NO_ACTION = 'No action'


class Priorities:
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'


class Columns:
    ACTION_PLAN = 'Action Plan'
    PRIORITY = 'Priority'
    CURRENT_STOCK_CATEGORY = 'Current Stock Category'
    DAILY_CONSUMPTION = 'Daily consumption'
    CURRENT_STOCK = 'Current Stock'
    PO_RAISED = 'PO raised'
    INDENT_RAISED = 'Indent raised'


class Days:
    MINIMUM_DAYS = 'Minimum days'
    RE_ORDER_DAYS = 'Re order days'
    RE_INDENT_DAYS = 'Re indent days'
    MAXIMUM_DAYS = 'Maximum days'
