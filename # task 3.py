# task 3

def maxStockValue(stock):
    maxValue = float('-inf')
    current = stock
    while current:
        if current.value > maxValue:
            maxValue = current.value
        current = current.next
    return maxValue

def maxStockValueRec(week, maxValue=float('-inf')):
    if not week:
        return maxValue
    
    return maxStockValueRec(week.next, max(maxValue, week.value))