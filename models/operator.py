from odoo import models, fields, api

class Operator(models.Model):
    _inherit = 'res.users'  # Inherit from the Odoo res.users model
    order_category_ids = fields.One2many('manufacturing.order.category', 'operator_id', string='Order Categories')