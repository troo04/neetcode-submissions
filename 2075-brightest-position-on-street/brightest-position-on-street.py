class Solution:
    def brightestPosition(self, lights: list[list[int]]) -> int:
        light_counter = defaultdict(int)

        for pos, r in lights:
            light_counter[pos - r] += 1
            light_counter[pos + r + 1] -= 1
        
        light_counter = dict(sorted(light_counter.items()))

        total = 0

        best_pos = float('inf')
        max_lights = float('-inf')

        for pos in light_counter:
            total += light_counter[pos]

            if total > max_lights:
                max_lights = total
                best_pos = pos
        
        return best_pos