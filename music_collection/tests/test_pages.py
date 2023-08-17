# from django.test import TestCase

# class IndexPageTestCase(TestCase):
#     def test_index_page(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'MUSIC COLLECTION')
#         self.assertContains(response, 'Welcome to MUSIC COLLECTION, your personal world of sounds!')
#         self.assertContains(response, 'Tracks:')
#         self.assertContains(response, 'Genres:')
#         self.assertContains(response, 'Artists:')
#         self.assertContains(response, 'Albums:')
#         self.assertContains(response, '<iframe')
#         self.assertContains(response, '<footer')

# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from collection_app.models import Tracks, Artists

# class IndexPageTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client.login(username='testuser', password='testpass')

#         self.artist = Artists.objects.create(name='Test Artist')
#         self.track1 = Tracks.objects.create(title='Test Track 1', artist=self.artist)
#         self.track2 = Tracks.objects.create(title='Test Track 2', artist=self.artist)
        
#     def test_index_page_with_auth(self):
#         response = self.client.get(reverse('index'))
        
#         self.assertEqual(response.status_code, 200)
        
#         self.assertContains(response, '<title>Music collection</title>')
#         self.assertContains(response, 'Test Artist')
#         self.assertContains(response, 'Test Track 1')
#         self.assertContains(response, 'Test Track 2')
#         self.assertContains(response, 'Logout')
        
#     def test_index_page_without_auth(self):
#         self.client.logout()

#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, '<title>Music collection</title>')
#         self.assertNotContains(response, 'Test Artist')
#         self.assertNotContains(response, 'Test Track 1')
#         self.assertNotContains(response, 'Test Track 2')
#         self.assertContains(response, 'Login')
#         self.assertContains(response, 'Register')

    
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.core.files.uploadedfile import SimpleUploadedFile
# from collection_app.models import Client


# class ProfilePageTest(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpass'
#         )
#         self.userprofile = Client.objects.create(
#             user=self.user,
#             balance=100,
#             tracks=['Track 1', 'Track 2']
#         )
        
#     def test_profile_page_authenticated(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profile.html')
#         self.assertContains(response, 'Your profile data:')
#         self.assertContains(response, 'testuser')
#         self.assertContains(response, 'balance: 100')
#         self.assertContains(response, 'Track 1')
#         self.assertContains(response, 'Track 2')
#         self.assertNotContains(response, 'You do not have purchase yet!')
#         self.assertNotContains(response, 'Add funds')
#         self.client.logout()
        
#     def test_profile_page_unauthenticated(self):
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('login') + '?next=' + reverse('profile'))
        
#     def test_add_funds(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.post(reverse('profile'), {'balance': 50})
#         self.assertEqual(response.status_code, 302)
#         self.userprofile.refresh_from_db()
#         self.assertEqual(self.userprofile.balance, 150)
#         self.client.logout()
        
#     def test_purchase_link(self):
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.get(reverse('profile'))
#         self.assertContains(response, reverse('purchase'))
#         self.client.logout()
        
#     def test_no_tracks(self):
#         userprofile = Client.objects.create(
#             user=self.user,
#             balance=0
#         )
#         self.client.login(username='testuser', password='testpass')
#         response = self.client.get(reverse('profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'You do not have purchase yet!')
#         self.assertNotContains(response, 'Track 1')
#         self.assertNotContains(response, 'Track 2')
#         self.client.logout()

# from django.test import TestCase, Client
# from django.urls import reverse

# class LogoutPageTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpass'
#         )
#         self.client.login(username='testuser', password='testpass')

#     def test_logout_page(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Logged out!')
#         self.assertContains(response, 'Click here to login again.')
#         self.assertTemplateUsed(response, 'logout.html')
#         self.client.logout()

# # from django.test import TestCase

# # class TestMusicPlayer(TestCase):
# #     def test_page_loads(self):
# #         response = self.client.get('/path/to/player/')
# #         self.assertEquals(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'base_generic.html')
# #         self.assertContains(response, 'My Music Player')
# #         self.assertContains(response, 'Player')
# #         self.assertContains(response, 'controls')
# #         self.assertContains(response, 'iframe')
        
