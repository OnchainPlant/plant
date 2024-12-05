import random
import time

class AIPlantGrowthSimulator:
    def __init__(self, water_frequency=24, fertilize_frequency=72):
        self.water_frequency = water_frequency  # in hours
        self.fertilize_frequency = fertilize_frequency  # in hours
        self.growth_stage = 0  # 0: Seed, 1: Sprout, 2: Full Growth
        self.last_watered = time.time()
        self.last_fertilized = time.time()

    def water_plant(self):
        self.last_watered = time.time()
        print("The plant has been watered!")
        self._grow_plant()

    def fertilize_plant(self):
        self.last_fertilized = time.time()
        print("The plant has been fertilized!")
        self._grow_plant()

    def _grow_plant(self):
        if self.growth_stage == 0:
            # Seed to sprout
            if random.random() > 0.5:
                self.growth_stage = 1
                print("The plant has sprouted!")
        elif self.growth_stage == 1:
            # Sprout to full growth
            if random.random() > 0.7:
                self.growth_stage = 2
                print("The plant is fully grown!")
        else:
            print("The plant is fully grown and cannot grow further!")

    def simulate_growth(self):
        # Randomly decide if plant grows based on watering and fertilizing frequency
        current_time = time.time()
        if current_time - self.last_watered > self.water_frequency * 3600:
            self.water_plant()
        if current_time - self.last_fertilized > self.fertilize_frequency * 3600:
            self.fertilize_plant()

# Example of usage
plant = AIPlantGrowthSimulator()
plant.simulate_growth()  # This would run periodically based on real time conditions
