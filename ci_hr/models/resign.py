from odoo import fields,api,models,_
from odoo.exceptions import UserError






class resign_form(models.Model):
	_name = 'hr.resign'
	_inherit = ['mail.thread','ir.needaction_mixin']
	_rec_name = "employee_id"

	# def _get_employee_id(self):
		# assigning the related employee of the logged in user
		# print self.env.uid,"000000000000000000000000000000000000000000000"
		# employee_rec = self.env['hr.applicant'].search([('user_id', '=', self.env.uid)], limit=1)
		# print employee_rec.id,"1111111111111111111111111111111111111"
		# return employee_rec.id
	

	name = fields.Char(string="Sequence No", required=True, Index= True, default=lambda self:('New'), readonly=True)
	employee_id = fields.Many2one('hr.applicant',string="Employee-Name",required=True)
	department = fields.Many2one('hr.department',string="Department",required=True)
	joining_date = fields.Date(string="Joining-date",required=True)
	releaving_date= fields.Date(string="Releaving-date",required=True)
	reason = fields.Text(string="Reason",required=True)
	state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('hr-approve','Hr-Approve'),('ceo_approve','CEO_Approve'),('employee-closed','Employee-Closed'),('reject','Reject')],default='draft')
	#state = fields.Selection([('draft','Draft'),('confirm','Confirm')('approved','Approved'),('hr-approve','Hr-Approve'),('reject','Reject'),],default="draft")
	hr_approve_date = fields.Datetime(string="HR-Approved-date",readonly=True)
	ceo_approve_date = fields.Datetime(string="CEO-Approved-date",readonly=True)
	closed_application = fields.Datetime(string="Closed-Employee",readonly=True)
	employee = fields.Boolean('Active',default=True)

	@api.multi
	def confirm_resign(self):
		if not self.joining_date<=self.releaving_date:
			raise UserError(_("releaving_date must be more than joining_date"))
		self.write({'state':'confirm'})


	@api.multi
	def approve_resign(self):

		self.write({'state':'hr-approve',
			'hr_approve_date':fields.datetime.now()})

		

	@api.multi
	def reject_resign(self):
		self.write({'state':'reject'})

	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('bi.employee.salary') or _('New')
			result = super(resign_form, self).create(vals)
			return result


			


	# @api.multi
	# def CEO_approvals(self):
	# 	# self.write({'state':'ceo_approve',
	# 	# 	'ceo_approve_date':fields.datetime.now()})
		
	# 	template1 = self.env.ref('ci_hr.hr_approval_mail')
	# 	# You can also find the e-mail template like this:
	# 	# template = self.env['ir.model.data'].get_object('mail_template_demo', 'example_email_template')
 
	# 	# Send out the e-mail template to the user
	# 	self.env['mail.template'].browse(template1.id).send_mail(self.id)
		
	

	# @api.multi
	# def mail_sending_template(self):
	# 	print "999999999999999999999999999999999999999999999"
	# 	template = self.env.ref('ci_hr.hr_approval_mail')

	# 	self.env['mail.template'].browse(template.id).send_mail(self.id,force_send=True)


	@api.multi
	def ceo_state_method(self):
		template1 = self.env.ref('ci_hr.test_email_send')
		
		self.env['mail.template'].browse(template1.id).send_mail(self.id,force_send=True)
	
		self.write({'state':'ceo_approve',
			'ceo_approve_date':fields.datetime.now()})
	


	@api.multi
	def closed_employees(self):
		self.write({'state':'employee-closed',
			'closed_application':fields.datetime.now()})
		# template1 = self.env.ref('ci_hr.test_email_send')
		
		# self.env['mail.template'].browse(template1.id).send_mail(self.id,force_send=True)


	@api.onchange('employee_id')
	def employee_joining_date(self):
		ddt=self.env['hr.applicant'].search([])
		for x in ddt:
			if self.employee_id.name == x.name:
				self.joining_date=x.joining
