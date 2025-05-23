def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Get input from user
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Check if discount was applied
    if final_price < original_price:
        print(f"Discount of {discount_percentage}% applied!")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print("No discount applied. Discount only applies for 20% or higher.")
        print(f"Original price: ${original_price:.2f}")
        
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
