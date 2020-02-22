table_anvailability = input("For how many people do you want to reserve a table: ")
table_anvailability = int(table_anvailability)
if table_anvailability > 8:
    print("\nYou should wait for a table")
else:
    print('\nYour table is ready')