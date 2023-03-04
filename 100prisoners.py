"""
Role the dice!
"""

from random import  shuffle


class Game:
    def __init__(self, size=100):
        self.size = size
        self.boxes = list(range(size))
        self.output = True

        self.sort_boxes()
        self.show()

    def sort_boxes(self):
        shuffle(self.boxes)

    def find_for_prisoner(self, person_id):
        attempts = 0
        next_id = person_id
        order = []
        while True:
            num_in_box = self.boxes[next_id]
            attempts += 1
            order.append(num_in_box)
            if num_in_box == person_id:
                if self.output:
                    print(f"Found person {person_id} in box {next_id} after {attempts} attempts")
                    print(f"      person {person_id} found via {order}")
                return True
            if attempts >= self.size/2:
                return False
            next_id = num_in_box

    def find_loops(self):
        boxes = list(self.boxes)
        loops = []

        for i in range(len(boxes)):
            next_id = i
            loop = []
            while True:
                num_in_box = boxes[next_id]
                if num_in_box is None:
                    break
                loop.append(num_in_box)
                # Mark box to be skipped next time!
                boxes[next_id] = None
                if num_in_box == i:
                    loops.append(loop)
                    loop = []
                    break
                next_id = num_in_box
        # Sort by loop length
        loops = [j for i, j in sorted([(len(l), l) for l in loops])]
        return loops

    def solve(self):
        for i in range(len(self.boxes)):
            if not self.find_for_prisoner(i):
                print("FAIL!")
                return False
        return True

    def show(self):
        b = list(self.boxes)
        r = 0
        width = 10

        def row(row_id, values):
            """ Show a single row """
            print(f"{row_id:>4} | ", end="")
            print("".join([f"{v:>4}" for v in values]))

        print("")
        # Show header (single digits)
        row("", range(width))
        # Show solid "-" visual breaker
        row("--", ("----",) * width)

        while r < self.size:
            row(r, self.boxes[r:r+width])
            r += 10
        print("")


if __name__ == "__main__":
    win = total = 0
    num_games = 1000
    for i in range(num_games):
        g = Game()

        # Less noisy
        g.output = False

        for i, loop in enumerate(g.find_loops()):
            print(f"Loop {i+1}:  Found {len(loop)} entries.   Loop={loop}")
        if g.solve():
            win +=1

    print(f"Total games {num_games}.   Won {win/num_games*100}%")

