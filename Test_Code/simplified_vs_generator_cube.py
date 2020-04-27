def cube(n):
    return n ** 3


def simplified_generator(n):
    generated_results = []
    current_number = 1
    while current_number <= n:
        generated_results.append(cube(current_number))
        current_number += 1
    return generated_results


def generated_using_yield(n):
    current_number = 1
    while current_number <= n:
        yield cube(current_number)
        current_number += 1


print(simplified_generator(10))
generatedValues = generated_using_yield(10)
print([i for i in generatedValues])
