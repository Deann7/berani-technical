# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CourierCustomer(models.Model):
    """Model to represent customers in the courier system"""
    _name = 'courier.customer'
    _description = 'Courier Customer'
    _order = 'name'

    name = fields.Char(
        string='Customer Name',
        required=True,
        index=True,
        help='Full name of the customer'
    )
    
    phone = fields.Char(
        string='Phone Number',
        help='Contact phone number'
    )
    
    email = fields.Char(
        string='Email',
        help='Email address'
    )
    
    address = fields.Text(
        string='Address',
        help='Full address of the customer'
    )
    
    incident_ids = fields.One2many(
        comodel_name='courier.incident',
        inverse_name='customer_id',
        string='Incidents',
        help='Related incidents for this customer'
    )
    
    incident_count = fields.Integer(
        string='Incident Count',
        compute='_compute_incident_count',
        store=True
    )
    
    @api.depends('incident_ids')
    def _compute_incident_count(self):
        """Compute the total number of incidents for this customer"""
        for record in self:
            record.incident_count = len(record.incident_ids)
    
    _sql_constraints = [
        ('unique_customer_email', 'UNIQUE(email)', 'Email must be unique!'),
    ]
