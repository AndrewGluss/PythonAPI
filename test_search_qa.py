import requests
import pytest

class TestAPI:
    def test_search_qa(self):
        qa_response = requests.get('https://api.pfm.team/v9/search/global?page=0&inquiry=qa')
        assert qa_response.status_code == 200, \
        "Something wrong"
        
        
        #print(qa_response.json())
        count_qa = 0
        for i in qa_response.json()["data"]["documents"]:
            if "qa" in i["user"]["login"]:
                count_qa += 1
        print("Количество результатов где есть 'qa': ", count_qa)
        assert count_qa > 0, \
        "Not Found"


if '__name__'=='__main__':
    pytest.main()
