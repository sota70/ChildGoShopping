from child import Child

def main():
    shop = { 
        "しらたき":120, 
        "こんにゃく":150, 
        "どらやき":160 
    }
    child = Child(1000)
    child.goShopping(shop, "こんにゃく", "どらやき")

main()