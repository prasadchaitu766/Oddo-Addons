from odoo import models, fields, api, _




class registration_form(models.Model):
	_name = 'hr.registration'

	name = fields.Char(string="Name")
	contact =  fields.Char(string="Contact")
	email = fields.Char(string="Email")
	address = fields.Char(string="Address")
	address2 =fields.Char(string="Address2",store=True)
	same=fields.Boolean(string="click same address")


	@api.multi
	def transfer_information(self):
		de=self.env['hr.transfer'].search([])
			
		return{
		'type':'ir.actions.act_window',
		'name':"registaration",
		'view_mode':'form',
		'res_model':"hr.transfer",
		'context':{
		'default_name':self[0].name,
		'default_contact':self[0].contact,
		}


			
		}

	@api.onchange('same')
	def same_address(self):
		if self.same==True:
			self.address2=self.address


		
class transfer_date(models.Model):
	_name = 'hr.transfer'

	name = fields.Char(string="Name",readonly=True)
	contact =  fields.Char(string="Contact",readonly=True)
	email = fields.Char(string="Email",readonly=True)
	address = fields.Char(string="Address")
	same=fields.Boolean(string="click same address")

	@api.multi
	def get_data(self):
		de=self.env['hr.registration'].search([])
		dict_emp={}
		for y in de:
			if y.name==self.name:
				dict_emp=y.id		
		return{
		'type':'ir.actions.act_window',
		'name':"registaration",
		'view_mode':'form',
		'res_model':"hr.registration",
		'res_id':dict_emp,
		'target':'current',
		# 'context':{
		# 'default_name':self[0].name,
		# 'default_contact':self[0].contact,
		}
		
		# }


	

	

class Hr_Applicant_inherited(models.Model):
	_inherit = "hr.applicant"

	state = fields.Selection([('employee','Employee'),('resign','Resign'),('refuse','Refuse'),('draft','Draft'),('terminate', 'Terminate')],default="draft")

	@api.multi
	def employee_creation(self):
		self.write({'state':'employee'})

	@api.multi
	def employee_refue(self):
		self.write({'state':'refuse'})
	@api.multi
	def terminate_employee(self):
		self.write({'state':"terminate"})
	@api.multi
	def employee_resign(self):
		self.write({'state':'resign'})

	# @api.multi
	# def send_msg(self):
	# 	return {'type': 'ir.actions.act_window',
 #                'name': _('Whatsapp Message'),
 #                'res_model': 'test.test',
 #                'target': 'new',
 #                'view_mode': 'form',
 #                'view_type': 'form',
 #                'context': {'default_user_id': self.id},
 #                }






			
		


		

	

	





