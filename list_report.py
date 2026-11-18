# list_report.py

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("Numbered items:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

long_names_count = 0
for item in items:
    if len(item) > 4:
        long_names_count += 1

print("Items with more than 4 letters:", long_names_count)

longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print("Longest item name:", longest_item)