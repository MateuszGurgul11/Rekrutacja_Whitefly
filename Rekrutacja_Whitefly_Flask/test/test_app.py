import pytest
from flask import url_for
from app.models import Message
from app import db, celery

def test_homepage(client):
    response = client.get(url_for('homepage'))
    assert response.status_code == 200
    assert response.data

def test_add_message(client, app):
    response = client.post(url_for('add_message'), data={
        'title': 'Test Title',
        'content': 'Test Content',
        'csrf_token': (client.get(url_for('add_message')).data.decode().split('csrf_token" type="hidden" value="')[1].split('"')[0])
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test Title" in response.data
    assert b"Test Content" in response.data

    with app.app_context():
        message = Message.query.filter_by(title='Test Title').first()
        assert message is not None
        assert message.content == 'Test Content'

def test_async_add_message(client, app):
    response = client.post(url_for('async_add_message'), data={
        'title': 'Async Test Title',
        'content': 'Async Test Content',
        'csrf_token': (client.get(url_for('async_add_message')).data.decode().split('csrf_token" type="hidden" value="')[1].split('"')[0])
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Async Test Title" in response.data 

    with app.app_context():
        message = Message.query.filter_by(title='Async Test Title').first()
        assert message is not None
        assert message.content == 'Async Test Content'
