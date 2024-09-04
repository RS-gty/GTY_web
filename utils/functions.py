from data.data import *


def peak(data: list, threshold=0):
    peaks = []
    for i in range(len(data)-2):
        if data[i+2] < data[i+1] > data[i] and data[i+1] >= threshold:
            peaks.append(data[i+1])
    return peaks
