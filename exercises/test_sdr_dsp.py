"""
Tests for sdr_dsp.py. Values independently verified with a reference
implementation before being written here. The ADS-B test message is a
commonly-cited real Extended Squitter example (DF 17, ICAO 4840D6).
"""
import pytest

from sdr_dsp import (
    am_envelope,
    fm_instantaneous_freq,
    adsb_downlink_format,
    adsb_icao_address,
)


def test_am_envelope_unit_samples():
    assert am_envelope([1, 0], [0, 1]) == [1.0, 1.0]


def test_am_envelope_scaled_samples():
    result = am_envelope([2, 0, 0.5], [0, 2, 0.5])
    assert result == pytest.approx([2.0, 2.0, 0.7071067811865476])


def test_fm_instantaneous_freq_constant_rotation():
    i = [1, 0, -1, 0, 1, 0, -1, 0]
    q = [0, 1, 0, -1, 0, 1, 0, -1]
    result = fm_instantaneous_freq(i, q, 8)
    assert result == pytest.approx([2.0] * 8)


def test_fm_instantaneous_freq_first_sample_not_spurious():
    i = [1, 0, -1, 0]
    q = [0, 1, 0, -1]
    result = fm_instantaneous_freq(i, q, 8)
    assert result[0] == pytest.approx(result[1])


def test_adsb_downlink_format_extended_squitter():
    assert adsb_downlink_format("8D4840D6202CC371C32CE0576098") == 17


def test_adsb_icao_address_known_message():
    assert adsb_icao_address("8D4840D6202CC371C32CE0576098") == "4840D6"


def test_adsb_icao_address_lowercase_input_normalizes():
    assert adsb_icao_address("8d4840d6202cc371c32ce0576098") == "4840D6"
