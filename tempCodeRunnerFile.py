    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)

    restaurant.pay_salary(chef)
    print('after salary', restaurant.revenue, restaurant.balance, restaurant.expense)
