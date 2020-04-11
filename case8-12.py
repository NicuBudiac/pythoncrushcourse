def create_sandwich(*incredients):
    print("\nPrepared sandwich should have following ingredients:")
    for incredient in incredients:
        print("- " + incredient)
create_sandwich(input("What kinf of ingredients do you have"))
create_sandwich('vegetables','meat')
create_sandwich('cheese','meat','fruits')
