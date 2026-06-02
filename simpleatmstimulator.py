accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500,  "pin": "5678"},
    "A003": {"name": "Bikash Rai",   "balance": 22000, "pin": "9012"}
}

def atm(account_id, pin, action, amount=0):
    # ── Guard 1: account must exist ──────────────────────────────
    if account_id not in accounts:
        print(f"Account not found: {account_id}")
        return

    account = accounts[account_id]

    # ── Guard 2: PIN must match ───────────────────────────────────
    if account["pin"] != pin:
        print(f"Incorrect PIN for account {account_id}.")
        return

    name    = account["name"]
    balance = account["balance"]

    # ── Actions ───────────────────────────────────────────────────
    if action == "balance":
        print(f"Account Holder : {name}")
        print(f"Current Balance: NPR {balance:,}")

    elif action == "deposit":
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        account["balance"] += amount
        print(f"NPR {amount:,} deposited successfully for {name}.")
        print(f"New Balance: NPR {account['balance']:,}")

    elif action == "withdraw":
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > balance:
            print(f"Insufficient funds for {name}.")
            print(f"Requested: NPR {amount:,} | Available: NPR {balance:,}")
        else:
            account["balance"] -= amount
            print(f"NPR {amount:,} withdrawn successfully for {name}.")
            print(f"Remaining Balance: NPR {account['balance']:,}")

    else:
        print(f"Unknown action '{action}'. Use: balance, deposit, or withdraw.")


# ── Test calls ────────────────────────────────────────────────────
print("=" * 45)
print("TEST 1 — Check balance (valid PIN)")
print("=" * 45)
atm("A001", "1234", "balance")

print("\n" + "=" * 45)
print("TEST 2 — Withdraw with wrong PIN")
print("=" * 45)
atm("A002", "0000", "withdraw", 2000)

print("\n" + "=" * 45)
print("TEST 3 — Deposit (valid PIN)")
print("=" * 45)
atm("A002", "5678", "deposit", 3000)

print("\n" + "=" * 45)
print("TEST 4 — Withdraw more than balance")
print("=" * 45)
atm("A003", "9012", "withdraw", 25000)

print("\n" + "=" * 45)
print("TEST 5 — Account does not exist")
print("=" * 45)
atm("A004", "1111", "balance")