# Step 1: Input the size of the array
size = int(input("Enter the size of the array: "))

# Step 2: Input the elements of the array
elements = input("Enter the elements separated by space: ").split()

# Ensure we only take 'size' number of elements
if len(elements) != size:
    print(f"Please enter exactly {size} elements.")
else:
    # Convert the elements to integers
    elements = [int(num) for num in elements]

    # Step 3: Display the cube of each element
    for element in elements:
        print(element ** 3)
