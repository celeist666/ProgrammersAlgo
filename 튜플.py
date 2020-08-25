# finall로 숫자들을 전부 찾고 이를 counter함수로 각각 중복이 몇번 되는지를 나타내는 dict로 바꾼다.
# 그런뒤 counter값의 역순으로(큰게 먼저나오는순) s의 값들을 정리해서 k 값만 뺀 리스트에 int로 매핑을 해서 리스트로 만든다.

import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s)) # \d+는 정규표현식으로 \d는 숫자를, +는 계속 숫자가 있으면 그거도 찾으라는 의미
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
