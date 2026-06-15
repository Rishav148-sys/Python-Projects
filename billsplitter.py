import random

# Seed for consistent results
random.seed(42)

# Given data
friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750


def split_bill(friends, total):
    """Returns the equal amount each person pays."""
    return total / len(friends)


def pick_lucky(friends):
    """Uses random.choice to pick one lucky person."""
    return random.choice(friends)


def final_summary(friends, total):
    """Prints full bill summary including lucky person's extra charge."""

    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    # Local variable - only exists inside this function
    lucky_total = share + 50

    print("=========================================")
    print("       Thamel Restaurant Bill Split      ")
    print("=========================================")
    print(f"Total Bill     : NPR {total}")
    print(f"Number of Friends : {len(friends)}")
    print(f"Equal Share    : NPR {share:.2f} each")
    print("-----------------------------------------")
    print("Individual Shares:")
    for friend in friends:
        if friend == lucky_person:
            print(f"  {friend:<10} : NPR {lucky_total:.2f}  <-- Lucky Tax (+NPR 50)")
        else:
            print(f"  {friend:<10} : NPR {share:.2f}")
    print("-----------------------------------------")
    print(f"Lucky Person   : {lucky_person}")
    print(f"Lucky Person's Total : NPR {lucky_total:.2f} (NPR {share:.2f} + NPR 50)")
    print("=========================================")


# Call the summary function
final_summary(friends, total_bill)