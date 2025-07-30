sales = [
    ("North", "apple", 5),
    ("South", "banana", 3),
    ("North", "banana", 2),
    ("East", "apple", 4),
    ("South", "apple", 7),
    ("North", "orange", 6),
    ("East", "banana", 1),
    ("South", "orange", 2),
    ("East", "orange", 5)
]

'''
{
    'North': {'apple': total, 'banana': total, ...},
    'South': {...},
    'East': {...}
}
'''
# To Form a Dictionary As Per requirement given above:
result = {}
for i in sales:
    region = i[0]
    product = i[1]
    quantity = i[2]
    if region not in result:
        result[region] = {}
    if product not in result[region]:
        result[region][product] = quantity
    else :
        result[region][product] += quantity
print(result)

#To Find the Total Quantities Sold in Each region:
for key,values in result.items():
    region = key
    product = values
    total_count = 0
    for product_name,product_qty in product.items():
        total_count += product_qty
    print(f"{region} : {total_count}")
#To Find The Top Sold Product in Each Region:
print("The Top Sold Product in Each Region:")
for key,values in result.items():
    region = key
    product = values
    max_count = 0
    top_product = []
    #print(f"{region}:{product}")
    for prd_name,qty_sld in product.items():
        if qty_sld > max_count:
            max_count = qty_sld
            top_product = [prd_name]
        elif qty_sld == max_count:
            top_product.append(prd_name)
    print(f"{region}:{','.join(top_product)}:{max_count}")