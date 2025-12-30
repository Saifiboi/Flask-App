# # Flask Application with Jenkins CI/CD Pipeline

This is a Flask web application with automated testing and deployment using Jenkins.

## 📋 Project Overview

A secure Flask application with:
- User authentication (login/logout)
- Contact form with validation
- SQLite database
- Security features (CSRF protection, password hashing)
- Automated testing with pytest
- CI/CD pipeline with Jenkins

## 🚀 Jenkins Pipeline Stages

### Stage 1: Checkout
**Purpose**: Retrieves the latest code from the GitHub repository.

```groovy
stage('Checkout') {
    steps {
        echo "Checking out code"
        checkout scm
    }
}
```

**What it does**:
- Clones/pulls the repository from GitHub
- Ensures Jenkins has the latest version of the code
- Sets up the workspace for the build

---

### Stage 2: Install Dependencies
**Purpose**: Installs all required Python packages for the application.

```groovy
stage('Install Dependencies') {
    steps {
        echo "Installing dependencies"
        bat 'pip install -r requirements.txt'
    }
}
```

**What it does**:
- Reads `requirements.txt` file
- Installs Flask, pytest, and all dependencies
- Prepares the environment for testing and building

**Dependencies installed**:
- Flask (web framework)
- Flask-SQLAlchemy (database)
- Flask-WTF (forms)
- Flask-Bcrypt (password hashing)
- pytest (testing framework)
- email-validator (email validation)

---

### Stage 3: Run Tests
**Purpose**: Executes automated tests to ensure code quality.

```groovy
stage('Run Tests') {
    steps {
        echo "Running tests"
        bat 'pytest test_app.py -v'
    }
}
```

**What it does**:
- Runs all test cases in `test_app.py`
- Verifies application functionality
- Tests include:
  - Home page redirect to login
  - Login page loads correctly
  - Valid/invalid login credentials
  - Contact page authentication requirement
  - Authenticated access to contact page
  - Logout functionality
  - Contact form submission

**If tests fail**: Pipeline stops, preventing broken code from being deployed.

---

### Stage 4: Build
**Purpose**: Packages the application files for deployment.

```groovy
stage('Build') {
    steps {
        echo "Building application"
        bat 'if not exist "build" mkdir build'
        bat 'xcopy /Y app.py build\\'
        bat 'xcopy /E /I /Y templates build\\templates'
        bat 'xcopy /Y requirements.txt build\\'
        echo "Build complete"
    }
}
```

**What it does**:
- Creates a `build` directory
- Copies application files:
  - `app.py` (main application)
  - `templates/` folder (HTML templates)
  - `requirements.txt` (dependencies)
- Prepares a clean deployment package

**Files included in build**:
```
build/
├── app.py
├── requirements.txt
└── templates/
    ├── base.html
    ├── login.html
    └── contact.html
```

---

### Stage 5: Deploy
**Purpose**: Deploys the application to the target directory.

```groovy
stage('Deploy') {
    steps {
        echo "Deploying to C:\\Deployment\\Flask-App"
        bat 'if not exist "C:\\Deployment\\Flask-App" mkdir C:\\Deployment\\Flask-App'
        bat 'xcopy /E /I /Y build\\* C:\\Deployment\\Flask-App\\'
        echo "Deployment complete!"
    }
}
```

**What it does**:
- Creates deployment directory: `C:\Deployment\Flask-App`
- Copies all files from `build/` to deployment location
- Simulates production deployment

**Deployment location**: `C:\Deployment\Flask-App\`

**To run the deployed app**:
```bash
cd C:\Deployment\Flask-App
python app.py
```

Then visit: `http://localhost:5000`

---

## 🏗️ Pipeline Flow Diagram

