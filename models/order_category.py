from odoo import models, fields, api

class OrderCategory(models.Model):
    _name = 'manufacturing.order.category'  # Set the name of the model
    _description = 'Order Category'  # Set the description of the model

    name = fields.Char(string='Name', required=True)  # Define a Char field for the name of the category
    description = fields.Text('Description')
    stage = fields.Selection([  # Define a Selection field for the stage of the category
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string='Stage', default='not_started')
    operator_id = fields.Many2one('res.users', string='Operator')  # Define a Many2one field for the operator of the category