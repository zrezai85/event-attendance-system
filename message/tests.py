from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.

class MessagePageTests(SimpleTestCase):

    def test_url_exist_at_correct_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        # assertEqual means = yani mige  ایا دوتا چیز با هم برابرن یا نه مثلا توی اینجا اومده وضعیت استوس کد رو گذاشته که ایا برابر 200 هست یا نه 
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    
    def test_template_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')
    
    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response,'<h1>this is your base code</h1>')