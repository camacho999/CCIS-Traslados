"""
Test básico de la aplicación Flask
"""
import unittest
from app import create_app, db
from app.models.user import User


class BasicTestCase(unittest.TestCase):
    """Tests básicos de la aplicación."""
    
    def setUp(self):
        """Configuración antes de cada test."""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
    
    def tearDown(self):
        """Limpieza después de cada test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_home_page(self):
        """Test de la página de inicio."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        """Test de la página acerca de."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        """Test de la página de login."""
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        """Test de la página de registro."""
        response = self.client.get('/auth/register')
        self.assertEqual(response.status_code, 200)
    
    def test_user_creation(self):
        """Test de creación de usuario."""
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        found_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.email, 'test@example.com')
        self.assertTrue(found_user.check_password('password123'))
    
    def test_404_error(self):
        """Test de error 404."""
        response = self.client.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
