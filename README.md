# Fast-Food_Fast

## Continous Integration Badges
[![Build Status](https://travis-ci.org/lizz24/Fast-Food-Fast.svg?branch=master)](https://travis-ci.org/lizz24/Fast-Food-Fast)

Fast food fast is a food delivery service app for a restaurant

## API Features
The API contains the endpoints below:
| Endpoint                      | What it does  |
| ------------------------------| ------------- |
| POST /v1/orders               |Place an order  |
| GET /v1/orders                |Fetch all orders  |
| GET /v1/orders/int:order_id   |Fetch specific order|
|PUT /v1/orders/int:order_id    |Update order status  |
|DELETE /v1/orders/int:order_id |DELETE a specific posted order |

## Manual testing of the API
To manually test these endpoints, configure and run the server as below:

1. git checkout develop for all the endpoints

2. Create and activate a Virtual Environment.

3. Run pip install -r requirements.txt to install dependencies

4. Run export FLASK_APP=run.py

5. Run flask run to start the server

6. Test the endpoints at localhost:5000/api/v1/orders.
