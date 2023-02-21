from odoo import models, fields, api

class Order(models.Model):
    _name = 'manufacturing.order'  # Set the name of the model
    _description = 'Manufacturing Order'  # Set the description of the model

    name = fields.Char(string='Name', required=True) 
    manufacturing_date = fields.Date(string='Manufacturing Date', required=True)  # Define a Date field for the manufacturing date
    shipping_date = fields.Date(string='Shipping Date', required=True)  # Define a Date field for the shipping date
    order_date = fields.Date(string='Order Date', required=True)  # Define a Date field for the order date
    product_width = fields.Float(string='Product Width')
    product_height = fields.Float(string='Product Height')
    order_category_id = fields.Many2one('manufacturing.order.category', string='Order Category')  # Define a Many2one field for the category of the order