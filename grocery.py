# ==========================================
# GROCERY COST COMPARISON TOOL
# ==========================================

print("=== GROCERY COST COMPARISON TOOL ===")

# --------- PART 1: what did this week's shop cost per person? ---------
# Store these five values in variables:
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

# Then work out basket_cost_per_person:
basket_cost_per_person = ((rice_price + milk_price + fruit_price) * number_of_baskets) / family_members

# Print the result.
print(f"Basket cost per person: {basket_cost_per_person}")


# --------- PART 2: can the items be shared equally? ---------
# Ask for total_items and people, both wrapped in int().
total_items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

# If people is 0, print a message saying you cannot share between 0 people.
if people == 0:
    print("You cannot share between 0 people.")
else:
    # Otherwise use % to check divisibility
    remainder = total_items % people
    if remainder == 0:
        # remainder 0 -> say they divide equally, and use // to say how many each
        items_each = total_items // people
        print(f"They divide equally. Each person gets {items_each} items.")
    else:
        # otherwise -> say they do not, and report the remainder
        print(f"They do not divide equally. The remainder is {remainder}.")


# --------- PART 3: fix the weekly average ---------
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

# Work backwards: multiply the average by the weeks to rebuild the total.
rebuilt_total = recorded_average * total_weeks

# Swap the wrong figure for the right one.
corrected_total = rebuilt_total - wrong_week_cost + correct_week_cost

# Divide by the weeks again to get corrected_average.
corrected_average = corrected_total / total_weeks

# Print all three numbers.
print(recorded_average, total_weeks, corrected_average)


# --------- PART 4: compare with three stores ---------
store_a_average = 70
store_b_average = 75
store_c_average = 80

# Use and to test all three at once.
# Store the outcome in a variable called verdict - do not just print it.
verdict = (corrected_average < store_a_average) and (corrected_average < store_b_average) and (corrected_average < store_c_average)


# --------- PART 5: the summary ---------
# Print basket_cost_per_person from Part 1, corrected_average from Part 3, and verdict from Part 4, all together.
print(f"Summary: Basket cost per person = {basket_cost_per_person}, Corrected average = {corrected_average}, Verdict = {verdict}")