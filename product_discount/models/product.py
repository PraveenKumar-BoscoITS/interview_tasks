# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float(string="Discount Percentage", default=0.0, help="Set the discount percentage for the product")
    discounted_price = fields.Float(string="Discounted Price", compute="_compute_discounted_price", store=True)

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        """Compute the discounted price based on the discount percentage."""
        for product in self:
            # Validate discount percentage
            if product.discount_percentage < 0 or product.discount_percentage > 100:
                raise ValidationError("Discount Percentage must be between 0 and 100.")

            # Compute discounted price
            discount_amount = (product.discount_percentage / 100) * product.list_price
            product.discounted_price = product.list_price - discount_amount if product.discount_percentage > 0 else product.list_price

    def _get_sales_prices(self, pricelist, fiscal_position):
        """Extend to include discount percentage and discounted price."""
        # Call the original method to get the default prices
        prices = super(ProductTemplate, self)._get_sales_prices(pricelist, fiscal_position)

        # Loop through each price entry and modify with discount information
        for product_id, price_info in prices.items():
            product = self.browse(product_id)
            discount_percentage = product.discount_percentage or 0.0  # Ensure fallback to 0
            discounted_price = price_info['price_reduce'] * (1 - discount_percentage / 100)

            # Update the price dictionary with discount details
            price_info.update({
                'discount_percentage': discount_percentage,
                'discounted_price': discounted_price,
            })

        return prices

    def _get_additionnal_combination_info(self, product_or_template, quantity, date, website):
        """Modify combination info to use the discounted price."""
        combination_info = super(ProductTemplate, self)._get_additionnal_combination_info(
            product_or_template, quantity, date, website
        )
        # Update the price to reflect the discounted price
        combination_info['price'] = product_or_template.discounted_price
        return combination_info
