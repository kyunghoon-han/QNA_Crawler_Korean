from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
from time import sleep
import random

"""
Function Definitions Below...
"""
wanted_levels = ['태양신', '절대신', '별신', '수호신','우주신',
                '달신', '물신', '바람신', '식물신']
# Takes 'href' links from the given BeautifulSoup Object
def get_question_links (bs_obj, string_a, re_condition):
    time_to_sleep = [1,2,3,2.7,0.5,1.2,0.9]
    return_list = []
    for link in bs_obj.find_all(string_a,href=re.compile(re_condition)):
        if 'href' in link.attrs:
            t_val = random.choice(time_to_sleep)
            sleep(t_val)
            return_list.append(link.attrs[str('href')])
    return return_list

# This gives the number of answers and the "levels" of responders
def answer_quality(bs_input):
    time_to_sleep = [1,2,3,2.7,0.5,1.2,0.9]
    """
        The following component represents the # of answers
        <em class="_answerCount num">4</em>
        and the following gives the "level" of the responders
        <em class="text-color--primary">태양신</em>
    """
    list_levels = []
    try:
        num_ans = bs_input.find('em', {'class':"_answerCount num"})
        num_ans = int(num_ans.contents[0])
        t_val = random.choice(time_to_sleep)
        sleep(t_val)
        for level in bs_input.find_all('em', {'class':"text-color--primary"}):
            level = level.contents[0]
            list_levels.append(level)
    except:
        num_ans = 0
    return num_ans, list_levels

# To read the answers?
def read_answers(bs_obj):
    list_answers = []
    for ans_dirty in bs_obj.find_all('div',
                {'class': 'se-module se-module-text'}):
        ans = ans_dirty.get_text()
        ans = ans.replace('\t', '')
        ans = ans.replace('\n', '')
        ans = ans.replace('\u200b', '')
        ans = ans.replace('\xa0', '')
        list_answers.append(ans_dirty.get_text())
    return list_answers

# To read the title and the contents of a question?
def read_question(bs_obj):
    title_q = ''
    contents_q = ''
    list_out = []
    try:
        # div class="c-heading__title-inner"  ===> Main title
        Q_dirty = bs_obj.find('div', {'class': "c-heading__title-inner"})
        title_q = Q_dirty.get_text()
        title_q = title_q.replace('\t', '')
        title_q = title_q.replace('\n', '')
        title_q = title_q.replace('\u200b', '')
        title_q = title_q.replace('\xa0', '')
        # div class="c-heading__content" ===> Contents of the question
        Q_dirty = bs_obj.find('div',{'class': "c-heading__content"})
        contents_q = Q_dirty.get_text()
        contents_q = contents_q.replace('\n', '')
        contents_q = contents_q.replace('\t' , '')
        contents_q = contents_q.replace('\u200b', '')
        contents_q = contents_q.replace('\xa0', '')
    except:
        return (title_q, contents_q)
    return (title_q, contents_q)
