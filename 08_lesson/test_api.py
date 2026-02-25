import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer $YOUR_TOKEN$'
}

base_url = "https://ru.yougile.com/api-v2/projects"


def create_project(title):
    url = base_url
    payload = json.dumps({
      "title": title
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json(), response.status_code


def update_project(project_id, title):
    url = base_url + "/" + project_id
    payload = json.dumps({
      "title": title
    })

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.json(), response.status_code


def get_project(project_id):
    url = base_url + "/" + project_id

    response = requests.request("GET", url, headers=headers)
    return response.json(), response.status_code


def test_create_project():
    result, code = create_project("some title")
    assert code == 201
    assert 'id' in result


def test_create_project_negative():
    result, code = create_project("")
    assert code == 400
    assert 'id' not in result


def test_update_project():
    result, _ = create_project("some title")
    update_result, code = update_project(result['id'], "another title")
    assert code == 200
    assert result['id'] == update_result['id']


def test_update_project_negative():
    result, _ = create_project("some title")
    update_result, code = update_project(result['id'], "")
    assert code == 400
    assert 'id' not in update_result


def test_get_project():
    title = "some title"
    result, _ = create_project(title)
    get_result, code = get_project(result['id'])
    assert code == 200
    assert get_result['title'] == title


def test_get_project_negative():
    title = "some title"
    result, _ = create_project(title)
    get_result, code = get_project("wrong-id")
    assert code == 404
    assert 'error' in get_result
