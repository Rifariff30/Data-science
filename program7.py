pairs_list = []
print("enter key-value pairs (type 'done' when you are finished):")
while True:
    user_input = input("enter pair (format: key:value): ")
    if user_input.lower() == 'done':
        break
    if ":" in user_input:
        key, value = user_input.split( ":",1)
        pairs_list.append((key.strip(), value.strip()))
    else:
        print(" invalid format.please use 'key:value' (e.g., age:21)")
nested_tuple = tuple(pairs_list)
print(f"\nGenerated tuple: {nested_tuple}")
result_dict = dict(nested_tuple)
print(f"Resulting Dictionary: {result_dict}")
