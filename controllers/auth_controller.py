import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)  # Initialize logger

class AuthController(http.Controller):

    @http.route('/auth/bypass', type='http', auth='none', methods=['GET'])
    def auth_bypass(self, **kwargs):
        session_id = kwargs.get('session_id')
        _logger.info("Auth bypass attempt. Received session_id: %s", session_id)

        if not session_id:
            _logger.warning("No session_id provided. Redirecting to login page.")
            return request.redirect('/web/login')

        # Manually set the session in Odoo
        request.session.authenticate(request.session.db, session_id, '')

        # Log session info
        _logger.info("Session authenticated successfully.")

        # Set session cookie in response
        response = request.redirect('/web')
        response.set_cookie('session_id', session_id, httponly=True, samesite='Lax')

        _logger.info("Session ID cookie set, redirecting to /web")
        return response
