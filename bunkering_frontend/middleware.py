import logging
from django.http import HttpResponseNotFound

logger = logging.getLogger(__name__)

class BotFilterMiddleware:
    """Filter out common bot/scanner requests to reduce noise."""
    
    # Common scanner/bot paths that your static site doesn't use
    BLOCKED_PATHS = {
        '/register', '/login', '/admin', '/wp-admin', '/wp-login.php',
        '/phpmyadmin', '/pma', '/mysql', '/config', '/.env', '/.git',
        '/api', '/test', '/tmp', '/backup', '/old', '/new', '/dev',
        '/staging', '/beta', '/alpha', '/demo', '/debug', '/info',
        '/phpinfo.php', '/info.php', '/test.php', '/config.php',
        '/xmlrpc.php', '/wp-content', '/wp-includes', '/trackback',
        '/cgi-bin', '/_private', '/_vti_bin', '/_vti_inf.html',
        '/_vti_pvt', '/_vti_txt', '/msadc', '/scripts', '/samples',
        '/iisadmin', '/iishelp', '/web.config', '/global.asax',
        '/global.asa', '/default.asp', '/default.aspx', '/index.php',
        '/joomla', '/drupal', '/magento', '/prestashop', '/typo3',
        '/phpbb', '/vbulletin', '/smf', '/node', '/graphql'
    }
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if this is a scanner/bot request
        path = request.path.lower()
        
        # Block common scanner paths without logging (reduces noise)
        if path in self.BLOCKED_PATHS or path.startswith(tuple(self.BLOCKED_PATHS)):
            return HttpResponseNotFound()
            
        # Block requests with suspicious headers or methods
        if request.method not in ['GET', 'POST', 'HEAD', 'OPTIONS']:
            return HttpResponseNotFound()
            
        # Block requests with common scanner user agents
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        scanner_agents = ['sqlmap', 'nikto', 'nessus', 'openvas', 'acunetix', 'burp']
        if any(agent in user_agent for agent in scanner_agents):
            return HttpResponseNotFound()
            
        response = self.get_response(request)
        return response