# #     def test_audio_playback(self):
# #         response = self.client.get('/path/to/player/')
# #         self.assertEquals(response.status_code, 200)
# #         self.assertContains(response, '<audio controls>')
# #         self.assertContains(response, '<button class="play">Play</button>')
# #         self.assertContains(response, '<button class="pause">Pause</button>')
        
# #         audio_element = response.context['audio']
# #         play_button = '<button class="play">Play</button>'
# #         pause_button = '<button class="pause">Pause</button>'
        
# #         response = self.client.post('/path/to/player/', {'action': 'play'})
# #         self.assertEquals(response.status_code, 200)
# #         self.assertEquals(audio_element.is_playing(), True)
# #         self.assertContains(response, pause_button)
# #         self.assertNotContains(response, play_button)
        
# #         response = self.client.post('/path/to/player/', {'action': 'pause'})
# #         self.assertEquals(response.status_code, 200)
# #         self.assertEquals(audio_element.is_playing(), False)
# #         self.assertContains(response, play_button)
# #         self.assertNotContains(response, pause_button)
        
# #     def test_audio_navigation(self):
# #         response = self.client.get('/path/to/player/')
# #         self.assertEquals(response.status_code, 200)
# #         self.assertContains(response, '<button class="prev">&lt;prev</button>')
# #         self.assertContains(response, '<button class="next">next&gt;</button>')
        
# #         audio_element = response.context['audio']
# #         prev_button = '<button class="prev">&lt;prev</button>'
# #         next_button = '<button class="next">next&gt;</button>'
        
# #         response = self.client.post('/path/to/player/', {'action': 'previous'})
# #         self.assertEquals(response.status_code, 200)
# #         self.assertEquals(audio_element.current_track, 0)
# #         self.assertContains(response, prev_button)
# #         self.assertNotContains(response, next_button)
        
# #         response = self.client.post('/path/to/player/', {'action': 'next'})
# #         self.assertEquals(response.status_code, 200)
# #         self.assertEquals(audio_element.current_track, 1)
# #         self.assertContains(response, next_button)
# #         self.assertNotContains(response, prev_button)

# from django.test import TestCase
# from django.urls import reverse

# from collection_app.models import Tracks

# class TrackListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Создаем данные для тестирования
#         Tracks.objects.create(
#             title='Track1',
#             artist='Artist1',
#             file='test_files/track1.mp3'
#         )
#         Tracks.objects.create(
#             title='Track2',
#             artist='Artist2',
#             file='test_files/track2.mp3'
#         )

#     def test_track_list_view(self):
#         url = reverse('track-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Track1 - Artist1')
#         self.assertContains(response, 'Track2 - Artist2')
#         self.assertContains(response, '<a href="test_files/track1.mp3">Download</a>')
#         self.assertContains(response, '<a href="test_files/track2.mp3">Download</a>')

# from django.test import TestCase, Client
# from django.urls import reverse
# from collection_app.models import Subscription
# from collection_app.forms import SubscriptionForm

# class SubscriptionViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('subscription')
#         self.data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'email': 'johndoe@example.com',
#         }
#         self.form = SubscriptionForm(data=self.data)
    
#     def test_subscription_view(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'subscription.html')
#         self.assertIsInstance(response.context['form'], SubscriptionForm)

#     def test_subscription_form_valid(self):
#         response = self.client.post(self.url, data=self.data)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('success'))

#         self.assertTrue(Subscription.objects.filter(email=self.data['email']).exists())
    
#     def test_subscription_form_invalid(self):
#         response = self.client.post(self.url, data={})
#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(response.context['form'].is_valid())
#         self.assertContains(response, 'Это поле обязательно.')

# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User

# class PurchaseSubscriptionTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('purchase_subscription')
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.money = Client.objects.create(user=self.user, amount=300)
        
#     def test_purchase_subscription_view(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html')
#         self.assertIn('You want to purchase a subscription to add tracks', response.content.decode())
#         self.assertIn('The price: 289', response.content.decode())
#         self.assertIn('Funds available: 300', response.content.decode())
        
#     def test_purchase_subscription_with_enough_funds(self):
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(self.url, data={})
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('subscription'))
        
#     def test_purchase_subscription_without_enough_funds(self):
#         self.money = 200
#         self.money.save()
#         self.client.login(username='testuser', password='12345')
#         response = self.client.post(self.url, data={})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('You can add funds on', response.content.decode())
