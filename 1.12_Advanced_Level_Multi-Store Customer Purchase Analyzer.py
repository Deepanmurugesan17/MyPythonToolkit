store_data = {
    "StoreA": [
        ("Alice", ["Bread", "Milk", "Eggs"]),
        ("Bob", ["Bread", "Butter"]),
        ("Charlie", ["Milk", "Eggs", "Juice"]),
        ("Diana", ["Bread", "Juice"])
    ],
    "StoreB": [
        ("Alice", ["Eggs", "Cheese"]),
        ("Eve", ["Butter", "Juice"]),
        ("Bob", ["Milk", "Cheese"]),
        ("Charlie", ["Bread", "Butter"])
    ],
    "StoreC": [
        ("Diana", ["Milk", "Cheese"]),
        ("Alice", ["Butter", "Juice"]),
        ("Charlie", ["Bread", "Cheese"]),
        ("Frank", ["Eggs", "Juice"])
    ]
}
'''
{
  'Alice': {'Bread', 'Milk', 'Eggs', 'Cheese', 'Butter', 'Juice'},
  ...
}

'''
#Question : 1 - Expected Output as Mentioned above
# Output Variable Declaration for Question - 1 and Person Wise Purchased products across the stores.
result_1 = {}

for store,customer_details in store_data.items(): #Looping through the Dictionary.
    store_name = store
    for i in customer_details: #Looping through the Inner Details which is available in the form of lists in the values section of Dictionary
        name = i[0]
        purchased_products = i[1]

        if name not in result_1:
            result_1[name] = set(purchased_products)
        else:
            result_1[name].update(purchased_products)
print(result_1)

#Question : 2 Find the customer(s) who bought the highest number of unique items.
#Since we already Have items which were bought by each customer in the above output we can just count them.

max_count = 0
customer_name = []
for cust_name, purchased_products in result_1.items():
    total_count = len(purchased_products)
    if total_count > max_count:
        max_count = total_count
        customer_name = [cust_name]
    elif total_count == max_count:
        customer_name.append(cust_name)
print(f"The customer(s) who bought the highest number of unique items is {','.join(customer_name)} with total count of {max_count}")

'''
{
  'Bread': {'Alice', 'Bob', 'Charlie', 'Diana'},
  'Cheese': {'Alice', 'Bob', 'Diana', 'Charlie'},
  ...
}
'''
#Question:3 Create an item_customers dictionary:(Expected Output as Mentioned above)
#Since we are already having a dictionary with customer wise unique products purchased we can use the same one in a reverse manner to have
#Product wise the total number of customers.

result_2 = {}
for name, products in result_1.items():
    customer_name = name
    for i in products:
        if i not in result_2:
            result_2[i] = set([customer_name])
        elif i in result_2:
            result_2[i].add(customer_name)
print(result_2)

#Question:4 Identify items that were purchased in all three stores.
products_list = [] # Used to Collect all the products sold across each stores
result_3 = {}
#Store Wise Sold Product Details:
for store, details in store_data.items():
    for i in details:
        cust_name = i[0]
        products = i[1]
        for i in products:
            products_list.append(i) # This is to have Detailed Product List across all the stores in a separate set used for comparison in the next steps
            if store not in result_3:
                result_3[store] = set([i])
            else:
                result_3[store].add(i)
products_list = set(products_list) # To have Unique Products List
#print(result_3)
#print(products_list)

for store,products in result_3.items():
    common_products = products_list & products
    products_list = common_products

print(f"The Common Products acroos the three stores were {','.join(common_products)}")

#Question 5: Identify customers who bought at least one item from each store.
#Similar to Question 4
customer_list = []
user_list = []
result_4 = {}
for store,details in store_data.items():
    for i in details:
        name = i[0]
        products = i[1]
        user_list.append(name)
        if store not in result_4:
            result_4[store] = set([name])
        else:
            result_4[store].add(name)
user_list = set(user_list)
#print(result_4)
#print(user_list)

for store,users in result_4.items():
    common_user = user_list & users
    user_list = common_user
print(f"The Common User across all the three stores were {','.join(common_user)}")