"""
SDR DSP -- fill in the four functions below.

The real signal-processing math behind what the interactive tour's
Simulation tab does live: AM envelope detection and FM phase-difference
demodulation (the exact algorithms real SDR software like GQRX runs on
IQ samples), plus real ADS-B message field extraction -- the actual
bit layout dump1090 parses on every Mode S Extended Squitter message.

Run the tests as you go:  pytest exercises/test_sdr_dsp.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""

import math


def am_envelope(i_samples, q_samples):
    """AM demodulation: the message is carried in the *magnitude* of the
    baseband IQ signal, so recovering it is just the magnitude of each
    complex sample -- sqrt(I^2 + Q^2). This is genuinely what an AM
    envelope detector computes, simplified to its core.

    >>> am_envelope([1, 0], [0, 1])
    [1.0, 1.0]
    """
    # TODO: return [math.sqrt(i*i + q*q) for i, q in zip(i_samples, q_samples)]
    raise NotImplementedError


def fm_instantaneous_freq(i_samples, q_samples, fs):
    """FM demodulation: the message is carried in the *phase* of the
    baseband IQ signal, so recovering it means measuring how fast the
    phase is changing between consecutive samples -- a phase-difference
    discriminator, the same technique real FM demodulators use.

    Steps: compute each sample's phase with atan2(Q, I), take the
    difference between consecutive phases, wrap that difference into
    [-pi, pi] (phase wraps around), then scale by fs / (2*pi) to turn
    a phase-per-sample into a frequency in Hz. The very first sample
    has no previous phase to diff against -- copy the second value into
    it rather than leaving a spurious 0.

    >>> fm_instantaneous_freq([1, 0, -1, 0], [0, 1, 0, -1], 8)
    [2.0, 2.0, 2.0, 2.0]
    """
    # TODO: build the phases list with math.atan2, then for n >= 1 compute
    # d = phases[n] - phases[n-1], wrap d into [-pi, pi] with a while loop
    # (add/subtract 2*pi), and append d * fs / (2*math.pi). Set index 0
    # equal to index 1 at the end.
    raise NotImplementedError


def adsb_downlink_format(hex_msg):
    """Every ADS-B / Mode S message's first byte encodes the Downlink
    Format (DF) in its top 5 bits. DF 17 means "ADS-B Extended
    Squitter" -- the message type this project actually decodes.

    >>> adsb_downlink_format("8D4840D6202CC371C32CE0576098")
    17
    """
    # TODO: parse hex_msg[0:2] as a hex byte, mask with 0xF8 to keep the
    # top 5 bits, then shift right by 3 to get them as a plain integer.
    raise NotImplementedError


def adsb_icao_address(hex_msg):
    """Bytes 2-4 of every ADS-B message (hex characters 2 through 7) are
    the transmitting aircraft's 24-bit ICAO address -- a fixed
    identifier for that specific airframe, byte-aligned right after the
    first byte's DF+CA fields.

    >>> adsb_icao_address("8D4840D6202CC371C32CE0576098")
    '4840D6'
    """
    # TODO: return hex_msg[2:8].upper()
    raise NotImplementedError
