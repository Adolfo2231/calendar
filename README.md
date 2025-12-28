# 📅 Calendar Application

Calendar application developed with FastAPI and React + JavaScript to manage events and reminders.

## 🚀 Features

- ✅ Event management (create, edit, delete)
- 📝 Custom reminders
- 🔍 Event search
- 🔐 JWT authentication
- 📊 Automatic API documentation (Swagger)

## 🛠️ Technologies

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- JWT + bcrypt

### Frontend
- React 18+
- JavaScript (ES6+)
- Vite
- Axios

## 📦 Installation

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# Edit .env with your configurations
alembic upgrade head
uvicorn app.main:app --reload
```

Server available at `http://localhost:8000`
- API: `http://localhost:8000/api/v1`
- Swagger: `http://localhost:8000/docs`

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
# Edit .env with the API URL
npm run dev
```

Frontend available at `http://localhost:5173`

## 🔧 Configuration

### Backend (.env)

```env
DATABASE_URL=postgresql://user:password@localhost:5432/calendar_db
SECRET_KEY=your-super-secure-secret-key-here
CORS_ORIGINS=http://localhost:5173
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/api/v1
```

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

## 🧪 Testing

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```
