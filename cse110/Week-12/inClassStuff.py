import locale
shopping_list = [
    ("Bib Shorts",          "Clothing",      92.50),
    ("Roubaix",             "Bicycle",     3599.99),
    ("Cycling Computer",    "Accessories",  394.99),
    ("Helmet",              "Accessories",  299.99),
    ("Road Shoes",          "Shoes",        144.99),
    ("700c presta tube",    "Accessories",    5.25),
    ("Jersey",              "Clothing",      25.99),
    ("Multi-Function Tool", "Accessories",   22.99),
    ("Gloves",              "Accessories",    8.99),
    ("Cleats",              "Shoes",         15.99),
    ("Power Pedals",        "Accessories",  999.99),
    ("Socks",               "Clothing",       8.50)
]

locale.setlocale(locale.LC_ALL, '')


def print_list(shopping):
    ''' Print out the list in a user-friendly way '''
    for item in shopping:
        print(item[0], "costs: ",
              locale.currency(item[2], grouping=True))


def compute_total_cost(shopping):
    ''' Compute the total cost of the shopping list '''
    sum = 0
    for item in shopping:
        sum += item[2]
    return sum


def compute_min_max(shopping):
    ''' Compute the minimum and maximum value of the shopping list '''
    cheapest = None
    most_expensive = None
    for item in shopping:
        if cheapest == None or item[2] < cheapest:
            cheapest = item[2]
        if most_expensive == None or item[2] > most_expensive:
            most_expensive = item[2]

    return cheapest, most_expensive


def print_accessories(shopping):
    ''' Print only the accessories '''
    for item in shopping:
        if item[1] == "Accessories":
            print(item[0], "costs: ",
                  locale.currency(item[2], grouping=True))


def most_expensive_accessory(shopping):
    ''' Find the name of the most expensive accessory '''
    max_cost = None
    max_name = None
    for item in shopping:
        if item[1] == "Accessories" and (max_cost == None or max_cost < item[2]):
            max_cost = item[2]
            max_name = item[0]
    return max_name


print()
extremes = compute_min_max(shopping_list)
print_list(shopping_list)
print(
    f"\n\nThe total cost is: {locale.currency(compute_total_cost(shopping_list), grouping=True)}\n")
print(f"The cheapest item cost {locale.currency(extremes[0], grouping=True)}")
print(
    f"The most expensive item cost {locale.currency(extremes[1], grouping=True)}\n")
print_accessories(shopping_list)
print(
    f"\nThe most expensive accessory is {most_expensive_accessory(shopping_list)}\n")
