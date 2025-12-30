import pytest
from app import app, db, User, bcrypt

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create a test user
            test_user = User(
                username='testuser',
                password=bcrypt.generate_password_hash('testpass123').decode('utf-8')
            )
            db.session.add(test_user)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()


def test_home_page_redirects_to_login(client):
    """Test that the home page redirects to login"""
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location


def test_login_page(client):
    """Test that the login page loads successfully"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'login' in response.data.lower()


def test_login_with_valid_credentials(client):
    """Test login with valid credentials"""
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Login successful' in response.data or b'contact' in response.data.lower()


def test_login_with_invalid_credentials(client):
    """Test login with invalid credentials"""
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    assert b'Invalid credentials' in response.data


def test_contact_page_requires_authentication(client):
    """Test that contact page redirects when not authenticated"""
    response = client.get('/contact')
    assert response.status_code == 302
    assert '/login' in response.location


def test_contact_page_with_authentication(client):
    """Test that authenticated users can access contact page"""
    # Login first
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    # Now access contact page
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'contact' in response.data.lower()


def test_logout(client):
    """Test logout functionality"""
    # Login first
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'logged out' in response.data.lower()


def test_contact_form_submission(client):
    """Test contact form submission when authenticated"""
    # Login first
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    # Submit contact form
    response = client.post('/contact', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '+1234567890',
        'message': 'This is a test message for the contact form.'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'success' in response.data.lower() or b'submitted' in response.data.lower()
