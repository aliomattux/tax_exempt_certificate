from openerp.osv import osv, fields


class ResPartner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
	'certificate_filename': fields.char('Certificate'),
	'exempt_certificate': fields.binary('Exempt Certificate'),
	'valid_from': fields.date('Valid From'),
	'valid_to': fields.date('Valid To'),
    }
