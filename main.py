import time

from seleniumbase import SB
from filter import category, basic_filter, data_filter
email = "ehdwnsqkqhek@naver.com"
password = "Tls1169511!"
# category basic_filter dictionary type , data_filter list
# 바람막이 -> 아우터 / 자켓
cate1 = input(f"{list(category.keys())} 한개의값을 입력하세요 : ")
cate2 = input(f"{list(category[cate1])} 한개의값을 입력하세요 : ")
bfilter1 = input(f"{list(basic_filter.keys())} 한개의값을 입력하세요 : ")
bfilter2 = input(f"{list(basic_filter[bfilter1])} 한개의값을 입력하세요 : ")
dfilter = input(f"{data_filter} 한개의값을 입력하세요 : ")



with SB() as sb:
    sb.open("https://kream.co.kr/search")
    # sb.click('a:contains("SHOP")') 생략
    sb.wait_for_element("div.search_filter")
    sb.click('li.menu span:contains("%s")' % cate1)
    sb.click('li.menu span:contains("%s")' % cate2)
    sb.click('div.title_box span:contains("%s")' % bfilter1)
    sb.wait_for_element('li.menu a.menu_link span.link_txt')
    sb.click('li.menu p:contains("%s")' % bfilter2)
    sb.click('button.sorting_title')
    if dfilter != "추천순":
        sb.click('li.sorting_item p:contains("%s")' % dfilter)
    time.sleep(7)









