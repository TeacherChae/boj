import sys
input = sys.stdin.readline

class SuffixAutomaton:
    def __init__(self):
        # state 0: 초기 상태
        self.states = [{
            'len': 0,       # 이 상태가 표현하는 최대 길이
            'link': -1,     # suffix‐link
            'next': {}      # 전이 맵: 문자 → 상태 번호
        }]
        self.last = 0        # 현재 문자열 전체를 표현하는   마지막 상태 ID

    def extend(self, c):
        """문자 c를 automaton 끝에 추가"""
        p = self.last
        cur = len(self.states)
        # 새 상태 생성
        self.states.append({'len': self.states[p]['len'] + 1, 'link': 0, 'next': {}})
        
        # p에서 c 전이가 없으면 전이 추가
        while p != -1 and c not in self.states[p]['next']:
            self.states[p]['next'][c] = cur
            p = self.states[p]['link']
        
        if p == -1:
            # 더 이상 suffix‐link 타고 올라갈 곳이 없으면
            self.states[cur]['link'] = 0
        else:
            q = self.states[p]['next'][c]
            if self.states[p]['len'] + 1 == self.states[q]['len']:
                # 바로 연결 가능한 경우
                self.states[cur]['link'] = q
            else:
                # clone 상태를 만들어 q와 p→c 전이를 재조정
                clone = len(self.states)
                self.states.append({
                    'len': self.states[p]['len'] + 1,
                    'link': self.states[q]['link'],
                    'next': self.states[q]['next'].copy()
                })
                # p와 그 위 suffix들에서 q 전이를 clone으로 변경
                while p != -1 and self.states[p]['next'].get(c) == q:
                    self.states[p]['next'][c] = clone
                    p = self.states[p]['link']
                # link 재배치
                self.states[q]['link'] = self.states[cur]['link'] = clone

        self.last = cur

    def count_distinct_substrings(self):
        """모든 상태 기여분을 합산해 서로 다른 부분 문자열 수 반환"""
        total = 0
        for i in range(1, len(self.states)):
            total += (self.states[i]['len']
                      - self.states[self.states[i]['link']]['len'])
        return total

def main():
    s = input().strip()
    sam = SuffixAutomaton()
    for ch in s:
        sam.extend(ch)
    print(sam.count_distinct_substrings())

if __name__ == "__main__":
    main()
