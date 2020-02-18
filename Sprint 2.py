import matplotlib.pyplot as plt
import numpy as np

Price = [15, 18, 16.5, 10, 12, 12]
plt.title('Chips')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [25, 30, 26, 22, 22, 22]
plt.title('Chips')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)

plt.subplots()
Price = [20, 20, 16.5, 10, 12, 10]
plt.title('Coldrink')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [80, 30, 60, 22, 39, 50]
plt.title('Coldrink')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)


plt.subplots()
Price = [10, 8.5, 6, 8, 10.5, 8.5]
plt.title('Chocolates')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [30, 10, 33, 50, 60, 60] 
plt.title('Chocolates')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)


plt.subplots()
Price = [10, 8.5, 6, 10, 12, 15]
plt.title('Pies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [25, 30, 60, 10, 50, 55]
plt.title('Pies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)


plt.subplots()
Price = [5, 5.5, 3, 4.5, 10.5, 8.5]
plt.title('Fruits')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [25, 30, 60, 10, 33, 50]
plt.title('Fruits')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)


plt.subplots()
Price = [25, 20, 33, 35, 35, 20]
plt.title('Cupcakes')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [5, 30, 2, 10, 20, 30]
plt.title('Cupcakes')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)


plt.subplots()
Price = [15, 18, 16.5, 10, 12, 12]
plt.title('Veggies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Price, 'ro')
plt.plot(Price)
plt.subplots()
Quantity = [25, 30, 26, 22, 22, 22]
plt.title('Veggies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Price In Rands')
plt.plot(Quantity, 'ro')
plt.plot(Quantity)

Price = [15, 18, 16.5, 10, 12, 12]
bars = ('Simba', 'Lays', 'Doretos', 'Cheese-C', 'Jumping-J', 'Nik-Naks')
y_pos = np.arange(len(bars))

plt.title('Chips')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
 # Create bars
plt.bar(y_pos, Price)
 # Create names on the x-axis
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['purple', 'red', 'green', 'blue', 'cyan', 'yellow'])
plt.show()

Quantity = [25, 30, 26, 22, 22, 22]
bars = ('Simba', 'Lays', 'Doretos', 'Cheese-C', 'Jumping-J', 'Nik-Naks')
y_pos = np.arange(len(bars))
plt.title('Stock For Chips')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()



Price = [20, 20, 16.5, 10, 12, 10]
bars = ('Coke', 'Fanta', 'Pepsi', 'Jive', 'Kingsley', 'Refresh')
y_pos = np.arange(len(bars))
plt.title('Coldrink')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['pink', 'red', 'green', 'blue', 'cyan', 'yellow'])
plt.show()
Quantity = [80, 30, 60, 22, 39, 50]
bars = ('Coke', 'Fanta', 'Pepsi', 'Jive', 'Kingsley', 'Refresh')
y_pos = np.arange(len(bars))
plt.title('Stock For Coldrink')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()


Price = [10, 8.5, 6, 8, 10.5, 8.5]
bars = ('Kit Kat', 'Lunch Bar', 'P.S', 'Rolo', 'Bar-One', 'Tex')
y_pos = np.arange(len(bars))
plt.title('Chocolates')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['purple', 'red', 'orange', 'blue', 'black', 'yellow'])
plt.show()
Quantity = [30, 10, 33, 50, 60, 60]
bars = ('Kit Kat', 'Lunch Bar', 'P.S', 'Rolo', 'Bar-One', 'Tex')
y_pos = np.arange(len(bars))
plt.title('Stock For Chocolates')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()


Price = [10, 8.5, 6, 10, 12, 15]
bars = ('P/S Pie', 'S&K Pie', 'Sausage', 'Burger', 'Cheese', 'Chicken')
y_pos = np.arange(len(bars))
plt.title('Pies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['purple', 'red', 'green', 'blue', 'cyan', 'yellow'])
plt.show()
Quantity = [25, 30, 60, 10, 50, 55]
bars = ('P/S Pie', 'S&K Pie', 'Sausage', 'Burger', 'Cheese', 'Chicken')
y_pos = np.arange(len(bars))
plt.title('Stock For Pies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()

Price = [5, 5.5, 3, 4.5, 10.5, 8.5]
bars = ('Orange', 'Pear', 'Banana', 'Orange', 'Plum', 'Litchi')
y_pos = np.arange(len(bars))
plt.title('Fruits')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['blue', 'red', 'green', 'purple', 'cyan', 'yellow'])
plt.show()
Quantity = [25, 30, 60, 10, 33, 50]
bars = ('Orange', 'Pear', 'Banana', 'Orange', 'Plum', 'Litchi')
y_pos = np.arange(len(bars))
plt.title('Stock For Fruits')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()

Price = [25, 20, 33, 35, 35, 20]
bars = ('Vanilla', 'Chacolate', 'Strawberry', 'Blueberry', 'Caramel', 'Rasberry')
y_pos = np.arange(len(bars))
plt.title('Cupcakes')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['purple', 'yellow', 'green', 'blue', 'cyan', 'red'])
plt.show()
Quantity = [5, 30, 2, 10, 20, 30]
bars = ('Vanilla', 'Chacolate', 'Strawberry', 'Blueberry', 'Caramel', 'Rasberry')
y_pos = np.arange(len(bars))

Price = [15, 18, 16.5, 10, 12, 12, 20, 20, 16.5, 10, 12, 10, 10, 8.5, 6, 8, 10.5, 8.5, 10, 8.5, 6, 10, 12, 15, 5, 5.5, 3, 4.5, 10.5, 8.5, 25, 20, 33, 35, 35, 20, 15, 18, 16.5, 10, 12, 12]

Quantity = [25, 30, 26, 22, 22, 22, 80, 30, 60, 22, 39, 50, 30, 10, 33, 50, 60, 60, 25, 30, 60, 10, 50, 55, 25, 30, 60, 10, 33, 50, 5, 30, 2, 10, 20, 30, 25, 30, 26, 22, 22, 22]

color = np.random.rand(42)

size = np.random.randint(20, 30, 10)

# Creating a scatter plot

plt.scatter(Price, Quantity, c=color, s=size)

# Labeling the plot and showing it

plt.xlabel('Values from list Price')

plt.ylabel('Values from list Quantity')

plt.show()
plt.title('Stock For Cupcakes')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()

Price = [15, 18, 16.5, 10, 12, 12]
bars = ('Spinach', 'Cabbage', 'Carrots', 'Butternut', 'Tomatoes', 'beetroot')
y_pos = np.arange(len(bars))
plt.title('Veggies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Pricing In Rands')
plt.bar(y_pos, Price)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['purple', 'red', 'cyan', 'blue', 'green', 'yellow'])
plt.show()
Quantity = [25, 30, 26, 22, 22, 22]
bars = ('Spinach', 'Cabbage', 'Carrots', 'Butternut', 'Tomatoes', 'beetroot')
y_pos = np.arange(len(bars))
plt.title('Stock For Veggies')
plt.xlabel('Brands/Flavours')
plt.ylabel('Quantity')
plt.bar(y_pos, Quantity)
plt.xticks(y_pos, bars)
plt.bar(y_pos, Price, color=['black', 'black', 'black', 'black', 'black', 'black'])
plt.show()

