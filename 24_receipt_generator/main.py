def main():
    print("=== Receipt Generator ===")
    
    products = []
    
    while True:
        name = input("\nProduct name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
            
        try:
            qty = int(input(f"Quantity of {name}: "))
            if qty <= 0:
                print("Quantity must be positive.")
                continue
                
            price = float(input(f"Price per unit of {name}: "))
            if price < 0:
                print("Price cannot be negative.")
                continue
                
            products.append({
                "name": name,
                "qty": qty,
                "price": price,
                "total": qty * price
            })
            
        except ValueError:
            print("Invalid input for quantity or price.")
            
    if not products:
        print("\nNo products added. Exiting...")
        return
        
    print("\n========== RECEIPT ==========\n")
    print(f"{'Product':<15} {'Qty':<5} {'Price'}")
    print("-" * 32)
    
    subtotal = 0
    for p in products:
        print(f"{p['name']:<15} {p['qty']:<5} ₹{p['total']:.2f}")
        subtotal += p['total']
        
    tax = subtotal * 0.05 # Assuming 5% tax
    grand_total = subtotal + tax
    
    print("-" * 30)
    print(f"{'Subtotal:':<15} ₹{subtotal:.2f}")
    print(f"{'Tax (5%):':<15} ₹{tax:.2f}")
    print("-" * 30)
    print(f"{'Total:':<15} ₹{grand_total:.2f}")
    print("==============================")

if __name__ == "__main__":
    main()
