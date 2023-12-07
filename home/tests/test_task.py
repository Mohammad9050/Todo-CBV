import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def client_api():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(username='test', password='12345678')
    return user


@pytest.mark.django_db
class TestApi:

    def test_api_list_get_401_status(self, client_api):
        url = reverse("api:tasks-list")
        response = client_api.get(url)
        assert response.status_code == 401

    # def test_api_list_get_200_status(self, client_api, common_user):
    #     url = reverse("api:tasks-list")
    #     client_api.force_login(user= common_user)
    #     response = client_api.get(url)
    #     assert response.status_code == 200
        
    # def test_api_task_post_401_status(self, client_api, common_user):
        
    #     url = reverse("api:tasks-list")
    #     data = {
    #         'user': common_user,
    #         'title': 'test'
    #     } 
    #     response = client_api.post(url, data)
    #     assert response.status_code == 401

    # def test_api_task_post_201_status(self, client_api, common_user):

    #     url = reverse("api:tasks-list")
    #     client_api.force_login(user= common_user)
    #     data = {
    #         'user': common_user,
    #         'title': 'test'
    #     } 
    #     response =client_api.post(url, data=data)

    #     assert response.status_code == 201


