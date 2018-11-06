import requests
import json


def main():
    r = requests.post("http://127.0.0.1:5000/distance", json= {"a": [2, 4], "b": [5,6]})
    sum_result = r.json()
    print(sum_result)
    print("The response was {0}.".format(sum_result['distance']))


if __name__ == "__main__":
    main()

