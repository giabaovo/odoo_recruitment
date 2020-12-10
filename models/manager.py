from odoo import models, fields, api, _


class Manager(models.Model):
    _name = 'company.manager'
    _inherit = ['mail.thread']
    _description = "Manager Recruitment"
    _rec_name = "manager_name"

    manager_name = fields.Char(string='Name', required=True, track_visibility='onchange', help="Please fill manager's name")
    manager_phone = fields.Char(string='Phone', required=True, track_visibility='onchange', size=12, help="Please fill manager's phone number")
    manager_email = fields.Char(string='Email', required=True, track_visibility='onchange', help="Please fill manager's email")
    manager_of_company = fields.Many2one("company.recruitment", string='Company', ondelete='cascade') 
    manager_name_seq = fields.Char(string="Manager ID", required=True, copy=False, readonly=True, index=True, default="New")

    @api.model
    def create(self, vals):
        if vals.get("manager_name_seq", "New") == "New":
            vals["manager_name_seq"] = self.env["ir.sequence"].next_by_code("manager.name.sequence") or "New"
        result = super(Manager, self).create(vals)
        return result