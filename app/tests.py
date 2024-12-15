# tests.py
from django.test import TestCase
from .models import User, Transaction

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User", email="test@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')

class TransactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="Test User", email="test@example.com")
        self.transaction = Transaction.objects.create(user=self.user, amount=100.50, description="Payment")

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.amount, 100.50)
        self.assertEqual(self.transaction.description, "Payment")

