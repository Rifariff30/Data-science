number_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {number_list}")

sq_evens = []

for num in number_list:
    if num % 2 == 0:
        sq_value = num ** 2
        sq_evens.append(sq_value)

print(f"Filtered and squared evens: {sq_evens}")