from ..data_service import ProductService
import json

class ProductLoader():

    def __init__(self) -> None:
        print(__file__)
        self.json_url = 'main/resources/products.json'
        self.products = self._load_json()
    
    def _load_json(self):
        with open(self.json_url) as f:
            products = json.load(f)
        return products




    def upload_to_database(self):
        # ProductService.delete_all()
        # quit()
        counter = 0
        for product in self.products:
            ProductService.post(product, return_object=False)
            if counter%100 == 0:
                print(f'progress {counter}')
            counter+=1
        print('Done uploading products')