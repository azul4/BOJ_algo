class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        res_str = "|"

        iterator = self.head
        while iterator is not None:
            res_str += f"{iterator.data} |"
            iterator = iterator.next

        return res_str

    def append(self, data):
        #새로운 링크드 리스트 노드 생성
        new_node = Node(data)

        #링크드 리스트가 비어있으면 head=tail=현재노드
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #링크드 리스트가 비어있지 않으면 기존 tail 노드 뒤에 new_node 삽입
        else:
            self.tail.next = new_node
            self.tail = new_node
    def insert(self, target_node, data):
        #삽입할 노드를 data로부터 생성
        new_node = Node(data)

        #tail node 다음에 삽입 (가장 끝에 추가)
        if self.tail is target_node:
            self.tail.next = new_node

            

        
li = LinkedList()
li.append(2)
li.append(5)
li.append(19)
li.insert(0,1)

print(li)
