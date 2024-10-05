from seleniumbase import SB
from filter import category, basic_filter, data_filter
email = "ehdwnsqkqhek@naver.com"
password = "Tls1169511!"
categories = [category[0]]
filter_tuple = ("성별", filter_list["성별"][0])
print(filter_list)



# with SB() as sb:
#     sb.open("https://kream.co.kr/")
#     sb.click('a:contains("로그인")')
#     sb.type('input[type="email"]', "ehdwnsqkqhek@naver.com")
#     sb.type('input[type="password"]', "Tls1169511!")
#     sb.click('button[type="submit"]')
#     sb.wait_for_element('a:contains("로그아웃")')
#     sb.click('a:contains("SHOP")')
#     sb.wait_for_element('div.search_filter')






