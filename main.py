from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import json
from QNA_links import *
"""
Main
"""

num_page = 1

max_page = num_page + 10000
bound_in_loop = True
while bound_in_loop:

    html = urlopen('https://kin.naver.com/qna/list.nhn?page=' + str(num_page))
    bs = soup(html, 'html.parser')
    links = get_question_links(bs,'a','^(/qna/detail.nhn?)')
    index = 0
    list_output = []
    for link in links :
        link = 'https://kin.naver.com' + link
        link_in = urlopen(link)
        bs_link = soup(link_in, 'html.parser')
        num_respond, levels_responders = answer_quality(bs_link)
        if num_respond == 0 or len(levels_responders) == 0:
            continue
        answer_list = read_answers(bs_link)
        main_Q, detail_Q = read_question(bs_link)
        list_pair_up = []
        for i in range(min(len(levels_responders),len(answer_list))):
            pair = (levels_responders[i],answer_list[i])
            list_pair_up.append(pair)
            dict_temp ={
                'Question Title':main_Q,
                'Question Details':detail_Q,
                "Number of Responders": num_respond,
                "Answer Contents":[{'Level of Responder': lvl, 'Answer':answ}
                                  for lvl, answ in list_pair_up]
                }
            list_output.append(dict_temp)
    output_name = str(num_page)
    output_name = 'crawl_data_'+ output_name +'.json'
    #output_name = 'crawl_data.json'
    with open(output_name, 'w', encoding='utf-8') as f:
        json.dump(list_output, f, ensure_ascii=False, indent=4)
    num_page += 1
    if num_page > max_page:
        bound_in_loop = False
