# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CourierIncident(models.Model):
    """Model to manage courier operational incidents"""
    _name = 'courier.incident'
    _description = 'Courier Incident Log'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'incident_datetime desc, id desc'

    name = fields.Char(
        string='Judul Insiden',
        required=True,
        tracking=True,
        help='Brief title describing the incident'
    )
    
    
    customer_id = fields.Char(
        string='Pelanggan',
        required=True,
        tracking=True,
        help='Customer name related to this incident'
    )
    
    shipment_id = fields.Char(
        string='No. Resi',
        tracking=True,
        help='Shipment/tracking number related to this incident (if applicable)'
    )
    
    incident_type = fields.Selection(
        selection=[
            ('package_damage', 'Kerusakan Paket'),
            ('delivery_delay', 'Keterlambatan Pengiriman'),
            ('package_lost', 'Paket Hilang'),
            ('courier_health', 'Masalah Kesehatan Kurir'),
            ('accident', 'Kecelakaan'),
            ('other', 'Lainnya'),
        ],
        string='Tipe Insiden',
        default='other',
        required=True,
        tracking=True,
        help='Type of incident'
    )
    
    incident_datetime = fields.Datetime(
        string='Waktu',
        required=True,
        default=fields.Datetime.now,
        tracking=True,
        help='Date and time when the incident occurred'
    )
    
    severity = fields.Selection(
        selection=[
            ('low', 'Rendah'),
            ('medium', 'Sedang'),
            ('high', 'Tinggi'),
            ('critical', 'Kritis'),
        ],
        string='Urgensi',
        default='low',
        required=True,
        tracking=True,
        help='Urgency level of the incident'
    )
    
    description = fields.Text(
        string='Kronologi',
        help='Detailed description of what happened'
    )
    
    followup_note = fields.Text(
        string='Catatan',
        tracking=True,
        help='Follow-up actions taken to resolve the incident'
    )
    
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('followup', 'Follow-up'),
            ('done', 'Done'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        help='Current state of the incident'
    )
    
    resolved_at = fields.Datetime(
        string='Selesai pada',
        readonly=True,
        tracking=True,
        help='Date and time when the incident was resolved'
    )
    
    color = fields.Integer(
        string='Color Index',
        default=0,
        help='Color for kanban view'
    )
    
    # Button Actions
    def action_mark_followup(self):
        """Change state to follow-up"""
        for record in self:
            record.state = 'followup'
    
    def action_resolve(self):
        """Change state to done and set resolved_at timestamp"""
        for record in self:
            record.write({
                'state': 'done',
                'resolved_at': fields.Datetime.now(),
            })
    
    def action_reset_to_draft(self):
        """Reset incident back to draft state"""
        for record in self:
            record.write({
                'state': 'draft',
                'resolved_at': False,
            })
    
    # Python Validation (Optional Challenge)
    @api.constrains('state', 'followup_note')
    def _check_followup_note_required(self):
        """Ensure followup_note is filled when state is 'done'"""
        for record in self:
            if record.state == 'done' and not record.followup_note:
                raise ValidationError(
                    'Catatan tindak lanjut wajib diisi sebelum menyelesaikan insiden!'
                )
