# -*- coding: utf-8 -*-
from odoo import http

# class CiHr(http.Controller):
#     @http.route('/ci_hr/ci_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ci_hr/ci_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ci_hr.listing', {
#             'root': '/ci_hr/ci_hr',
#             'objects': http.request.env['ci_hr.ci_hr'].search([]),
#         })

#     @http.route('/ci_hr/ci_hr/objects/<model("ci_hr.ci_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ci_hr.object', {
#             'object': obj
#         })