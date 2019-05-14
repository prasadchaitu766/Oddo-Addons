# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
 

class hr_recruitment_test_inheritence(models.Model):
	_inherit = "hr.applicant"

	@api.multi
	def daily_report_employee(self):
		

		return{
		'type':'ir.actions.act_window',
		'name':"Daily Report",
		'view_mode':'tree,form',
		'res_model':"hr.daily_report",
		'domain':[('name','=',self.name)],	
			
		}


class Daily_Report(models.Model):
	_name = "hr.daily_report"


	name = fields.Char(string="Employee-Name")
	Manager_name = fields.Char(string="Manager-name")
	date=fields.Date(string="Date-Of Report")
	task = fields.One2many('hr.daily_task','report',string="Task")


class daily_task(models.Model):
	_name = 'hr.daily_task'

	task_no = fields.Integer(string="Task-No")
	des = fields.Char(string="Decription")
	planned_date = fields.Date(string="Planned-Date")
	estimated_date = fields.Date(string="Estimated-date")
	status = fields.Char(string="Status")
	report = fields.Many2one('hr.daily_report')











	

