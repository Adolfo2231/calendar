from fastapi_mail import MessageSchema
from app.extensions.email import fastmail
class EmailService:
    def __init__(self): 
        self.mail = fastmail

    async def send_registration_email(self, email: str, username: str = None):
        """
        Envía email de bienvenida al usuario registrado.
        
        Args:
            email: Email del destinatario
            username: Nombre de usuario (opcional, para personalizar el mensaje)
        """
        body = f"Welcome to MyCalendar{', ' + username if username else ''}!"
        await self.send_email({
            "subject": "Welcome to MyCalendar",
            "recipients": email,
            "body": body,
            "subtype": "plain"
        })
        return body

    async def send_email(self, data: dict):
        message = MessageSchema( 
            subject=data["subject"],
            recipients=[data["recipients"]],
            body=data["body"],
            subtype=data.get("subtype", "plain"),  # Por defecto "plain", puede ser "html"
        )
        await self.mail.send_message(message)