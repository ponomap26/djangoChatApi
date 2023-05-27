from channels.routing import URLRouter, ProtocolTypeRouter
from channels.sessions import CookieMiddleware, SessionMiddleware
from django.core.asgi import get_asgi_application
from messages import routing

asgi = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi,
    "websocket": CookieMiddleware(SessionMiddleware(URLRouter(routing.websocket_urlpatterns))),
})