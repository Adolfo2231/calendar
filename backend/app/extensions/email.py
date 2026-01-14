# Fix aplicado: Se agregó el import de SecretStr en fastapi_mail/config.py
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import SecretStr
from app.config import settings

# Configuración automática de TLS según el puerto comúnmente usado
# Puerto 587 → STARTTLS (Gmail, Outlook, etc.)
# Puerto 465 → SSL/TLS
port = settings.MAIL_PORT

# Si ambos están en True (conflicto), usar detección automática según puerto
# Si solo uno está en True, usar ese. Si ninguno está en True, usar detección automática
if settings.MAIL_TLS and settings.MAIL_SSL:
    # Conflicto: ambos en True, usar detección automática
    use_starttls = (port == 587)
    use_ssl_tls = (port == 465)
elif settings.MAIL_TLS:
    # Usuario especificó STARTTLS
    use_starttls = True
    use_ssl_tls = False
elif settings.MAIL_SSL:
    # Usuario especificó SSL
    use_starttls = False
    use_ssl_tls = True
else:
    # Ninguno especificado, usar detección automática
    use_starttls = (port == 587)
    use_ssl_tls = (port == 465)

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=SecretStr(settings.MAIL_PASSWORD) if settings.MAIL_PASSWORD else SecretStr(""),
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=port,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=use_starttls,  # Habilitado automáticamente para puerto 587
    MAIL_SSL_TLS=use_ssl_tls,  # Habilitado automáticamente para puerto 465
)

print(f"Configuración de email: {conf.MAIL_PASSWORD}")
# Instancia global de FastMail
fastmail = FastMail(conf)
