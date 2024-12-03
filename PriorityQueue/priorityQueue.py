import heapq

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))     # οταν κανω push tuple σε heap μεσω της heapq, βλεπει το πρωτο στοιχειο ως το priority
        self.count += 1

    def pop(self):
        self.count -= 1
        return heapq.heappop(self.heap)[1]

    def isEmpty(self):
        if self.count:
            return False
        else:
            return True

    def update(self, item, priority):                   # περναω ολο το pq σε εναν πινακα για να ελεγξω 1-1 τα στοιχεια του κ επειτα τα ξαναβαζω στο pq αλλαζοντας καταλληλα οποιο χρειαζεται 
        temp = []                                       # αμα δεν βρω καποιο στοιχειο ιδιο με το item και το flag μεινει false, προσθετω αυτο το στοιχειο στο pq
        flag = False
        while self.count != 0:
            item0 = self.pop()
            if item0[1] == item:
                flag = True
                if item0[0] > priority:
                    item0[0] = priority

            temp.apend(item0)

        for i in range(len(temp)):
            item0 = temp[i]
            self.push(item0[1], item0[0])

        if not flag:
            self.push(item, priority)


def PQSort(list):                                       # βαζω τα στοιχεια της λιστας σε ενα pq οριζοντας το priority τους ως το ιδιο το στοιχειο 
    pq = PriorityQueue()                                # ετσι οταν τα κανω pop σε μια νεα λιστα να ειναι ταξινομιμενα αυτοματα απ την pq
    list0 = []
    for i in list:
        pq.push(i, i)

    for i in range(len(list)):
        list0.append(pq.pop())

    return list0