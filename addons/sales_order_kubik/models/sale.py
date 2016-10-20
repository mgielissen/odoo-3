from openerp import models, fields

class Sale(models.Model):
    _inherit = 'sale.order'
    batch = fields.Char(string = 'Batch',required = True)
    npwp = fields.Char(string="NPWP")
    type = fields.Selection([("Training","Training"),("Seminar","Seminar")],string="Type")
    order = fields.Selection([("First Order", "First Order"), ("Repeat Order", "Repeat Order")],string="Order")
    incoming = fields.Selection([("Incoming", "Incoming"), ("Non Incoming", "Non Incoming")],string="Incoming")
    date_from = fields.Date(string="Date From",required=True)
    date_to = fields.Date(string ="Date To",required=True)
    work_time_from = fields.Float("From Hour",required=True)
    work_time_to = fields.Float("To Hour",required=True)
    total_participant = fields.Integer("Total Participant",required=True)
    sale_trainer = fields.Char(string = "Trainer")
    sale_location = fields.Char(string = "Location")
    sale_information = fields.Char(string = "Information")
    sale_trr = fields.Char(string="TRR")
    sale_hr_contact_name = fields.Char(string="HR Contact Name")
    sale_hr_position = fields.Char(string="Position")
    sale_hr_phone = fields.Char(string="Phone")
    sale_hr_fax = fields.Char(string="Fax")
    sale_technical_contact_name = fields.Char(string="Technical Contact Name")
    sale_technical_position = fields.Char(string="Position")
    sale_technical_phone = fields.Char(string="Phone")
    sale_technical_fax = fields.Char(string="Fax")
    sale_accounting_contact_name = fields.Char(string="Accounting Contact Name")
    sale_accounting_position = fields.Char(string="Position")
    sale_accounting_phone = fields.Char(string="Phone")
    sale_accounting_fax = fields.Char(string="Fax")