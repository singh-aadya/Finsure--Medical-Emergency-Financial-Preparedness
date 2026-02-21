def predict_cost(age, dependents):
    base = 200000
    return base + age*1500 + dependents*30000

def calculate_gap(cost, savings, insurance):
    return max(cost - (savings + insurance), 0)

def risk_score(gap, income):
    if gap > income*6:
        return "High"
    elif gap > income*3:
        return "Medium"
    return "Low"

def recommendation(gap):
    if gap > 0:
        return f"Increase emergency fund. Save ₹{gap//12} monthly."
    return "You are financially prepared."