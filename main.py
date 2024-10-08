import time
from seleniumbase import SB

product_name = None
product_url = None
product_option = None
product_ipp = None
product_ssp = None
product_mr = None
product_mn = None
product_exmn = None
product_ssp_ipp = None
product_rssp_day = None
product_ra_day = None
product_mpc = None
product_pip = None
product_sip = None
product_id = None
product_category = None
product_reviews = None
product_rp = None
product_brand = None
product_number = None
product_color = None
product_quantity = None
now_page = None
all_page = None


start_index = 0
## TODO: 특정 필터를 지정하면 basic_filleter 없어지는 조합이 존재한다 컬렉터블 > 레고 > 성별존재없음
with SB() as sb:
    sb.open("https://kream.co.kr/search")
    sb.wait_for_element('div.search_result_list')
    if sb.is_element_visible('div.search_result_item.content'):
        start_index = 1

    sb.click('div.search_result_item.product[data-result-index="%s"]' % start_index)
    sb.wait_for_element('div.content div.column_top')
    product_name = sb.get_text('div.main-title-container p.sub-title')
    product_url = sb.get_current_url()
    product_option = sb.get_text('div.product_figure_wrap.lg span.title-txt')
    product_ipp = sb.get_text('div.price-text-container p.text-lookup.price.display_paragraph')
    sb.go_back()
    sb.sleep(5)
    # sb.click('li.menu p:contains("%s")' % self.basic_filter2, timeout=10)

## 가져와야할 데이터
print(product_name, product_url, product_option, product_ipp)







