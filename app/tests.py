from django.test import TestCase

class ViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # here we can insert data in DB for test but my case is different
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

# Create your tests here.
