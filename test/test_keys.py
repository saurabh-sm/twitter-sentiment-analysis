"""
Test environment variables set for the current session
"""

import pytest

from app import keys

def test_api_key_exists():
    '''
    Ensure API key has been set for the session.
    '''
    assert keys.API_KEY is not None

def test_api_secret_key_exists():
    '''
    Ensure API key password has been set for the session.
    '''
    assert keys.API_SECRET_KEY is not None

def test_access_token_exists():
    '''
    Ensure access token has been set for the session.
    '''
    assert keys.ACCESS_TOKEN is not None

def test_access_token_secret_exists():
    '''
    Ensure access token password has been set for the session.
    '''
    assert keys.ACCESS_TOKEN_SECRET is not None

def test_api_key_string():
    '''
    Verify data type of API key is a string
    '''
    assert type(keys.API_KEY) is str

def test_api_key_secret_string():
    '''
    Verify data type of API key password is a string
    '''
    assert type(keys.API_SECRET_KEY) is str

def test_access_token_string():
    '''
    Verify data type of access token is a string
    '''
    assert type(keys.ACCESS_TOKEN) is str

def test_access_token_secret_string():
    '''
    Verify data type of access token password is a string
    '''
    assert type(keys.ACCESS_TOKEN_SECRET) is str
