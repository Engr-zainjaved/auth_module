from odoo import http
from odoo.http import request

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        session_id = kwargs.get('session_id')
        if not session_id:
            return request.redirect('/web/login')

        # Manually load the session using session ID
        session_store = request.session.session_store
        session = session_store.get(session_id)

        if not session:
            return request.redirect('/web/login')  # If session ID is invalid, redirect to login

        # Restore the session
        request.session.update(session)
        request.session.sid = session_id  # Ensure Odoo uses this session

        # Redirect to /web as an authenticated user
        return request.redirect('/web')
