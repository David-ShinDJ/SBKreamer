import time,re
from seleniumbase import SB

product_name = None
product_url = None
product_option = None
product_ipp = None
product_ssp = None
product_mn = None
product_mr = None
product_exmn = None
product_r_ssp_ipp = None
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
    product_ipp = int(re.sub(r'[^\d]', '', sb.get_text('div.price-text-container p.text-lookup.price.display_paragraph')))
    product_ssp_elements = sb.find_elements('div.btn_wrap div.price em')
    product_ssp = int(re.sub(r'[^\d]', '', product_ssp_elements[1].text))
    product_mn = product_ssp - product_ipp
    product_mr = f"{(product_mn / product_ssp) * 100:.2f}%"
    sb.wait_for_element('div.content div.detail_wrap')
## TODO: exmn_elements <td>태그 확인해서 텍스트값 전부 불러오기
    product_exmn_elements = sb.find_elements("price_table.table_wrap.lg td.table_td.align_right span")
    print(product_exmn_elements, product_exmn[0].text)
    product_exmn = [product_exmn_elements.text for price in product_exmn_elements]
    sb.go_back()
    sb.sleep(5)
    # sb.click('li.menu p:contains("%s")' % self.basic_filter2, timeout=10)

## 가져와야할 데이터
print(product_name, product_url, product_option, product_ipp, product_ssp, product_mn, product_mr, product_exmn)







