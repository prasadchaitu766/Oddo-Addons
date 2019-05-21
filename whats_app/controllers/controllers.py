# -*- coding: utf-8 -*-
from odoo import http

# class WhatsApp(http.Controller):
#     @http.route('/whats_app/whats_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/whats_app/whats_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('whats_app.listing', {
#             'root': '/whats_app/whats_app',
#             'objects': http.request.env['whats_app.whats_app'].search([]),
#         })

#     @http.route('/whats_app/whats_app/objects/<model("whats_app.whats_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('whats_app.object', {
#             'object': obj
#         })