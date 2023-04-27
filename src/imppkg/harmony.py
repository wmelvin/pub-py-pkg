import sys

import termcolor

from imppkg.harmonic_mean import harmonic_mean


def main():
    # TODO: Some input validation (maybe?)
    nums = [float(arg) for arg in sys.argv[1:]]
    termcolor.cprint(harmonic_mean(nums), "red", "on_yellow", attrs=["bold"])
