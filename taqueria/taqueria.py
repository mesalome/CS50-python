def main():
    taqueria()

def taqueria():
    n = 0
    items = {
                "baja taco": 4.00,
                "burrito": 7.50,
                "bowl": 8.50,
                "nachos": 11.00,
                "quesadilla": 8.50,
                "super burrito": 8.50,
                "super quesadilla": 9.50,
                "taco": 3.00,
                "tortilla salad": 8.00
            }
    while True:
        try:
            user_order = input("Item: ").lower()
            for item in items:
                if user_order == item.lower():
                    n += float(items[item])
                    print (f"${n:.2f}")
        except EOFError:
            break

main()