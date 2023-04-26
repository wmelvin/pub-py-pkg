import sys

from imppkg.harmonic_mean import harmonic_mean


def main():
    # TODO: Some input validation (maybe?)
    nums = [float(arg) for arg in sys.argv[1:]]
    print(harmonic_mean(nums))
