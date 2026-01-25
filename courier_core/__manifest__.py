# -*- coding: utf-8 -*-
{
    'name': 'Courier Core - Incident Log System - Deandro Najwan Ahmad Syahbanna',
    'version': '18.0.1.0.0',
    'category': 'Operations/Logistics',
    'summary': 'Incident management system for BeraniExpress courier operations',
    'description': """
        Courier Incident Log System
        ============================
        This module provides a comprehensive incident logging and tracking system
        for BeraniExpress courier operations. It helps manage operational issues
        such as package damage, delivery delays, and courier health concerns.
        
        Key Features:
        * Record and track incidents with detailed information
        * Manage incident workflow (Draft → Follow-up → Done)
        * Link incidents to customers and shipments
        * Categorize incidents by type and severity
        * Track resolution timeline
    """,
    'author': 'Deandro Najwan Ahmad Syahbanna',
    'website': 'https://deandronajwan.vercel.app',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/courier_incident_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
