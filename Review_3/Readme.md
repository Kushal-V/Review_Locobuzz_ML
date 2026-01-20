# Customer Purchase Behavior Analytics API

## Business Scenario
The marketing team wants to identify high-value customers and understand how revenue is distributed across different customer segments and cities.

## Database Tables

### customers
- `customer_id` (Primary Key)
- `name`
- `city`
- `signup_date`

### orders
- `order_id` (Primary Key)
- `customer_id` (Foreign Key)
- `order_date`
- `total_amount`

### order_items
- `order_item_id` (Primary Key)
- `order_id` (Foreign Key)
- `product_category`
- `quantity`
- `price`

## Task Requirements

You must implement a FastAPI GET endpoint that performs the following:

### Data Extraction (PostgreSQL)
Aggregate customer-level metrics:
- Total number of orders per customer
- Total spending per customer
- Average order value per customer

Include only customers who:
- Have placed at least 3 orders
- Have total spending greater than the average spending of all customers

### Data Processing (Pandas)
Load the query result into a Pandas DataFrame

Segment customers into:
- **High Value**
- **Medium Value**
- **Low Value**
(Segmentation must be based on spending percentiles)

Identify the top 5 cities contributing the highest total revenue

### Visualization
Generate:
- A bar chart showing total revenue by customer segment
- A box plot showing distribution of order values across customer segments

### API Output
The endpoint should return:
- Aggregated customer data
- City-wise revenue summary
- Location or reference to generated visualizations
