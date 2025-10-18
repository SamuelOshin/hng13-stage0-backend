from fastapi.testclient import TestClient
from unittest.mock import patch

import main


client = TestClient(main.app)


def test_get_me_returns_profile_and_fact():
    async def fake_cat_fact():
        return "Test cat fact"

    with patch("app.services.cat_facts.get_cat_fact", fake_cat_fact):
        resp = client.get("/me")
        assert resp.status_code == 200
        data = resp.json()

        # Basic shape
        assert data["status"] == "success"
        assert "user" in data
        assert "timestamp" in data
        assert "fact" in data

        # User fields
        assert set(data["user"].keys()) == {"email", "name", "stack"}

        # Fact was patched
        assert data["fact"] == "Test cat fact"
