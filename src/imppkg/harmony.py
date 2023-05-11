import sys

from termcolor import cprint

from imppkg.harmonic_mean import harmonic_mean


def main():
    result = 0.0

    try:
        nums = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        harmonic_mean(nums)
    except ZeroDivisionError:
        pass

    cprint(result, "red", "on_yellow", attrs=["bold"])
