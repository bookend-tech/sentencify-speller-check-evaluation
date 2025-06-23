# 부산대 맞춤법 검사기
from kospellpy import spell_init
spell_checker = spell_init() # default: busan spell check
text = "근처에 제육 봌음 좀 마싰게 하느ㄴ ㅅㅣㄱ당 좀 없냐"
print(spell_checker(text))