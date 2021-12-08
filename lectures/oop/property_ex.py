class Person:
    def __init__(self, name):
        self.name = name

    @property
    def get_info(self):
        print(f'hello I am {self.name}')
        return 'Hello'


ted = Person('Ted')

print(ted.name)
print(ted.get_info)

class Flight:
    def __init__(self, segments):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)

    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, value):
        dest = self.segments[0].departure = value
        self.segments[0] = Segment(departure=value, destination=dest)


class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination


first = Segment('LWO', 'JFK')
second = Segment('KBP', 'WAW')
flight = Flight([first])
print(flight.departure_point)

# flight.segments[0].departure = 'KBP'
flight.departure_point = 'KBP'
print(flight.departure_point)

flight_2 = Flight([first, second])
print(flight_2.departure_point)
print(flight_2)

flight_2.departure_point = 'CAN'
print('Setting departure point to CAN')
print(flight_2.departure_point)
print(flight_2)
