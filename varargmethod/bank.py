def balance_enq(**kwargs):
    print(kwargs)
    bank_name=kwargs.get("bank_name")
    acno=kwargs.get("acno")
    balance=kwargs.get("balance")
    print(f"your {bank_name} {acno} account balace is INR {balance}")

balance_enq(bank_name="SBI", acno="1234", balance="23455")
    