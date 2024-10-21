{
    'name': 'E-commerce Product Discount',
    'version': '1.0',
    'summary': 'Apply and display discounts on eCommerce products',
    'description': """
Product Discount Feature for E-commerce (Odoo 17)
-------------------------------------------------

This module allows eCommerce products to have discounts applied, and ensures the discounted price is correctly reflected in the cart, checkout, and invoices.

### Features:
- Discount percentage field for products
- Automatic calculation of discounted price
- Display original and discounted prices on the product page with strikethrough for original price
- Apply discounts in the cart, checkout, and final invoice

### Testing Steps:

1. **Create or Edit a Product**:
   - Navigate to Products menu.
   - Create a new product or open an existing product.
   - In the form view, set the **Sales Price** and specify a **Discount Percentage** in the newly added field.

2. **Verify Discounted Price**:
   - Once the discount percentage is set, ensure the **Discounted Price** field is automatically calculated and shown next to the Sales Price field.

3. **Check Frontend (Website)**:
   - Go to the eCommerce website and find the product.
   - Verify that the product page displays the original price (with strikethrough) and the discounted price next to it.

4. **Add Product to Cart**:
   - Add the product to the cart.
   - Confirm that the cart reflects the discounted price instead of the original price.

5. **Checkout Process**:
   - Proceed to the checkout page.
   - Ensure that the discounted price is applied during the checkout process.

6. **Verify Final Invoice**:
   - Once the order is confirmed, navigate to Sales > Orders and find the corresponding sale order.
   - Check that the **invoice** reflects the discounted price.

7. **Edge Case Testing**:
   - Set a 0% discount and ensure the full price is displayed.
   - Test with different combinations of product variants to ensure the discount applies correctly.
   - Test with multiple discounts across different products in the same cart.

8. **No Discount Scenario**:
   - When no discount is applied (0% discount), ensure the original price is shown without any strikethrough or discounted price.
   
<strong>Screenshots:</strong><br />
    <img src="/product_discount/static/description/screenshot_1.png" /><br />
    <img src="/product_discount/static/description/screenshot_2.png" /><br />
    <img src="/product_discount/static/description/screenshot_3.png" /><br />
    <img src="/product_discount/static/description/screenshot_4.png" /><br />
    <img src="/product_discount/static/description/screenshot_5.png" /><br />
    <img src="/product_discount/static/description/screenshot_6.png" /><br />
    <img src="/product_discount/static/description/screenshot_7.png" /><br />
""",
    'author': 'Praveen Kumar G',
    'category': 'E-commerce',
    'depends': ['product', 'website_sale'],
    'data': [
        'views/product_views.xml',
        'views/templates.xml',
    ],
    'images': [
        'static/description/screenshot_1.png',
        'static/description/screenshot_2.png',
        'static/description/screenshot_3.png',
        'static/description/screenshot_4.png',
        'static/description/screenshot_5.png',
        'static/description/screenshot_6.png',
        'static/description/screenshot_7.png',
    ],
    'installable': True,
    'application': False,
}
