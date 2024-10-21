# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line')
    def _compute_website_order_line(self):
        """Override to ensure discounted prices are applied in the website cart."""
        for order in self:
            # Filter order lines to show in cart
            order.website_order_line = order.order_line.filtered(lambda l: l._show_in_cart())

            # Apply the discounted price to products with discounts
            for line in order.website_order_line:
                if line.product_id.discount_percentage > 0:
                    line.price_unit = line.product_id.discounted_price