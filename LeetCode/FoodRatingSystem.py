from collections import defaultdict
import heapq
class FoodRating(object):
    def __init__(self, foods, cuisines, rating):
        self.cuisine_in_heap = defaultdict(list)
        self.food_in_cuisines = {}
        self.food_rating = defaultdict(int)

        for i in range(len(foods)):
            self.food_in_cuisines[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_to_heap[cuisines[i]], (-rating[i], foods[i]))
            self.food_rating[foods[i]] = -rating[i]


    def changeRating(self, food , newRating):
        cuisine = self.food_in_cuisines[food]
        heapq.heappush(self.cuisine_in_heap[cuisine], (-newRating, food))
        self.food_rating[food] = -newRating

    
    def highestRating(self, cuisine):
        smallest_lexico = None
        while len(self.cuisine_in_heap[cuisine]) > 0:
            curr = self.cuisine_in_heap[cuisine][0]

            if curr[0] != self.food_rating[curr[1]]:
                heapq.heappop(self.cuisine_in_heap[cuisine])
                continue
            smallest_lexico = curr[1]
            break
        return smallest_lexico