sandwich_orders = ['pastrami', 'pocket', 'submarine', 'club', 'pastrami', 'two_slices', 'two_halves', 'open_faced','pastrami']
print("Deli is out of pastrami ")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)