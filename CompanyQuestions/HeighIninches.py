class Solution:
    def __init__(self, height_cm):
        self.height_cm = height_cm
        self.height_inches, self.height_feet = self.convert_height()

    
    def convert_height(self):
        # convert the height from cm to inches and feet
        inches = self.height_cm / 2.54
        feet = inches / 12
        return inches, feet
    

s2 =Solution(180)
print(f"Height in inches: {s2.height_inches : 2f}")
print(f"Height in inches: {s2.height_feet : 2f}")