# Courier Core - Incident Log System

## Deskripsi

Modul Odoo 18 untuk sistem pencatatan dan pengelolaan insiden operasional BeraniExpress. Sistem ini membantu tim operasional mencatat dan menindaklanjuti berbagai kendala seperti keterlambatan pengiriman, barang hilang, atau masalah kesehatan kurir.

## Struktur Modul

```
courier_core/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── courier_customer.py      # Model pelanggan
│   ├── courier_shipment.py      # Model pengiriman/resi
│   └── courier_incident.py      # Model insiden (UTAMA)
├── views/
│   └── courier_incident_views.xml
├── security/
│   └── ir.model.access.csv
└── README.md
```

## Instalasi

### Prasyarat

- Odoo 18.0 terinstal
- Python 3.10+
- PostgreSQL

## Teknologi

- **Platform**: Odoo 18.0
- **Bahasa**: Python 3.10+
- **Framework**: Odoo ORM
- **Database**: PostgreSQL

## Lisensi

LGPL-3

## Author

Deandro Najwan Ahmad Syahbanna

## Referensi

- [Odoo 18 Documentation](https://www.odoo.com/documentation/18.0/)
- [Odoo ORM API](https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html)
- [Odoo Views](https://www.odoo.com/documentation/18.0/developer/reference/backend/views.html)
