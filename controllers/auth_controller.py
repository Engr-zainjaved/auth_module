from odoo import http
from odoo.http import request

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        session_id = kwargs.get('session_id')
        if not session_id:
            return request.redirect('/web/login')

        # Validate the session using Odoo's session store
        try:
            session = request.env['ir.session'].sudo().search([
                ('session_token', '=', session_id)
            ], limit=1)
            if session:
                # Bypass login by setting the session in cookies
                request.session.authenticate(request.db, session.login, session.session_token)
                return request.redirect('/web')
            else:
                return request.redirect('/web/login')
        except Exception as e:
            return request.redirect('/web/login')
