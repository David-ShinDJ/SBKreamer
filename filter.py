import time
from seleniumbase import SB
from const import category, basic_filter, data_filter

class Filter:
    # category basic_filter dictionary type , data_filter list
    # 바람막이 -> 아우터 / 자켓
    def __init__(self, category1, category2, basic_filter1, basic_filter2, data_filter):
        cate1 = input(f"{list(category.keys())} 한개의값을 입력하세요 : ")
        cate2 = input(f"{list(category[cate1])} 한개의값을 입력하세요 : ")
        bfilter1 = input(f"{list(basic_filter.keys())} 한개의값을 입력하세요 : ")
        bfilter2 = input(f"{list(basic_filter[bfilter1])} 한개의값을 입력하세요 : ")
        dfilter = input(f"{data_filter} 한개의값을 입력하세요 : ")
        self.category1 = cate1
        self.category2 = cate2
        self.basic_filter1 = bfilter1
        self.basic_filter2 = bfilter2
        self.data_filter = dfilter

    def set_filter(self):
        ## TODO: 특정 필터를 지정하면 basic_filleter 없어지는 조합이 존재한다 컬렉터블 > 레고 > 성별존재없음
        with SB() as sb:
            sb.open("https://kream.co.kr/search")
            # sb.click('a:contains("SHOP")') 생략
            sb.wait_for_element("div.search_filter")
            sb.click('li.menu span:contains("%s")' % self.category1)
            sb.click('li.menu span:contains("%s")' % self.category2, timeout=10)
            sb.click('div.title_box span:contains("%s")' % self.basic_filter1)
            sb.wait_for_element('li.menu a.menu_link span.link_txt')
            sb.click('li.menu p:contains("%s")' % self.basic_filter2, timeout=10)
            sb.click('button.sorting_title')
            if self.data_filter != "추천순":
                sb.click('li.sorting_item p:contains("%s")' % self.data_filter)



