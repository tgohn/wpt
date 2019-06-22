import time

def main(request, response):
    """Simple handler that causes redirection after a 2 second wait.

    The request query parameter "location" is the resource to redirect to.
    """
    time.sleep(2);
    response.status = 302
    response.headers.set("Location", request.GET.first("location"))
