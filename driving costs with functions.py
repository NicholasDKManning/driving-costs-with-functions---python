# Write a function driving_cost() 
# with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven, 
# that returns the dollar cost to drive those miles. #
# All items are of type float. 
# The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.
# Write a function driving_cost() 
# with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven, 
# that returns the dollar cost to drive those miles. 
# All items are of type float. 
# The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    
    dollar_cost_for_drive = (miles_driven / miles_per_gallon) * dollars_per_gallon
    
    return dollar_cost_for_drive


if __name__ == '__main__':
    
    miles_per_gallon = float(input())

    dollars_per_gallon = float(input())
    
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}') 
    
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
    
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')