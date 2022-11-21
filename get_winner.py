import random

name_list = [
    "박민영",
    "김준섭",
    "이은결",
    "신지연",
    "정민혁",
    "권준우",
    "배수홍",
    "한선진",
    "심보성",
    "김나연",
    "최지원",
    "김서이",
    "김민우",
    "김문혁",
    "윤채원",
    "이예찬",
    "이다경",
    "임태인",
    "이종민",
    "김민서",
]

win_list = []
print("총 참여인원 : ", len(name_list))
print("꼬북칩의 주인은??!!!!")
print("------- 중앙대학교 산업보안학과 이상 해킹캠프 -------")

while(len(win_list) < 10):
    rand_index = random.randint(0,len(name_list)-1)
    tmp_name = name_list[rand_index]
    
    if tmp_name not in win_list:
        win_list.append(tmp_name)
        
for i in range(3,0,-1):
    input()
    print("과연!! 꼬북칩의 주인은!! {}".format(i))
        
index = 1
for name in win_list:
    input()
    # print("test{}".format(index))
    print("{}번쨰 당첨자 : {}".format(index, name))
    index += 1
    
print()
print("축하드립니다~~")