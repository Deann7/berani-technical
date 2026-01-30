# Penjelasan Project - Courier Incident Management System

Dokumentasi ini menjelaskan secara teknis mengenai modul `courier_core` yang dikembangkan untuk pengelolaan insiden operasional pada BeraniExpress.

## 1. Struktur Kode & Model Data

Model utama dalam sistem ini adalah `courier.incident`. Model ini dirancang untuk mencatat setiap kejadian luar biasa dalam operasional pengiriman.

### Keterkaitan Data:

- **Pelanggan (`customer_id`)**: Dalam demo teknis ini, field ini menggunakan tipe data `Char`. Hal ini dipilih untuk mempermudah input manual nama pelanggan tanpa harus bergantung pada data master partner terlebih dahulu. Pada implementasi skala besar, field ini dapat dikonversi menjadi `Many2one` ke `res.partner`.
- **Nomor Resi (`shipment_id`)**: Field ini menyimpan identitas unik transaksi atau paket. Menggunakan tipe `Char` agar fleksibel dalam menerima format nomor resi dari berbagai ekspedisi mitra.
- **Tipe & Urgensi**: Menggunakan `Selection` field untuk standarisasi kategori data (misal: Kerusakan Paket, Kecelakaan) dan tingkat prioritas (Low sampai Critical).

![Courier Incident Screenshot](assets/courier%20incident.png)

---

## 2. Alur Kerja Fitur (Workflow)

Sistem menggunakan _State Machine_ yang cukup clear untuk melacak progress penanganan insiden:

1.  **Log Baru (Draft)**:
    - Status awal saat insiden pertama kali dicatat.
    - Fokus pada pengumpulan data kronologi (`description`).
2.  **Proses Penanganan (Follow-up)**:
    - User menekan tombol **"Tandai Follow-up"**.
    - Tim operasional mulai mengambil tindakan perbaikan atau investigasi.
3.  **Penyelesaian (Done)**:
    - User menekan tombol **"Selesaikan Insiden"**.
    - Sistem akan melakukan validasi akhir dan mencatat waktu penyelesaian secara otomatis.

![alur kerja Screenshot](assets/alur%20kerja.png)

## 3. Logic & Constraint (Python Backend)

Untuk python backendnya sebagai berikut:

### A. Otomatisasi Waktu Penyelesaian

Fungsi `action_resolve` bertanggung jawab mengubah status sekaligus mengisi timestamp.

```python
def action_resolve(self):
    for record in self:
        record.write({
            'state': 'done',
            'resolved_at': fields.Datetime.now(), # Mengisi waktu real-time
        })
```

### B. Validasi Catatan (Constraint)

Untuk memastikan setiap insiden yang selesai memiliki rekam jejak solusi, kami menerapkan `@api.constrains`. Logika ini mencegah insiden ditutup jika `followup_note` (Catatan Tindak Lanjut) masih kosong.

```python
@api.constrains('state', 'followup_note')
def _check_followup_note_required(self):
    for record in self:
        if record.state == 'done' and not record.followup_note:
            raise ValidationError(
                'Catatan tindak lanjut wajib diisi sebelum menyelesaikan insiden!'
            )
```

### C. Logic Tombol Status

- **Visibility**: Tombol di header form (XML) diatur agar muncul secara kontekstual menggunakan atribut `invisible`. Misalnya, tombol "Selesaikan" hanya muncul jika status saat ini adalah `followup`.
- **State Reset**: Fungsi `action_reset_to_draft` memungkinkan pemulihan data jika terjadi kesalahan input, sekaligus menghapus nilai `resolved_at` yang sebelumnya terisi.

---

## 4. Visualisasi Integritas Data

Berikut ini visualisasi integritas datanya pakai sequence diagram:

![Sequence Diagram](assets/sequence%20diagram.png)
