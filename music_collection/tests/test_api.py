from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.test.client import Client as DjangoClient
from rest_framework.test import APIClient
from collection_app.models import Tracks, Artists, Genres, Albums, Client
import json


def create_api_test(cls_model, url: str, to_add: dict, to_change: dict):
    class ViewSetsTests(TestCase):
        id_query = 'id/' # Add this line to define the id_query attribute

        def setUp(self):
            self.client = DjangoClient()
            self.creds_superuser = {'username': 'super', 'password': 'super'}
            self.creds_user = {'username': 'default', 'password': 'default'}
            self.superuser = User.objects.create_user(is_superuser=True, **self.creds_superuser)
            self.user = User.objects.create_user(**self.creds_user)
            self.token = Token.objects.create(user=self.superuser)

        def test_get(self):
            # logging in with superuser creds
            client = DjangoClient()  # создаем объект-клиент
            client.login(**self.creds_user)  # авторизуемся
            
            self.client.login(**self.creds_user)
            # GET
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            # logging out
            self.client.logout()

        def manage(self, auth_token=False):
            # POST
            resp_post = self.client.post(url, data=to_add)
            self.assertEqual(resp_post.status_code, status.HTTP_201_CREATED)
            created_id = cls_model.objects.get(**to_add).id
            # PUT
            if not auth_token:
                resp_put = self.client.put(
                    f'{url}{self.id_query}{created_id}',
                    data=json.dumps(to_change),
                )
                self.assertEqual(resp_put.status_code, status.HTTP_200_OK
                                )
                attr, obj_value = list(to_change.items())[0]
                self.assertEqual(getattr(cls_model.objects.get(id=created_id), attr), obj_value)
            # DELETE EXISTING
            resp_delete = self.client.delete(f'{url}{self.id_query}{created_id}')
            self.assertEqual(resp_delete.status_code, status.HTTP_204_NO_CONTENT)
            # DELETE NONEXISTENT
            repeating_delete = self.client.delete(f'{url}{self.id_query}{created_id}')
            self.assertEqual(repeating_delete.status_code, status.HTTP_404_NOT_FOUND)

        def test_manage_superuser(self):
            # logging in with superuser creds
            self.client.login(**self.creds_superuser)

            self.manage()

            # logging out
            self.client.logout()

        def test_manage_user(self):
            # logging in with superuser creds
            self.client.login(**self.creds_user)
            # POST
            resp_post = self.client.post(url, data=to_add)
            self.assertEqual(resp_post.status_code, status.HTTP_403_FORBIDDEN)
            # PUT
            created = cls_model.objects.create(**to_add)
            resp_put = self.client.put(
                f'{url}{self.id_query}{created.id}',
                data=json.dumps(to_change),
            )
            print(f'RESP PUT CONTENT: {resp_put.content}')
            self.assertEqual(resp_put.status_code, status.HTTP_403_FORBIDDEN)
            # DELETE EXISTING
            resp_delete = self.client.delete(f'{url}{self.id_query}{created.id}')
            self.assertEqual(resp_delete.status_code, status.HTTP_403_FORBIDDEN)
            # clean up
            created.delete()
            # logging out
            self.client.logout()

        def test_manage_token(self):
            # creating rest_framework APIClient instead of django test Client
            # because it can be forcefully authenticated with token auth
            self.client = APIClient()

            self.client.force_authenticate(user=self.superuser, token=self.token)
            self.manage(auth_token=True)
    return ViewSetsTests


GenresTest = create_api_test(Genres, '/rest/Genres/', {'title': 'genre'}, {'description': 'new_description'})
TracksTest = create_api_test(Tracks, '/rest/Tracks/', {'title': 'track', 'year': 2000}, {'rating': 5})
ArtistsTest = create_api_test(Artists, '/rest/Artists/', {'name': 'name', 'birth_date': '1995-01-01'}, {'education': 'musician'})
AlbumsTest = create_api_test(Albums, '/rest/Albums/', {'title': 'name', 'year': 1990}, {'category': 'new_category'})
ClientTest = create_api_test(Client, '/rest/Client/', {'user': 'username'}, {'money': 100})