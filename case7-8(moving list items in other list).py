sandwich_orders = ['pocket', 'submarine', 'club', 'two_slices', 'two_halves', 'open_faced']
finished_sandwich = []
while sandwich_orders:
    removed = sandwich_orders.pop()
    print("I made you " + removed.title() + " sandwich")
    finished_sandwich.append(removed)
for sandwich in finished_sandwich:
    print("\n" + sandwich.title() + " sandwich was done")




