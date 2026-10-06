n =  int(input("Number of products"))
print(n)
products = []
prices = []
stock = []

for _ in range(n):
    productname, Price , Qty = input().split()
    products.append(productname)
    prices.append(Price)
    stock.append(Qty)
    print(products)
print(prices)
print(stock)



def display_products():
    for i in range(len(products)):
        print(f"{products[i]} - {prices[i]} - Stock: {stock[i]}")
display_products()


def update_price(product_name, new_price):
    
    if product_name in products:
        
        index = products.index(product_name)
        
        prices[index] = new_price
        
        print(f"Updated {product_name} price to ${new_price}")
    
    else:
        print("Product not found!")
update_price("Bread", 5)




def update_stock(product_name, quantity):
    
    if product_name in products:
        
        index = products.index(product_name)
        
        stock[index] += quantity
        
        print(f"Updated {product_name} stock to {stock[index]}")
        
    else:
        print("Product not found!")
update_stock("Milk", 5)




def search_product(product_name):
    
    if product_name in products:
        
        index = products.index(product_name)
        
        print(f"{product_name} - Price: ${prices[index]}, Stock: {stock[index]}")
        
    else:
        print("Product not found!")
search_product("Cheese")





def delete_product(product_name):

    if product_name in products:

        index = products.index(product_name)

        products.remove(product_name)
        prices.pop(index)
        stock.pop(index)

        print(f"{product_name} deleted successfully!")

    else:
        print("Product not found!")

delete_product("Butter")

display_products()