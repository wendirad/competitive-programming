class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        to_kelvin = lambda cel: cel + 273.15
        to_fahrenheit = lambda cel: cel * 1.80 + 32.00

        return [to_kelvin(celsius), to_fahrenheit(celsius)]