def test_create_student(test_client):
    response = test_client.post("/students", json={
        "reg_no": "123",
        "name": "Test User",
        "course": "DevOps"
    })
    assert response.status_code == 200
    assert response.json()["reg_no"] == "123"
