from odoo import api,models,fields,_



class ResPartner(models.Model):
    _inherit = 'hr.applicant'

    @api.multi
    def send_msg(self):
        return {'type': 'ir.actions.act_window',
                'name': _('Whatsapp Message'),
                'res_model': 'test.test',
                'target': 'new',
                'view_mode': 'form',
                'view_type': 'form',
                'context': {'default_user_id': self.id},
                }


class employee_list_config(models.TransientModel):
    _name = "hr.employees"


    employee_id = fields.Many2one('hr.job',string="Type Of Employees",required=True)


    @api.multi
    def generate_employee_list(self):
        
        employee_search=self.env['hr.applicant'].search([('job_id','=',self.employee_id.id)])
     
        return self.env["report"].get_action(employee_search,'ci_hr.report_employee_new')