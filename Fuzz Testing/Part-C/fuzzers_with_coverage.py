import random
import utils
from num2words import num2words 
from fuzzingbook.Fuzzer import RandomFuzzer
from fuzzingbook.MutationFuzzer import MutationFuzzer

studentID = 40062066
random.seed(studentID) # to fix the randomness
trials = 300
fuzzer = MutationFuzzer(seed = ["3452020"])
random_fuzzer = RandomFuzzer()

def getMutationCoverage():
    input_set = []
    for i in range(0, trials):
        input_set.append(fuzzer.fuzz())
    return utils.calculate_cumulative_coverage(input_set, num2words)


def getRandomCoverage():
    input_set = []
    for i in range(0, trials):
        input_set.append(random_fuzzer.fuzz())
    return utils.calculate_cumulative_coverage(input_set, num2words)