#!/usr/bin/env python3
import sys
import random

def get_weather(city):
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Snowy"]
    return {
        "city": city,
        "temp": random.randint(-5, 35),
        "condition": random.choice(conditions),
        "humidity": random.randint(30, 90)
    }

def main():
    city = sys.argv[1] if len(sys.argv) > 1 else "Shanghai"
    data = get_weather(city)
    print(f"Weather in {data['city']}:")
    print(f"  Temperature: {data['temp']}C")
    print(f"  Condition: {data['condition']}")
    print(f"  Humidity: {data['humidity']}%")

if __name__ == "__main__":
    main()
