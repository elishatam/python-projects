def is_prime(number):
    """Return True if number is prime"""
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*"""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

# app = Flask(__name__)
#
# def highest_random(limit):
#     highest = 0
#     for i in range(5):
#         r = randint(0, limit)
#         if r > highest:
#             highest = r
#
#     msg = 'Hello {num:d}'.format(num-highest)
#     return msg
#
# @app.route('/')
# def hello_world():
#     upper_limit = 100
#     msg = highest_random(upper_limit)
#     return msg
#
# if __name__ == '__main__':
#     app.run(debug=True)

