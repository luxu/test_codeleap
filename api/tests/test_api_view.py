import json

from rest_framework import status


def test_list_careers(client, career):
    url = '/careers/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content)[0]['id'] == career.id
    assert json.loads(response.content)[0]['title'] == 'Example Post Title'
    assert json.loads(response.content)[0]['author_ip'] == '127.0.0.1'


def test_get_career_by_id(client, career):
    url = f'/careers/{career.id}/'
    response = client.get(url)
    assert json.loads(response.content)['id'] == career.id
    assert json.loads(response.content)['title'] == 'Example Post Title'
    assert json.loads(response.content)['author_ip'] == '127.0.0.1'


def test_create_careers_with_authorization(api_client, token):
    url = '/careers/'
    payload = {
        'title': 'Updated Title',
        'content': 'Updated Content',
        'username': 'testuser',
        'author_ip': '127.0.0.1'
    }
    response = api_client.post(
        url,
        payload,
        format='json',
    )
    assert json.loads(response.text)['detail'] == 'As credenciais de autenticação não foram fornecidas.'
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_career(api_client, token):
    url = '/careers/'
    payload = {
        'title': 'Updated Title',
        'content': 'Updated Content',
        'username': 'testuser',
        'author_ip': '127.0.0.1'
    }
    api_client.credentials(
        HTTP_AUTHORIZATION=f'Token {token}'
    )
    response = api_client.post(
        url,
        payload,
        format='json',
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_update_career(api_client, token, career):
    url = f'/careers/{career.id}/'
    payload = {
        'author_ip': '0.0.0.0'
    }
    api_client.credentials(
        HTTP_AUTHORIZATION=f'Token {token}'
    )
    response = api_client.patch(
        url,
        payload,
        format='json',
    )
    assert response.status_code == status.HTTP_200_OK
    career.refresh_from_db()
    assert career.author_ip == '0.0.0.0'

def test_delete_career(api_client, token, career):
    url = f'/careers/{career.id}/'
    api_client.credentials(
        HTTP_AUTHORIZATION=f'Token {token}'
    )
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT

