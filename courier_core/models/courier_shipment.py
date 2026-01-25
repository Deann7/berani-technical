# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CourierShipment(models.Model):
    """Model to represent shipments/tracking numbers in the courier system"""
    _name = 'courier.shipment'
    _description = 'Courier Shipment'
    _order = 'create_date desc'

    name = fields.Char(
        string='Tracking Number',
        required=True,
        index=True,
        copy=False,
        help='Unique tracking/resi number for the shipment'
    )
    
    customer_id = fields.Many2one(
        comodel_name='courier.customer',
        string='Customer',
        required=True,
        ondelete='restrict',
        help='Customer who owns this shipment'
    )
    
    origin = fields.Char(
        string='Origin',
        help='Pickup location'
    )
    
    destination = fields.Char(
        string='Destination',
        help='Delivery location'
    )
    
    shipment_date = fields.Date(
        string='Shipment Date',
        default=fields.Date.context_today,
        help='Date when the shipment was created'
    )
    
    status = fields.Selection(
        selection=[
            ('pending', 'Pending'),
            ('in_transit', 'In Transit'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='pending',
        required=True,
        help='Current status of the shipment'
    )
    
    incident_ids = fields.One2many(
        comodel_name='courier.incident',
        inverse_name='shipment_id',
        string='Incidents',
        help='Related incidents for this shipment'
    )
    
    incident_count = fields.Integer(
        string='Incident Count',
        compute='_compute_incident_count',
        store=True
    )
    
    @api.depends('incident_ids')
    def _compute_incident_count(self):
        """Compute the total number of incidents for this shipment"""
        for record in self:
            record.incident_count = len(record.incident_ids)
    
    _sql_constraints = [
        ('unique_tracking_number', 'UNIQUE(name)', 'Tracking number must be unique!'),
    ]
