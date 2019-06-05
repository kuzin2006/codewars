class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(queue) for queue in queues]  # to make queues mutable
        self.capacity = capacity
        pass

    def theLift(self):
        lift_path = [0]  # current lift load
        lift_path_up = []  # floors to stop on the way up
        lift_path_down = []  # floors to stop on the way down
        floors_queues = [len(i) for i in self.queues]  # passengers orders
        lift_passengers = [0 for i in range(0, len(self.queues))]  # passengers in lift going to i floor
        while sum(floors_queues) != 0:
            lift_path_up = []
            lift_path_down = []
            for floor in range(0, len(self.queues)):  # going UP
                if lift_passengers[floor]:  # somebody in the lift goes here
                   lift_passengers[floor] = 0   # all came out
                if self.queues[floor]:  # somebody wants to go, gonna stop, if anyone goes up
                    self.queues[floor].sort()  # order passengers
                    i = 0
                    while len(self.queues[floor]) > 0 and sum(lift_passengers) < self.capacity:
                        if self.queues[floor][-1] > floor:  # take the passenger...
                            if floor not in lift_path_up:  # ...and add floor to the path
                                lift_path_up.append(floor)
                            if self.queues[floor][-1] not in lift_path_up:
                                lift_path_up.append(self.queues[floor][-1])
                            floors_queues[floor] -= 1
                            lift_passengers[self.queues[floor][-1]] += 1  # passenger came into lift
                            self.queues[floor].pop()  # passenger came out of queue
                        else:
                            i += 1
                        if i > len(self.queues[floor]):  # no suitable orders left
                            break
            lift_path_up.sort()  # all orders given

            if sum(floors_queues) != 0:  # if orders left - going down
                for floor in range(len(self.queues)-1, -1, -1):  # going DOWN
                    if lift_passengers[floor]:  # somebody in the lift goes here
                       lift_passengers[floor] = 0   # all came out
                    if self.queues[floor]:  # somebody wats to go, gonna stop

                        self.queues[floor].sort(reverse=True)  # order passengers
                        i = 0
                        while len(self.queues[floor]) > 0 and sum(lift_passengers) < self.capacity:
                            if self.queues[floor][-1] < floor:  # take the passenger
                                if floor not in lift_path_down:
                                    lift_path_down.append(floor)
                                if self.queues[floor][-1] not in lift_path_down:
                                    lift_path_down.append(self.queues[floor][-1])
                                floors_queues[floor] -= 1
                                lift_passengers[self.queues[floor][-1]] += 1  # passenger came into lift
                                self.queues[floor].pop()  # passenger came out of queue
                            else:
                                i += 1
                            if i > len(self.queues[floor]):  # no suitable orders left
                                break
                lift_path_down.sort(reverse=True)  # all orders given
            #if lift_path_up[-1] == lift_path_down[0]:
            #    lift_path += lift_path_up + lift_path_down[1:]
            #else:
            for cmd in lift_path_up+lift_path_down:
                if cmd != lift_path[-1]:
                    lift_path.append(cmd)

            # lift_path += lift_path_up + lift_path_down

        if lift_path[-1] != 0:
            lift_path += [0]  # go down if no orders left

        return lift_path

# Floors:    G     1      2        3     4      5      6         Answers:
tests = [[ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
         [ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
         [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
         [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ]]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    print(lift.theLift(), answer, "\n")