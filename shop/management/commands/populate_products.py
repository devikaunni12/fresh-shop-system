from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Populate the database with sample products'

    def handle(self, *args, **options):
        # Sample products data
        products_data = [
            {
                'name': 'Fresh Organic Apples',
                'description': 'Crisp, juicy organic apples picked fresh from local orchards. Perfect for snacking or baking.',
                'price': 3.99,
            },
            {
                'name': 'Farm Fresh Milk',
                'description': 'Whole milk from grass-fed cows. Rich in nutrients and delicious taste.',
                'price': 4.49,
            },
            {
                'name': 'Organic Bananas',
                'description': 'Sweet and ripe organic bananas. Great source of potassium and energy.',
                'price': 2.99,
            },
            {
                'name': 'Free-Range Eggs',
                'description': 'Farm fresh eggs from free-range chickens. Perfect for breakfast or baking.',
                'price': 5.99,
            },
            {
                'name': 'Whole Wheat Bread',
                'description': 'Freshly baked whole wheat bread made with organic grains. Healthy and delicious.',
                'price': 3.49,
            },
            {
                'name': 'Organic Strawberries',
                'description': 'Sweet and juicy organic strawberries. Perfect for desserts or smoothies.',
                'price': 4.99,
            },
            {
                'name': 'Greek Yogurt',
                'description': 'Creamy Greek yogurt made from fresh milk. High in protein and probiotics.',
                'price': 4.29,
            },
            {
                'name': 'Fresh Salmon Fillet',
                'description': 'Wild-caught salmon fillet. Rich in omega-3 fatty acids and perfect for grilling.',
                'price': 12.99,
            },
            {
                'name': 'Organic Spinach',
                'description': 'Fresh organic spinach leaves. Nutrient-rich and perfect for salads or cooking.',
                'price': 2.49,
            },
            {
                'name': 'Avocado',
                'description': 'Ripe and creamy avocados. Great for guacamole or as a healthy fat source.',
                'price': 1.99,
            },
            {
                'name': 'Brown Rice',
                'description': 'Organic brown rice. Nutritious and versatile grain for healthy meals.',
                'price': 3.79,
            },
            {
                'name': 'Almond Butter',
                'description': 'Natural almond butter made from roasted almonds. Perfect spread for toast or smoothies.',
                'price': 6.99,
            },
        ]

        # Create products
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created product: {product.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {len(products_data)} products')
        )
