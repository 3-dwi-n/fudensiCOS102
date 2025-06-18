def calculate_annual_tax_revenue(years_of_experience: int, age: int) -> float:
    """
    Calculates the Annual Tax Revenue (ATR) for a staff member at Izifin Technology
    based on their years of experience and age, according to the specified rules.

    Args:
        years_of_experience (int): The number of years of work experience of the staff.
        age (int): The age of the staff member.

    Returns:
        float: The calculated Annual Tax Revenue (ATR) in Naira (N).
    """
    if years_of_experience < 0 or age < 0:
        raise ValueError("Years of experience and age cannot be negative.")

    # Rule 1: More than 25 years of experience AND age >= 55
    if years_of_experience > 25 and age >= 55:
        return 5_600_000.0  # N5,600,000

    # Rule 2: More than 20 years of experience AND age >= 45
    elif years_of_experience > 20 and age >= 45:
        return 4_480_000.0  # N4,480,000

    # Rule 3: More than 10 years of experience AND age >= 35
    elif years_of_experience > 10 and age >= 35:
        return 1_500_000.0  # N1,500,000

    # Rule 4 (Else): Less than 10 years of experience AND below 35 years of age
    else:
        # This 'else' covers all other cases not met by the above conditions.
        # It specifically applies to staff with <= 10 years experience AND age < 35
        # but also implicitly covers cases where experience is low but age is high,
        # or vice-versa, if they don't meet the higher tiers.
        return 550_000.0  # N550,000

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Izifin Technology Annual Tax Revenue (ATR) Calculator ---")

    # Test cases based on the rules
    print("\nTest Case 1: Staff with >25 years experience and age >= 55")
    exp1, age1 = 26, 55
    atr1 = calculate_annual_tax_revenue(exp1, age1)
    print(f"Experience: {exp1} years, Age: {age1} years -> ATR: N{atr1:,.2f}")

    print("\nTest Case 2: Staff with >20 years experience and age >= 45 (but not Rule 1)")
    exp2, age2 = 22, 48
    atr2 = calculate_annual_tax_revenue(exp2, age2)
    print(f"Experience: {exp2} years, Age: {age2} years -> ATR: N{atr2:,.2f}")

    print("\nTest Case 3: Staff with >10 years experience and age >= 35 (but not Rule 1 or 2)")
    exp3, age3 = 15, 38
    atr3 = calculate_annual_tax_revenue(exp3, age3)
    print(f"Experience: {exp3} years, Age: {age3} years -> ATR: N{atr3:,.2f}")

    print("\nTest Case 4: Staff with <10 years experience and age < 35")
    exp4, age4 = 5, 30
    atr4 = calculate_annual_tax_revenue(exp4, age4)
    print(f"Experience: {exp4} years, Age: {age4} years -> ATR: N{atr4:,.2f}")

    print("\nTest Case 5: Edge case - Exactly 10 years experience, 35 years old (should fall to 'Else')")
    exp5, age5 = 10, 35
    atr5 = calculate_annual_tax_revenue(exp5, age5)
    print(f"Experience: {exp5} years, Age: {age5} years -> ATR: N{atr5:,.2f}")

    print("\nTest Case 6: Edge case - Exactly 20 years experience, 45 years old (should fall to 'Else')")
    exp6, age6 = 20, 45
    atr6 = calculate_annual_tax_revenue(exp6, age6)
    print(f"Experience: {exp6} years, Age: {age6} years -> ATR: N{atr6:,.2f}")

    print("\nTest Case 7: Experience meets criteria for higher tier, but age does not")
    exp7, age7 = 26, 40 # >25 years exp, but age < 55
    atr7 = calculate_annual_tax_revenue(exp7, age7)
    print(f"Experience: {exp7} years, Age: {age7} years -> ATR: N{atr7:,.2f}")

    print("\nTest Case 8: Age meets criteria for higher tier, but experience does not")
    exp8, age8 = 18, 55 # age >= 55, but exp not >25 or >20
    atr8 = calculate_annual_tax_revenue(exp8, age8)
    print(f"Experience: {exp8} years, Age: {age8} years -> ATR: N{atr8:,.2f}")

    # Example of error handling
    try:
        calculate_annual_tax_revenue(-5, 30)
    except ValueError as e:
        print(f"\nError caught for invalid input: {e}")
