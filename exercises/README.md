# Exercises — SDR DSP

A hands-on companion to Lessons 1 and 3 in the interactive tour: the real signal-processing math behind
the IQ & Demodulation Simulator tab (AM envelope detection, FM phase-difference demodulation), plus real
ADS-B message field extraction — the actual bit layout `dump1090` parses on every message.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 7 failing tests — every function in `sdr_dsp.py` currently raises `NotImplementedError`.

## What to do

Open `sdr_dsp.py`. Implement in this order:

1. `am_envelope` — the actual math an AM envelope detector runs: magnitude of each IQ sample.
2. `fm_instantaneous_freq` — the phase-difference discriminator real FM demodulators use.
3. `adsb_downlink_format` — the first 5 bits of every ADS-B message, telling you the message type.
4. `adsb_icao_address` — the transmitting aircraft's fixed 24-bit identifier, byte-aligned right after
   the first byte.

The ADS-B test message (`8D4840D6202CC371C32CE0576098`) is a commonly-cited real Extended Squitter
example — DF 17, ICAO `4840D6` — not a fabricated string.

## When you're done

All 7 tests passing means you have real, reusable demodulation and message-parsing logic — the same
category of code the Simulation tab runs live, and the actual first step any ADS-B decoder (including
`dump1090` itself) takes on a raw message.
