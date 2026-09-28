from django.http import HttpResponseRedirect

class ApexToWwwRedirectMiddleware:
    """
    Redirects requests from the apex domain to the www subdomain,
    but explicitly ignores specified subdomains like 'dash'.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        domain = host.split(':')[0]
        
        # Define subdomains that should NOT be redirected to www.<subdomain>
        ignored_subdomains = ['dash.', 'www.']
        
        needs_redirect = True
        for sub in ignored_subdomains:
            if domain.startswith(sub):
                needs_redirect = False
                break
                
        if needs_redirect:
            port = f":{host.split(':')[1]}" if ':' in host else ""
            new_host = f"www.{domain}{port}"
            new_url = f"{request.scheme}://{new_host}{request.get_full_path()}"
            return HttpResponseRedirect(new_url)

        return self.get_response(request)
