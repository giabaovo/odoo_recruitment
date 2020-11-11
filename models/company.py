from odoo import models, fields, api, _


class HRJobInherit(models.Model):
    _inherit = 'hr.job'
    
    company_name_inherit = fields.Many2one("company.recruitment", string="Company")
    company_location_inherit = fields.Char(string="Company Address", related="company_name_inherit.company_location")

    

class CompanyRecruitment(models.Model):
    _name = "company.recruitment"
    _inherit = ['mail.thread']
    _description = "Company Recruitment"
    _rec_name = "company_name"

    company_name = fields.Char(string="Company", required=True, track_visibility='onchange')
    company_location = fields.Char(string="Company Address", required=True, track_visibility='onchange')
    company_name_seq = fields.Char(string="Company ID", required=True, copy=False, readonly=True, index=True, default="New")

    @api.model
    def create(self, vals):
        if vals.get("company_name_seq", "New") == "New":
            vals["company_name_seq"] = self.env["ir.sequence"].next_by_code("company.name.sequence") or "New"
        result = super(CompanyRecruitment, self).create(vals)
        return result