from odoo import models, fields, api, _


class HRJobInherit(models.Model):
    _inherit = 'hr.job'
    
    company_name_inherit = fields.Many2one("company.recruitment", string="Company", required=True)
    company_location_inherit = fields.Char(string="Company Address", related="company_name_inherit.company_location")
    
    job_salary = fields.Char(string="Salary", required=True)
    job_salary_increase = fields.Char(string='Salary increase', required=True)
    job_bonus = fields.Char(string='Bonus per year', required=True)
    job_assumed_annual = fields.Char(string='Assumed annual', required=True)

    job_working_hour = fields.Char(string="Working hours", required=True)
    job_holiday = fields.Char(string="Holiday", required=True)
    job_average_overtime = fields.Char(string="Average overtime", required=True)
    job_overtime_salary = fields.Char(string="Overtime salary", required=True)

    job_trial_period = fields.Char(string="Trial period", required=True)
    job_trial_period_salary = fields.Char(string="Trial period salary", required=True)

    job_other_benefit = fields.Text("Other benefit", required=True)

    job_recruitment_ids = fields.Integer(string='Number', required=True)
    job_recruitment_type = fields.Char(string='Recruitment type', required=True)
    job_employment_type = fields.Char(string='Employment type', required=True)
    job_working_location = fields.Char(string='Working location', required=True) 
    job_application_period = fields.Date(string='Application period',default=fields.Date.today(), required=True)
    job_employment_period = fields.Char(string='Employment period', required=True)
    job_employment_age = fields.Integer(string='Age', required=True)
    job_joining_time = fields.Date(string='Joining time', required=True)
    job_soft_skill = fields.Text(string="Welcome soft-Skill", required=True)
    job_required_skill = fields.Text(string="Required Skill and experience", required=True)
    job_assume = fields.Text(string="Assumed career path after joining the company", required=True)

    


class CompanyRecruitment(models.Model):
    _name = "company.recruitment"
    _inherit = ['mail.thread']
    _description = "Company Recruitment"
    _rec_name = "company_name"

    company_name = fields.Char(string="Company", required=True, track_visibility='onchange')
    company_location = fields.Char(string="Company Address", required=True, track_visibility='onchange')
    company_phone = fields.Char(string='Phone number', required=True, track_visibility='onchange', size=12)
    company_note = fields.Html(string='Note')
    company_job_ids = fields.One2many('hr.job', 'company_name_inherit', string="Company Job", readonly=True)
    company_manager_ids = fields.One2many("company.manager", "manager_of_company", string="Company Manager")
    company_name_seq = fields.Char(string="Company ID", required=True, copy=False, readonly=True, index=True, default="New")

    @api.model
    def create(self, vals):
        if vals.get("company_name_seq", "New") == "New":
            vals["company_name_seq"] = self.env["ir.sequence"].next_by_code("company.name.sequence") or "New"
        result = super(CompanyRecruitment, self).create(vals)
        return result