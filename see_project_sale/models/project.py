# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

# class Project(models.Model):
#     _inherit = 'project.project'
#
#     sale_order_ids = fields.One2many('sale.order','projects_id',string='Sale order')

class ProjectTask(models.Model):
    _inherit = 'project.task'

    # sale_order_ids = fields.Many2one('sale.order',string="Sale order")
    # sale_order_ids = fields.Many2many('sale.order',string="Sale order")

    sale_order_ids = fields.Many2many('sale.order',
      'task_sale_rel',
      'task_id',
      'sale_order_id',
      'Sale(s) order(s)'
    )
