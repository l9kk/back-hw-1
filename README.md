# 🚀 Quick Start Guide

### Option 1: Manual Setup

```bash
# 1. Start the application
docker-compose up -d

# 2. Run database migrations (REQUIRED!)
docker-compose exec web alembic upgrade head
```

### 🎯 Access Your App

- **Web Interface**: http://localhost:8000/frontend/
- **API Documentation**: http://localhost:8000/docs

### 🆘 Something Wrong?

**Most Common Issue**: "relation 'users' does not exist"
**Fix**: Run the migrations:
```bash
docker-compose exec web alembic upgrade head
```

**If tables still don't exist after migration**:
```bash
# Check what tables exist
docker-compose exec db psql -U postgres -d postgres -c "\dt"

# If only alembic_version table exists, create a new migration:
docker-compose exec web alembic revision --autogenerate -m "Create missing tables"
docker-compose exec web alembic upgrade head
```

**Other Issues**:
```bash
# Check if containers are running
docker-compose ps

# View logs
docker-compose logs -f

# Fresh restart
docker-compose down && docker-compose up -d
```

---

That's it!


## 📱 How to Use

### 1. Register a New Account
- Open http://localhost:8000/frontend/
- Fill in the registration form with username and password
- Click "Register"

### 2. Login
- Use your credentials to log in
- You'll be redirected to the task management interface

### 3. Manage Tasks
- **Add Task**: Fill in title and description, click "Add Task"
- **Complete Task**: Click the ✓ button to mark as complete
- **Edit Task**: Click the ✎ button to modify task details
- **Delete Task**: Click the ✕ button to remove a task
