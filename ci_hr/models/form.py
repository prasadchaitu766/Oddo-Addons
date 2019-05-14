from odoo import models, fields, api, _




class registration_form(models.Model):
	_name = 'hr.registration'

	name = fields.Char(string="Name")
	contact =  fields.Char(string="Contact")
	email = fields.Char(string="Email")

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

		
class transfer_date(models.Model):
	_name = 'hr.transfer'

	name = fields.Char(string="Name",readonly=True)
	contact =  fields.Char(string="Contact",readonly=True)
	email = fields.Char(string="Email",readonly=True)

	@api.multi
	def get_data(self):
		de=self.env['hr.registration'].search([])
		print self.id,"90000000000000000000000000000"
		dict_emp={}
		for y in de:
			if y.name==self.name:
				print y.id,"88888888888888888888888888888"
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


			
		


		

	

	





