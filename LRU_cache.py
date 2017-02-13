"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# http://www.cnblogs.com/zuoyuan/p/3701572.html
class Node:　　　　　　　　　　　　　　　　　　#双向链表中节点的定义
    def __init__(self,k,x):
        self.key=k
        self.val=x
        self.prev=None
        self.next=None

class DoubleLinkedList: #双向链表是一个表头，head指向第一个节点，tail指向最后一个节点
    def __init__(self):
        self.tail=None
        self.head=None
        
    def isEmpty():　　　　　　　　#如果self.tail==None，那么说明双向链表为空
        return not self.tail

    def removeLast(self):　 　　　#删除tail指向的节点
        self.remove(self.tail)
        
    def remove(self,node): 　　　 #具体双向链表节点删除操作的实现
        if self.head==self.tail:
            self.head,self.tail=None,None
            return
        if node == self.head:
            node.next.prev=None
            self.head=node.next
            return
        if node ==self.tail:
            node.prev.next=None
            self.tail=node.prev
            return
        node.prev.next=node.next
        node.next.prev=node.prev

    def addFirst(self,node):　#在双向链表的第一个节点前面再插入一个节点　　
        if not self.head:
            self.head=self.tail=node
            node.prev=node.next=None
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        node.prev=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity　 #LRU Cache的容量大小　　　　　　　　　　　　　
        self.size=0　　　　　　　#LRU Cache目前占用的容量
        #dict为文章中提到的hashmap，加快搜索速度，{key：对应节点的地址}
        self.P=dict()
        self.cache=DoubleLinkedList()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.P) and self.P[key]:　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　#将key对应的指针指向的节点删除
            self.cache.addFirst(self.P[key])　　#然后将这个节点添加到双向链表头部
            return self.P[key].val　　　　　　　#并返回节点的value
        else: return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.P:　　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　  #先删掉key对应的节点
            self.cache.addFirst(self.P[key])　　#然后将这个节点插入到表的头部
            self.P[key].val=value　　　　　　　 #将这个节点的值val改写为value
        else:　　　　　　　　　　　　　　　　　#如果key不在字典中
            node=Node(key,value)　　　　　　　#新建一个Node节点，val值为value
            self.P[key]=node　　　　　　　　 #将key和node的对应关系添加到字典中
            self.cache.addFirst(node)　　　　#将这个节点添加到链表表头
            self.size +=1　　　　　　　　　　#容量加1
            #如果链表的大小超过了缓存的大小，删掉最末尾的节点，
            if self.size > self.capacity:
                #并同时删除最末尾节点key值和末节点在字典中的对应关系
                self.size -=1 
                del self.P[self.cache.tail.key]
                self.cache.removeLast()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
