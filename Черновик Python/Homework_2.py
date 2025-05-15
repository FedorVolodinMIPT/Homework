import cmath
from math import pi, log2
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def bit_reverse(x, bits):
    b = '{:0{width}b}'.format(x, width=bits)
    return int(b[::-1], 2)


def FFT(P):
    n = len(P)
    size = 1
    while size < n:
        size <<= 1
    P += [0] * (size - n)

    bits = int(log2(size))
    for i in range(size):
        j = bit_reverse(i, bits)
        if i < j:
            P[i], P[j] = P[j], P[i]

    m = 2
    while m <= size:
        half_m = m // 2
        w_m = cmath.exp(-2j * pi / m)
        for i in range(0, size, m):
            w = 1+0j
            for j in range(half_m):
                u = P[i + j]
                t = w * P[i + j + half_m]
                P[i + j]          = u + t
                P[i + j + half_m] = u - t
                w *= w_m
        m <<= 1

    return P


def IFFT(P):
    n = len(P)
    size = 1
    while size < n:
        size <<= 1
    P += [0] * (size - n)

    for i in range(size):
        P[i] = P[i].conjugate()

    FFT(P)

    return [round((P[i].conjugate().real) / size) for i in range(size)]


def filter_fft(input_wav, cutoff, kind = 'low'):
    sr, samples = wavfile.read(input_wav)
    orig_dtype = samples.dtype
    if samples.ndim == 2:
        samples = samples.mean(axis=1)

    N_orig = samples.shape[0]

    complex_signal = [complex(s) for s in samples]
    spectrum = FFT(complex_signal.copy())
    N = len(spectrum)

    freqs = np.arange(N) * sr / N
    freqs[N//2 + 1 :] -= sr

    if kind == 'low':
        mask = [1.0 if abs(f) <= cutoff else 0.0 for f in freqs]
    elif kind == 'high':
        mask = [0.0 if abs(f) <= cutoff else 1.0 for f in freqs]
    else:
        raise ValueError("kind must be 'low' or 'high'")

    filtered_spectrum = [s * m for s, m in zip(spectrum, mask)]

    recovered = IFFT(filtered_spectrum.copy())
    recovered = np.array(recovered[:N_orig], dtype=orig_dtype)

    out_name = f"{kind}_filtered_{input_wav}"
    wavfile.write(out_name, sr, recovered)

    fig, axes = plt.subplots(3, 1, figsize=(10, 8))

    axes[0].plot(samples, linewidth=0.5)
    axes[0].set_title("Original Waveform")

    half = N // 2
    axes[1].plot(freqs[:half], np.abs(spectrum[:half]), linewidth=0.5)
    axes[1].set_title("Original Spectrum")

    axes[2].plot(freqs[:half], np.abs(filtered_spectrum[:half]), linewidth=0.5)
    axes[2].set_title(f"Filtered Spectrum ({kind}-pass)")

    plt.tight_layout()
    plt.show()

    return recovered

low_passed = filter_fft('welcome-to-Mars.wav', cutoff=1000, kind='low')
high_passed = filter_fft('welcome-to-Mars.wav', cutoff=1000, kind='high')