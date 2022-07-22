# pylint:disable=C0111,C0103

import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''

    query=" SELECT o.OrderID id, c.ContactName , e.FirstName FROM Orders o JOIN Employees e ON e.EmployeeID  = o.EmployeeID JOIN Customers c ON c.CustomerID = o.CustomerID "
    db.execute(query)
    results=db.fetchall()
    return (results)

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query="SELECT c.ContactName, ROUND(SUM(od.UnitPrice*od.Quantity),2) as total FROM Orders o JOIN OrderDetails od ON od.OrderID =o.OrderID JOIN Customers c ON c.CustomerID =o.CustomerID GROUP BY c.ContactName ORDER BY total ASC "
    db.execute(query)
    results=db.fetchall()
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''

    query="""SELECT e.FirstName
	,e.LastName
	,ROUND(SUM(od.UnitPrice * od.Quantity),2) as total_sales
    FROM Orders o
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY e.EmployeeID
    ORDER BY total_sales DESC
    LIMIT 1"""

    db.execute(query)
    results=db.fetchone()
    print( results)
    return results

def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''

    query="""SELECT c.ContactName,count(OrderID) as orders
    FROM Customers c
    LEFT JOIN Orders o  ON o.CustomerID =c.CustomerID
    GROUP BY c.ContactName
    ORDER BY orders ASC  """

    db.execute(query)
    results=db.fetchall()
    print( results)
    return results
