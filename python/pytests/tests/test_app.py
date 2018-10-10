# -*- coding: utf-8 -*-

import json
import pytest

from app import app


def test_fetch_valid_json():
    url = "http://localhost:8000/json/valid_format.json"

    try:
        app.fetch_json(url)
    except json.decoder.JSONDecodeError:
        pytest.fail("should decode valid json")


def test_fetch_invalid_json():
    url = "http://localhost:8000/json/invalid_format.json"

    with pytest.raises(json.decoder.JSONDecodeError) as excinfo:
        app.fetch_json(url)
    assert 'Expecting value' in str(excinfo), "should not decode invalid json"
