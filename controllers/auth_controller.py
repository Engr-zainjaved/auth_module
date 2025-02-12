from odoo import http
from odoo.http import request, root

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        # Extract session_id from URL parameters
        session_id = kwargs.get('session_id')
        if not session_id:
            return request.redirect('/web/login')  # Redirect to login if no session_id

        # Validate the session using Odoo's session store
        session_store = root.session_store
        session = session_store.get(session_id)
        
        if session and session.uid:
            # Session is valid: Set cookie and redirect to Odoo interface
            response = request.redirect('/web')
            response.set_cookie('session_id', session_id, httponly=True)
            return response
        else:
            # Invalid session: Redirect to login
            return request.redirect('/web/login')
