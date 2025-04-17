# Development Log
# Started at 2025-04-03 08:49:13

# Fixed some bugs
# Added documentation

import json

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Update at 2025-04-04 04:34:04
# Fixed some bugs
# Added unit tests


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Update at 2025-04-05 07:44:02
# Added some random functionality
# Added documentation
# Updated the code with new features
import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Update at 2025-04-06 05:09:08
# Optimized the algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Update at 2025-04-07 01:21:08
# This is a random comment


import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Update at 2025-04-08 04:27:06
# Fixed some bugs
# Improved performance

from datetime import datetime, timedelta

def get_date_range(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list

# Update at 2025-04-08 15:28:07
# Added error handling

from datetime import datetime, timedelta

def get_date_range(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list

# Update at 2025-04-09 01:40:04
# Optimized the algorithm

from PIL import Image

def resize_image(image_path, size):
    with Image.open(image_path) as img:
        resized = img.resize(size)
        return resized

def convert_to_grayscale(image_path):
    with Image.open(image_path) as img:
        return img.convert('L')

# Update at 2025-04-10 04:56:09
# Added unit tests
# Improved performance

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Update at 2025-04-11 02:18:12
# Optimized the algorithm


import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def extract_phone_numbers(text):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)

# Update at 2025-04-12 14:36:04
# Refactored the code


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Update at 2025-04-13 02:46:07
# Improved performance


def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_file_lines(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

# Update at 2025-04-13 15:17:07
# Updated the code with new features
# Added some random functionality
# Added documentation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Update at 2025-04-14 10:42:12
# Improved performance
# Added some random functionality


import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Update at 2025-04-15 08:24:09
# Added documentation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Update at 2025-04-16 11:55:08
# Added unit tests
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Update at 2025-04-17 13:17:11
# Added documentation
# Fixed some bugs
# Updated the code with new features
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True