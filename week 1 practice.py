import math

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculates Simple Interest.

    Formula: A = P * (1 + (R/100) * T)
    Where:
    A = Total Amount (Principal + Interest)
    P = Principal amount (initial investment)
    R = Annual interest rate (as a percentage, e.g., 5 for 5%)
    T = Time in years

    Args:
        principal (float): The initial principal amount.
        rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        time (float): The time in years.

    Returns:
        float: The total amount (Principal + Simple Interest).
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative values.")
    
    # Calculate the simple interest part
    simple_interest = principal * (rate / 100) * time
    # Calculate the total amount
    total_amount = principal + simple_interest
    return total_amount

def calculate_compound_interest(principal: float, rate: float, compounding_frequency: int, time: float) -> float:
    """
    Calculates Compound Interest.

    Formula: A = P * (1 + R/n)^(n*t)
    Where:
    A = Total Amount (Principal + Compound Interest)
    P = Principal amount (initial investment)
    R = Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    n = Number of times interest is compounded per year
    t = Time in years

    Args:
        principal (float): The initial principal amount.
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        compounding_frequency (int): The number of times interest is compounded per year (e.g., 1 for annually, 4 for quarterly, 12 for monthly).
        time (float): The time in years.

    Returns:
        float: The total amount (Principal + Compound Interest).
    """
    if principal < 0 or rate < 0 or compounding_frequency <= 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative; compounding frequency must be positive.")
    
    # Calculate the compound interest total amount
    amount = principal * (1 + rate / compounding_frequency)**(compounding_frequency * time)
    return amount

def calculate_annuity_plan(payment: float, rate: float, compounding_frequency: int, time: float) -> float:
    """
    Calculates the Future Value of an Ordinary Annuity.

    Formula: A = PMT * [((1 + R/n)^(n*t) - 1) / (R/n)]
    Where:
    A = Future Value of the Annuity
    PMT = Payment made each period
    R = Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    n = Number of times interest is compounded per year
    t = Time in years

    Args:
        payment (float): The periodic payment amount (PMT).
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        compounding_frequency (int): The number of times interest is compounded per year.
        time (float): The total time in years.

    Returns:
        float: The future value of the annuity.
    """
    if payment < 0 or rate < 0 or compounding_frequency <= 0 or time < 0:
        raise ValueError("Payment, rate, and time must be non-negative; compounding frequency must be positive.")
    if rate == 0: # Handle zero interest rate to avoid division by zero
        return payment * compounding_frequency * time # Simple accumulation without interest
        
    rate_per_period = rate / compounding_frequency
    number_of_periods = compounding_frequency * time

    # Calculate the future value of the annuity
    future_value = payment * (( (1 + rate_per_period)**number_of_periods - 1) / rate_per_period )
    return future_value

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Financial Calculations ---")

    # a) Simple Interest Example
    p_si = 1000  # Principal
    r_si = 5     # Annual rate (5%)
    t_si = 3     # Time in years
    amount_si = calculate_simple_interest(p_si, r_si, t_si)
    print(f"\nSimple Interest:")
    print(f"Principal (P): N{p_si:,.2f}")
    print(f"Annual Rate (R): {r_si}%")
    print(f"Time (T): {t_si} years")
    print(f"Total Amount (A): N{amount_si:,.2f}")

    # b) Compound Interest Example
    p_ci = 1000    # Principal
    r_ci = 0.05    # Annual rate (5% as a decimal)
    n_ci = 12      # Compounded monthly
    t_ci = 3       # Time in years
    amount_ci = calculate_compound_interest(p_ci, r_ci, n_ci, t_ci)
    print(f"\nCompound Interest:")
    print(f"Principal (P): N{p_ci:,.2f}")
    print(f"Annual Rate (R): {r_ci:.2%}") # Format as percentage
    print(f"Compounding Frequency (n): {n_ci} times/year")
    print(f"Time (t): {t_ci} years")
    print(f"Total Amount (A): N{amount_ci:,.2f}")

    # c) Annuity Plan Example
    pmt_an = 100   # Payment per period
    r_an = 0.04    # Annual rate (4% as a decimal)
    n_an = 4       # Compounded quarterly
    t_an = 5       # Time in years (20 quarters)
    amount_an = calculate_annuity_plan(pmt_an, r_an, n_an, t_an)
    print(f"\nAnnuity Plan (Future Value of Ordinary Annuity):")
    print(f"Periodic Payment (PMT): N{pmt_an:,.2f}")
    print(f"Annual Rate (R): {r_an:.2%}")
    print(f"Compounding Frequency (n): {n_an} times/year")
    print(f"Time (t): {t_an} years")
    print(f"Future Value of Annuity (A): N{amount_an:,.2f}")

    # Example of error handling
    try:
        calculate_simple_interest(-100, 5, 3)
    except ValueError as e:
        print(f"\nError caught: {e}")

    try:
        calculate_compound_interest(1000, 0.05, 0, 3)
    except ValueError as e:
        print(f"\nError caught: {e}")

    try:
        calculate_annuity_plan(100, 0, 4, 5) # Example with zero rate for annuity
        print(f"\nAnnuity with zero rate: N{calculate_annuity_plan(100, 0, 4, 5):,.2f}")
    except ValueError as e:
        print(f"\nError caught: {e}")

