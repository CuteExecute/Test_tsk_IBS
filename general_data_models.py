def single(single_data_model: {}):
    single_model = {
        "data": single_data_model,
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    return single_model


def pages(data_list: []):
    page_model = {
        "page": 1,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": data_list,
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    return page_model

# class Pages:
#     json_object: dict
#     page: str = json_object["page"]