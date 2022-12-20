# For the explanation of the problem please check the question link.
# Question link: https://leetcode.com/problems/keys-and-rooms/
# To follow the solving process please follow the steps.
# The steps are represented in parentheses, as (1),(2)...

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # (1) To check if a room is already visited, create a list of visited rooms for each room in rooms[].
        # False: room is not visited yet, True: room is visited before
        visitedRooms = [False] * len(rooms)
        visitedRooms[0] = True # Since we always start with 0th room, we set it to True

        # (3) Create a stack to hold the keys that are present inside a room
        stackKeys = []
        stackKeys.append(0) # Adding the 0th room key since we start with that, we have the key 0
        # Since every key is going to be used for a room, loop until stack is empty
        while len(stackKeys) > 0:
            currentKey = stackKeys.pop()
            # This key represent a room in rooms[], so look inside that room to see which keys it has
            for newKey in rooms[currentKey]:
                if visitedRooms[newKey] == False: # If the room is already visited, no need to append key to stack
                    visitedRooms[newKey] = True # Set the room to visited(True) since we found that room's key
                    stackKeys.append(newKey)
        
        # (2) If there is at least one room that is not visited, return False
        # If all of them are True(i.e visited/can be visited) return True
        # The (3)rd step will reassing each value in visitedRooms
        for room in visitedRooms:
            if not room:
                return False
        return True