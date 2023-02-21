# -*- coding: utf-8 -*-
{
    'name': "Manufacturing",
    'version': '1.0',
    'summary': "Manage order easily",  # Module subtitle phrase

    'description': 'This module provides functionality for managing manufacturing orders and categories.',

    'author': "Kilian e Iván",
    'website': "http://www.thisisnotarealdomainacceptit.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/order_category_view.xml",
        "views/order_view.xml"
    ],

    'installable': True,
    'auto_install': False,
    'application': True

    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}