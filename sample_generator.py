import random

def sample_generator(start_number, stop_number, training_number):
    samples = []

    for i in range(start_number, stop_number):
        samples.append('{} + {} = {}'.format(i, training_number, i + training_number))

    return samples

def add_one():
    add_one_samples = []

    #1
    add_one_samples.append(sample_generator(1, 1 + 10, 1))
    samples = sample_generator(7, 7 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)
    add_one_samples.append(sample_generator(10, 10 + 10, 1))

    #2
    add_one_samples.append(sample_generator(16, 16 + 10, 1))
    samples = sample_generator(24, 24 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)
    add_one_samples.append(sample_generator(30, 30 + 10, 1))

    #3
    add_one_samples.append(sample_generator(37, 37 + 10, 1))
    samples = sample_generator(45, 45 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)
    add_one_samples.append(sample_generator(55, 55 + 10, 1))

    #4
    samples = sample_generator(63, 63 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)
    add_one_samples.append(sample_generator(75, 75 + 10, 1))
    samples = sample_generator(81, 81 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)

    #5
    samples = sample_generator(90, 90 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)
    add_one_samples.append(sample_generator(96, 96 + 10, 1))
    samples = sample_generator(100, 100 + 10, 1)
    random.shuffle(samples)
    add_one_samples.append(samples)

    print(add_one_samples)
    return add_one_samples

if __name__ == '__main__':
    add_one()