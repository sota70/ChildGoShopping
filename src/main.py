from child import Child

def main():
    shopContent = { 
        "しらたき":120, 
        "こんにゃく":150, 
        "どらやき":160 
    }
    child = Child(1000)
    child.goShopping(shopContent, "こんにゃく", "どらやき")

main()