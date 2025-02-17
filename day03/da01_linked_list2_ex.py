# 실습(명함 관리 프로그램)

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=',')
    while current.link != None:
        current = current.link
        print(current.data, end= '')
    print()

def makeList(namephone):
    global memory, head, current, pre
    printNodes(head)
    
    node= Node()
    node.data = namephone
    memory.append(node)
    if head == None : 
        head = node
        return
    if head.data[0]>namephone[0]: # 첫 번째 노드보다 작을 때
        node.link = head
        head = node
        return
    # 중간 노드로 삽입하는 경우
    current = head
    while current.link!= None:
        pre = current
        current = current.link
        if current.data[0]>namephone[0]:
            pre.link=node
            node.link=current
            return
    # 삽입하는 노드가 가장 큰 경우
    current.link = node

## 전역 변수 선언 부분 
memory=[]
head,current,pre =None,None,None
dataArray = [["가마","010-1234-5678","645"], ["가나", "010-1111-2222"], ["다","010-3333-4444"],
             ["라","010-5555-6666"], ["마", "010-7777-8888"], ["바", "010-9999-9999"]
            ]

if __name__ == "__main__":
    for data in dataArray:
        makeList(data)

    printNodes