import fuzzers_with_coverage as cov
import utils
import matplotlib.pyplot as plt


plt.title('Coverage')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')

randomCoverage = cov.getRandomCoverage()
print(randomCoverage)
plt.plot(randomCoverage)
mutationCoverage = cov.getMutationCoverage()
print(mutationCoverage)
plt.plot(mutationCoverage)
plt.legend(["Random Fuzzer Coverage", "Mutation Fuzzer Coverage"])
plt.show()