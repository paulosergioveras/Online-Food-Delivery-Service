# Online Food Delivery System

## Overview

This project is an online food delivery system developed as part of the Software Project course at the Federal University of Alagoas (Universidade Federal de Alagoas - UFAL), taught by Professor Dr. Baldoíno Fonseca dos Santos Neto.

## Features and Implementation

### 1. Restaurant Profile Management
- **Implementation**: Created `Restaurant` and `Menu` models.
- **Model**: `Restaurant` model stores details like name, owner, address, phone, and description. `Menu` model tracks dishes details (e.g., name, description, name, etc.).
- **Serializer**: `RestaurantSerializer` handles data serialization.
- **View**: `RestaurantViewSet` manages API endpoints for CRUD operations.
- **URL**: Registered routes in `urls.py`.

### 2. Order Placement and Management
- **Implementation**: Created `Order` and `OrderItem` models.
- **Model**: `Order` model tracks order details, status, and related restaurant. `Menu` model tracks dishes details (e.g., name, description, name, etc.).
- **Serializer**: `OrderSerializer` and `OrderItemSerializer` manage serialization.
- **View**: `OrderViewSet` handles API endpoints.
- **URL**: Registered in `urls.py`.

### 3. Delivery Tracking
- **Implementation**: Used `status` field in the `Order` model to track order status.
- **View**: API endpoint to update and retrieve order status.

### 4. Payment Processing
- **Implementation**: Created `Payment` model and integrated Stripe for transactions.
- **Model**: `Payment` stores transaction details like payment method, order and price.
- **Serializer**: `PaymentSerializer` for data handling.
- **View**: `PaymentViewSet` with a `create_payment_intent` action for Stripe integration.
- **URL**: Payment-related routes added.

### 5. Customer Reviews and Ratings
- **Implementation**: Created `Reviews` model.
- **Model**: Stores ratings and comments by the clients to restaurants.
- **Serializer**: `ReviewsSerializer` for API responses.
- **View**: `ReviewsViewSet` handles CRUD operations.
- **URL**: Added review routes.

### 6. Promotion and Discount Management
- **Implementation**: Created `Promotion` model.
- **Model**: Stores restaurant discount details for customers.
- **Serializer**: `PromotionSerializer` for data handling.
- **View**: `PromotionViewSet` for handling promotions.
- **URL**: Registered promotion endpoints.

### 7. Order History
- **Implementation**: API allows users to view past orders.
- **View**: `OrderViewSet` with a filter for historical orders.

### 8. Customizable Delivery Options
- **Implementation**: `instructions` field in `Order` model for special requests.

### 9. Customer Support Interface
- **Implementation**: Created `SupportTicket` model.
- **Model**: Tracks customer support requests.
- **Serializer**: `SupportTicketSerializer` for data handling.
- **View**: `SupportTicketViewSet` for API management.
- **URL**: Support ticket routes added.

### 10. Analytics for Restaurants
- **Implementation**: Added analytics endpoint in `RestaurantViewSet`.
- **View**: `analytics` action provides insights like total orders, revenue, and popular dishes.
- **URL**: API for restaurant insights.

## Installation and Setup
Step 1. Clone the repository:
   ```sh
   git clone https://github.com/paulosergioveras/Online-Food-Delivery-Service.git
   cd Online-Food-Delivery-Service
   ```

Step 2. Configure the Django Environment:
   ```sh
    python -m venv venv
    source venv/bin/activate  # on Windows use `.\venv\Scripts\activate`
   ```

Step 3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

Step 4. Apply makemigrations:
   ```sh
   python manage.py makemigrations
   ```

Step 5. Apply migrations:
   ```sh
   python manage.py migrate
   ```
Step 6. Run the server:
   ```sh
   python manage.py runserver
   ```
Step 7. API endpoints available at `http://localhost:8000/`
