import time,re
from seleniumbase import SB


def get_info(text_elements: str):
    lines = text_elements.split('\n')
    result = [lines[i] for i in [1, 2, 4, 6, 8, 10]]
    return result
class Product:
    def __init__(self, name, url, option, ipp, ssp, info, index, page_index):
        self.name = name
        self.url = url
        self.option = option
        self.ipp = ipp
        self.ssp = ssp
        self.m = self.ssp - self.ipp
        self.mr = f"{(self.m / self.ssp) * 100:.2f}%"
        self.info = info
        self.index = index
        self.page_index = page_index


## TODO : 로그인후에 더 많은 데이터 추출해야한다

start_index = 0
products = []
## TODO: 특정 필터를 지정하면 basic_filleter 없어지는 조합이 존재한다 컬렉터블 > 레고 > 성별존재없음
with SB() as sb:
    sb.open("https://kream.co.kr/search")
    if sb.is_element_visible('div.search_result_item.content'):
        start_index += 1
    for i in range(1, 10):
        sb.wait_for_element_present('div.search_result_list')
        sb.click('div.search_result_item.product[data-result-index="%s"]' % start_index)
        sb.wait_for_element_present('div.content div.column_top')
        name = sb.get_text('div.main-title-container p.sub-title')
        url = sb.get_current_url()
        option = sb.get_text('div.product_figure_wrap.lg span.title-txt')
        ipp = int(
            re.sub(r'[^\d]', '', sb.get_text('div.price-text-container p.text-lookup.price.display_paragraph')))
        ssp_elements = sb.find_elements('div.btn_wrap div.price em')
        ssp = int(re.sub(r'[^\d]', '', ssp_elements[1].text))
        sb.wait_for_element('div.content div.detail_wrap')
        texts_element = sb.get_text('div.product_info_wrap dl.detail-product-container')
        info = get_info(texts_element)
        product = Product(name, url, option, ipp, ssp, info, start_index, 1)
        products.append(product)
        sb.go_back()
        start_index += 1
    sb.sleep(5)

def get_products(products: list):
    for product in products:
        print(f"Name: {product.name}")
        print(f"URL: {product.url}")
        print(f"Option: {product.option}")
        print(f"IPP: {product.ipp}")
        print(f"SSP: {product.ssp}")
        print(f"Margin: {product.m}")
        print(f"Margin Rate: {product.mr}")
        print(f"Info: {product.info}")
        print(f"Index: {product.index}")
        print(f"Page Index: {product.page_index}")
        print("-" * 20)

get_products(products)