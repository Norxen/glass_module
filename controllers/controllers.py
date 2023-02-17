# -*- coding: utf-8 -*-
# from odoo import http


# class GlassModule(http.Controller):
#     @http.route('/glass_module/glass_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/glass_module/glass_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('glass_module.listing', {
#             'root': '/glass_module/glass_module',
#             'objects': http.request.env['glass_module.glass_module'].search([]),
#         })

#     @http.route('/glass_module/glass_module/objects/<model("glass_module.glass_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('glass_module.object', {
#             'object': obj
#         })
