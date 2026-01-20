from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.models.customer import Customer
from app.models.orders import Order
from app.models.order_items import OrderItem
import pandas as pd
import matplotlib.pyplot as plt

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/customers")
def aggregated_customer_data():
    query = """
    SELECT c.customer_id, c.name, c.city, COUNT(o.order_id) as total_orders, SUM(o.total_amount) as total_spent, AVG(o.total_amount) as average_order_value FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name, c.city
    HAVING COUNT(o.order_id) >= 3 AND SUM(o.total_amount) > (SELECT AVG(customer_total) FROM (SELECT SUM(total_amount) as customer_total FROM orders GROUP BY customer_id) AS average_spent)
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")
    
@app.get("/city")
def city_wise_revenue():
    query = """
    SELECT c.city, SUM(o.total_amount) as total_revenue FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.city ORDER BY total_revenue DESC
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

app.mount("/static", StaticFiles(directory="app/images"), name="static")
    
@app.get("/visualize", response_class=HTMLResponse)
def visualize_data():
    html_content = """
    <html>
        <head>
            <title>Customer Analytics Visualization</title>
        </head>
        <body style="text-align:center; font-family:Arial">

            <h2>Total Revenue by Customer Segment</h2>
            <img src="/static/revenue_by_customer_segment.png" width="600"/>

            <h2>Order Value Distribution by Customer Segment</h2>
            <img src="/static/distribution_of_order_values.png" width="600"/>

        </body>
    </html>
    """
    return html_content
    