# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
 

class hr_recruitment_test_inheritence(models.Model):
	_inherit = "hr.applicant"
	# _rec_name =""


	date=fields.Date(string="Interview-Date")
	interviewr_name=fields.Char(string="Interviewer_name")
	joining=fields.Date(string="Joining-Date")

	@api.multi
	def daily_report_employee(self):
		
		

		return{
		'type':'ir.actions.act_window',
		'name':"Daily Report",
		'view_mode':'tree,form',
		'res_model':"hr.daily_report",
		'domain':[('name','=',self.name)],	
			
		}

	@api.onchange('job_id')
	def onchange_job_id(self):

		if self.job_id:
			self.name = 'Application for the post of '+str(self.job_id.name)
			
	def _onchange_stage_id_internal(self, stage_id):
		# print self.stage_id.name,"0000000000000000000000000000000000"
		# print self.last_stage_id.name,"111111111111111111111111111111111111111"
		if self.stage_id.name != False and self.last_stage_id.name != False:
			template = self.env.ref('ci_hr.example_email_template')
			
			self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)
		
		if not stage_id:
			return {'value': {}}
		stage = self.env['hr.recruitment.stage'].browse(stage_id)
		if stage.fold:
			return {'value': {'date_closed': fields.datetime.now()}}
		return {'value': {'date_closed': False}}





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











	

