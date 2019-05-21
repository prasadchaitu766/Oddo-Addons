# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # projects_id = fields.Many2one('project.project',string="Project")

    # task_id = fields.Many2one('project.task',string="Task")
    # task_ids = fields.Many2many('project.task','sale_order_ids',string="Task")

    # hr.skill
    #   employee_ids = fields.Many2many(
    #     'hr.employee',
    #     'skill_employee_rel',
    #     'skill_id',
    #     'employee_id',
    #     'Employee(s)'
    #   )

    # hr.employee'
    #     skill_ids = fields.Many2many(
    #       'hr.skill',
    #       'skill_employee_rel',
    #       'employee_id',
    #       'skill_id',
    #       'Skills',
    #     )

    # sale.order
    task_ids = fields.Many2many(
        'project.task',
        'task_sale_rel',
        'sale_order_id',
        'task_id',
        'Task(s)')

    # @api.onchange('task_id')
    # def onchange_task_id(self):
    #     if self.task_id:
    #           # first try this if it work
    #           self._origin.task_id.sale_order_id = self.id
    #
    #           # if not working then you need to fetch the recorod
    #           # from the database first.
    #           task = self.env['project.task'].search[('id', '=', self.task_id.id)]
    #
    #           task.sale_order_id = self.id
