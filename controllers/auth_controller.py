from odoo import http
from odoo.http import request

class AutoLogin(http.Controller):
    @http.route('/web/login', type='http', auth='none', csrf=False)
    def auto_login(self, **kwargs):
        session_id = request.httprequest.args.get('session_id')
        if session_id:
            request.session.session_token = session_id
            request.session.rotate = True
            return request.redirect('/web')

        return request.render('web.login')
