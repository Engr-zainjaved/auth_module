from odoo import http
from odoo.http import request

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        session_id = kwargs.get('session_id')
        if not session_id:
            return request.redirect('/web/login')

        # Set session ID directly in cookies
        request.session.session_token = session_id
        return request.redirect('/web')
