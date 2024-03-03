class QueueError(LookupError):  # Choose base class for the new exception.
    pass


class Queue:

    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.insert(0, elem)

    def get(self):
        if self.__queue_list:
            return self.__queue_list.pop()
        else:
            raise QueueError

    def peek(self):
        if self.__queue_list:
            return self.__queue_list[-1]
        else:
            raise QueueError


class SuperQueue(Queue):
#    def __init__(self):
#        Queue.__init__(self)

    def isempty(self):
        return len(self._Queue__queue_list) == 0

        # try:
        #     Queue.peek(self)
        #     return False
        # except QueueError:
        #     return True

#que = Queue()
#que.put(1)
#que.put("dog")
#que.put(False)
#try:
#    for i in range(4):
#        print(que.get())
#except:
#    print("Queue error")

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")