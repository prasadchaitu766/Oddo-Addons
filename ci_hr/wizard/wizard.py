from odoo import models, api, fields


class WhatsappSendMessage(models.TransientModel):

    _name = 'test.test'
    

    # user_id = fields.Many2one('res.partner', string="Recipient")
    # mobile = fields.Char(related='user_id.mobile', required=True)
    # message = fields.Text(string="message", required=True)
    user_id = fields.Many2one('hr.applicant',string="employee")
    mobile= fields.Char(related='user_id.partner_mobile',required=True)
    message = fields.Text(string="message", required=True)
    image = fields.Binary(string="Image")
    # testing = fields.Char(string="Testing")

    def send_message(self):
        print self.image,"1111111111111111111111111111111"
       
        if self.message and self.mobile:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
               
            message_string = message_string[:(len(message_string) - 3)]
            
            return {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone=" +self.user_id.partner_mobile+"&text=" + message_string+self.image,
                'target': 'new',
                'res_id': self.id,

            }

# class inherit_message(models.TransientModel):
#     _inherit = "test.test"

#     testing = fields.Char(string="Testing")



