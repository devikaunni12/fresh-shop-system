# FreshShop

FreshShop is a Django-based e-commerce application that allows users to browse products, add them to a cart, and complete checkout. It features user authentication, product management via admin interface, and search functionality.

## Features

- **Product Management**: Add, view, and manage products with images, names, descriptions, and prices.
- **User Authentication**: Login and registration using Django's built-in User model.
- **Shopping Cart**: Add products to cart, view cart, and remove items.
- **Checkout**: Review cart items and place orders.
- **Pagination**: Paginated product listing.
- **Search**: Search products by name or description.
- **Admin Interface**: Manage products and users via Django admin.

## Setup Instructions

1. **Clone or Extract the Project**:
   - Extract the zip file to your desired directory.

2. **Create Virtual Environment**:
   - Navigate to the project directory.
   - Run `python -m venv myvenv` (or use the existing myvenv).

3. **Activate Virtual Environment**:
   - On Windows: `myvenv\Scripts\activate`
   - On macOS/Linux: `source myvenv/bin/activate`

4. **Install Dependencies**:
   - Run `pip install -r requirements.txt`

5. **Database Migration**:
   - Run `python manage.py makemigrations`
   - Run `python manage.py migrate`

6. **Create Superuser**:
   - Run `python manage.py createsuperuser`
   - Follow the prompts to create an admin user.

7. **Run the Server**:
   - Run `python manage.py runserver`
   - Access the application at `http://127.0.0.1:8000/`
   - Access admin at `http://127.0.0.1:8000/admin/`

## Usage

- **Browse Products**: Visit the home page to view products.
- **Search**: Use the search bar to find products.
- **Add to Cart**: Login and add products to your cart.
- **Checkout**: Review your cart and place an order.
- **Admin**: Use the admin interface to add products.

## Project Structure

- `FreshShop/`: Main Django project settings.
- `shop/`: App containing models, views, templates, and URLs.
- `templates/shop/`: HTML templates for the application.
- `media/`: Directory for uploaded product images.
- `db.sqlite3`: SQLite database file.

## Technologies Used

- Django 5.0.1
- Pillow 12.1.0 (for image handling)
- Bootstrap 5 (for styling)
