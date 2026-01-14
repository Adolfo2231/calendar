# 📅 Calendar Application

Calendar application developed with FastAPI to manage events and reminders.

## 🚀 Features

- ✅ Event management (create, edit, delete)
- 📝 Custom reminders
- 🔍 Event search
- 🔐 JWT authentication
- 📧 Welcome emails on user registration
- 📊 Automatic API documentation (Swagger)

## 🛠️ Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- JWT + bcrypt
- Email service (fastapi-mail)

## 📦 Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configurations
uvicorn app.main:app --reload
```

Server available at `http://localhost:8000`
- API: `http://localhost:8000/api/v1`
- Swagger: `http://localhost:8000/docs`

## 🔧 Configuration

```env
# Database
DATABASE_URL=sqlite+aiosqlite:///./calendar.db
# For PostgreSQL: DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/calendar_db

# Security
SECRET_KEY=your-super-secure-secret-key-here
CORS_ORIGINS=http://localhost:5173

# Email (for welcome emails on registration)
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password  # For Gmail, use App Password
MAIL_FROM=your-email@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
# TLS/SSL auto-detected based on port (587=STARTTLS, 465=SSL)
```

#### 📧 Email Configuration

The application sends welcome emails when users register. To configure email:

1. **For Gmail:**
   - Enable 2-Step Verification in your Google Account
   - Generate an App Password: https://myaccount.google.com/apppasswords
   - Use the App Password (16 characters) as `MAIL_PASSWORD`
   - Use `smtp.gmail.com` as `MAIL_SERVER`
   - Port `587` (STARTTLS) or `465` (SSL/TLS)

2. **For other providers:**
   - Update `MAIL_SERVER` with your SMTP server
   - Update `MAIL_PORT` (587 for STARTTLS, 465 for SSL/TLS)
   - TLS/SSL is automatically detected based on port

**Note:** If email fails, the user registration still succeeds. Check server logs for email errors.

## 📚 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Current user

### Events
- `GET /api/v1/events` - List events
- `POST /api/v1/events` - Create event
- `GET /api/v1/events/{id}` - Get event
- `PUT /api/v1/events/{id}` - Update event
- `DELETE /api/v1/events/{id}` - Delete event

Interactive documentation: `http://localhost:8000/docs`