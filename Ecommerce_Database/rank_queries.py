# pylint:disable=C0111,C0103
import sqlite3

conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

def order_rank_per_customer(db):
    query = """
    SELECT o.OrderID, o.CustomerID, o.OrderDate,
	RANK() OVER (PARTITION BY o.CustomerID
	ORDER BY o.OrderDate) AS OrderRank
    FROM Orders o
    """
    db.execute(query)
    results=db.fetchall()
    print(results)
    return (results)


def order_cumulative_amount_per_customer(db):
    query="""
    SELECT o.OrderID , o.CustomerID , o.OrderDate
    ,SUM(SUM(od.UnitPrice*od.Quantity)) OVER (PARTITION BY o.CustomerID ORDER BY o.OrderDate) AS cum_total
    FROM Orders o
    JOIN OrderDetails od on o.OrderID = od.OrderID
    GROUP BY o.OrderID
    """
    db.execute(query)
    results=db.fetchall()
    print(results)
    return (results)