```
┌─────────────┐
│  Checkout   │ ← Get code from GitHub
└──────┬──────┘
       │
┌──────▼──────────────┐
│ Install Dependencies │ ← pip install -r requirements.txt
└──────┬──────────────┘
       │
┌──────▼──────┐
│  Run Tests  │ ← pytest test_app.py
└──────┬──────┘
       │
   ┌───▼────┐
   │ PASS?  │
   └───┬────┘
       │ Yes
┌──────▼──────┐
│    Build    │ ← Copy files to build/
└──────┬──────┘
       │
┌──────▼──────┐
│   Deploy    │ ← Copy to C:\Deployment\Flask-App
└──────┬──────┘
       │
   ┌───▼─────┐
   │ SUCCESS │
   └─────────┘
```

---

## 📦 Prerequisites

### Local Development:
- Python 3.8+
- pip (Python package manager)

### Jenkins Setup:
- Jenkins installed
- Git plugin installed
- GitHub repository connected
- Windows agent (for Windows commands)

---

## 🧪 Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_app.py -v

# Run specific test
pytest test_app.py::test_login_with_valid_credentials -v
```

---

## 🔧 Running the Application Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit: `http://localhost:5000`

**Default credentials**:
- Username: `Ahmed` / Password: `ahmed123`
- Username: `Umer` / Password: `umer123`

---

## 📁 Project Structure

```
Flask-App/
├── app.py                  # Main Flask application
├── test_app.py            # Pytest test cases
├── requirements.txt       # Python dependencies
├── Jenkinsfile           # Jenkins pipeline configuration
├── README.md             # This file
├── instance/             # SQLite database
│   └── users.db
└── templates/            # HTML templates
    ├── base.html
    ├── login.html
    └── contact.html
```

---

## 🔄 CI/CD Workflow

1. **Developer pushes code** to GitHub
2. **Jenkins detects changes** (webhook or polling)
3. **Pipeline starts automatically**:
   - Checks out code
   - Installs dependencies
   - Runs tests
   - Builds application
   - Deploys to target directory
4. **If successful**: Application is deployed
5. **If failed**: Notifications sent, no deployment

---

## ✅ Post-Deployment Verification

After Jenkins completes:

1. **Check deployment directory**:
   ```bash
   dir C:\Deployment\Flask-App
   ```

2. **Verify files copied**:
   - app.py
   - requirements.txt
   - templates/

3. **Run deployed application**:
   ```bash
   cd C:\Deployment\Flask-App
   python app.py
   ```

4. **Test the application**:
   - Open browser: `http://localhost:5000`
   - Login with test credentials
   - Submit a contact form

---

## 🛠️ Troubleshooting

### Tests Fail
- Check test output in Jenkins console
- Run tests locally to debug
- Verify all dependencies installed

### Build Fails
- Check file paths are correct
- Ensure `build` directory can be created
- Verify sufficient disk space

### Deployment Fails
- Ensure `C:\Deployment\` directory exists and is writable
- Check file permissions
- Verify xcopy commands have proper syntax

---

## 📊 Test Coverage

Current tests cover:
- ✅ Route redirects (home → login)
- ✅ Page loading (login, contact)
- ✅ Authentication (valid/invalid credentials)
- ✅ Authorization (protected routes)
- ✅ Session management (logout)
- ✅ Form submission (contact form)

**Total: 8 test cases**

---

## 🔐 Security Features

- CSRF protection (Flask-WTF)
- Password hashing (Bcrypt)
- SQL injection prevention (SQLAlchemy ORM)
- XSS protection (input validation)
- Session security (HTTPOnly cookies)
- Input validation (custom validators)

---

## 📝 License

This project is for educational purposes.

---

## 👥 Authors

- Flask Application Developer
- Jenkins Pipeline Configuration

---

## 🎓 Learning Objectives

This project demonstrates:
- ✅ Flask web application development
- ✅ Automated testing with pytest
- ✅ Jenkins CI/CD pipeline setup
- ✅ Build automation
- ✅ Deployment simulation
- ✅ Version control with Git/GitHub

---

**Last Updated**: December 2025