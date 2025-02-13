from odoo import http
from odoo.http import request

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        session_id = kwargs.get('session_id')
        if not session_id:
            return request.redirect('/web/login')

        # Set the session ID in the cookies
        response = request.redirect('/web')
        response.set_cookie('session_id', session_id, httponly=True, samesite='Lax')  # Securely setting the session ID in cookies
        
        return response
