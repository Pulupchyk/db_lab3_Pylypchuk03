import psycopg2
import matplotlib.pyplot as plt

username = 'Pylypchuk'
password = '3313'
database = 'Laptops_Info'
host = 'localhost'
port = '5432'

query_1 = '''
    DROP VIEW IF EXISTS AmountOfLaptopsByBrand;
    CREATE VIEW AmountOfLaptopsByBrand AS
    Select brand_name, Count(laptops.brand_id) as "quantity" from laptops 
    INNER JOIN brands ON brands.brand_id = laptops.brand_id
    group by brand_name, laptops.brand_id
    order by count(laptops.brand_id) desc;
    SELECT * FROM AmountOfLaptopsByBrand;
'''

query_2 = '''
    DROP VIEW IF EXISTS LaptopsWithDiscountAndWithout;
    CREATE VIEW LaptopsWithDiscountAndWithout AS
    Select 'Do not have' as "Discounts", count(discount_price) from prices where discount_price = old_price union
    Select 'Have', count(discount_price) from prices where discount_price < old_price;
    SELECT * FROM LaptopsWithDiscountAndWithout;
    '''

query_3 = '''
    DROP VIEW IF EXISTS LaptopsRatings;
    CREATE VIEW LaptopsRatings AS
    Select laptops.laptop_id, ratings_5max from laptops
    INNER JOIN ratings ON ratings.laptop_id = laptops.laptop_id 
    Where ratings_5max != '0';
    SELECT * FROM LaptopsRatings;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    
    brands = []
    quantity = []

    cur = conn.cursor()
    cur.execute(query_1)
    for row in cur:
        brands.append(row[0])
        quantity.append(row[1])
    
    x_range = range(len(brands))
 
    bar_ax.bar(x_range, quantity, label='Number of laptops by brands')
    bar_ax.set_title('Number of laptops by brands')
    bar_ax.set_xlabel('Brands')
    bar_ax.set_ylabel('Quantity')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(brands)

    discounts = []
    quantity = []

    cur = conn.cursor()
    cur.execute(query_2)
    for row in cur:
        discounts.append(row[0]) 
        quantity.append(row[1])
    
    pie_ax.pie(quantity, labels=discounts, autopct='%1.1f%%')
    pie_ax.set_title("Laptops without discount and with")

    rating = []
    nofr = []

    cur = conn.cursor()
    cur.execute(query_3)
    for row in cur:
        rating.append(row[0])
        nofr.append(row[1])
    
    graph_ax.plot(rating, nofr, marker='o')
    graph_ax.set_xlabel('laptop_id')
    graph_ax.set_ylabel('rating')
    graph_ax.set_title('Rating of laptops')

    for y, g_r in zip(rating, nofr):
        graph_ax.annotate(g_r, xy=(y, g_r), xytext=(7, 2), textcoords='offset points')
                   
plt.show()
