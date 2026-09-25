# 📖 Lesson Plan — RTL-SDR-Receiver

> **Chain K — Hardware & Systems Foundations** | A $30 USB dongle that receives real radio signals —
> decode aircraft transponders, weather satellite images, and FM radio. License-free, receive-only.

## What This Project Is

Turn "radio" from a sealed black box into something you can actually see: raw RF comes in over USB, and
software does the demodulation a dedicated chip would normally hide from you. Start with the simplest
possible signal (FM broadcast), then decode two genuinely useful real-world signals — aircraft ADS-B
transponders and NOAA weather satellite images — with the exact same $30 dongle.

## Learning Objectives

By the end I can:

1. Explain what IQ sampling is and why software, not a dedicated chip, does the actual demodulation.
2. Receive and demodulate a real FM broadcast signal with GQRX.
3. Decode real aircraft ADS-B transponder messages with `dump1090`, and extract a message's Downlink
   Format and ICAO address by hand from the raw bits.
4. Receive and decode a NOAA weather satellite APT pass, and explain why antenna choice changes
   reception more than almost anything else in this project.

## Software You Will Use

- **GQRX** (or SDR#) — general-purpose SDR receiver software; tunes, demodulates, and plays audio.
- **dump1090** — decodes ADS-B aircraft transponder messages from raw IQ samples.
- **noaa-apt** (or WXtoIMG) — decodes a recorded NOAA APT audio pass into an actual image.
- **rtl_433** — decodes a wide range of simple 433MHz ISM-band devices (weather stations, sensors);
  mentioned for context, not required for the core build order.

## Build Order

1. Install RTL-SDR drivers and GQRX; tune to a strong local FM broadcast station and confirm audio.
   🔗 [rtl-sdr.com — A Good Quickstart Guide for RTL-SDR Linux Users](https://www.rtl-sdr.com/a-good-quickstart-guide-for-rtl-sdr-linux-users/)
2. Explore GQRX's waterfall display; identify a few other signal types (narrowband FM, AM, digital
   bursts) just by their visual "shape" before demodulating anything.
   🎥 [RTL-SDR on Raspberry Pi 3 B+ with GQRX](https://www.youtube.com/watch?v=7pgCC4cqgTc) (TheSmokinApe Ham Radio)
3. Install and run `dump1090`; watch real aircraft appear, then manually decode one raw message's
   Downlink Format and ICAO address by hand and check it against `dump1090`'s own output.
   🎥 [How To Install Dump1090, FlightAware, And More On A Raspberry Pi](https://www.youtube.com/watch?v=J6JlKbOE7_A) (Fuzz The Pi Guy)
4. Build or buy a 137MHz-matched antenna, capture a NOAA APT pass, and decode it into an image.
   🎥 [How To Receive Images Directly From NOAA Satellites](https://www.youtube.com/watch?v=PWWGDL5tC_I) (Ham Radio Crash Course)

## Common Mistakes to Avoid

- Buying a generic "USB TV tuner" instead of a dongle explicitly sold as RTL-SDR — many use a different,
  incompatible tuner chip despite looking identical in photos.
- USB port RF noise swamping weak signals — a USB extension cable, keeping the dongle away from the
  computer itself, fixes most of this.
- Running an incompatible or generic dongle and blaming the software when reception is poor.
- A whip antenna with no ground plane underperforming badly indoors — the antenna, not the software or
  the dongle, is very often the actual limiting factor.
- Trying to decode ADS-B (1090MHz) or APT (137MHz) with a mismatched or wrong-band antenna and
  assuming the decoder software itself is broken.

## Check Your Understanding

The quiz covers IQ sampling and why demodulation is software-defined, ADS-B message structure (DF and
ICAO address extraction), why antenna matching matters more than almost any other single choice, and
diagnosing the common failure points above.

## Why This Matters (Industry Application)

RF/SDR skills are directly relevant to telecom, spectrum analysis, and security research (RF is a real
attack surface). It's also one of the fastest ways to make "invisible" infrastructure — flight tracking,
weather data, radio — visible and concrete, with a total hardware cost under $40.

## Reflection Questions

- What surprised you most about how much of "radio" turns out to be software, once you have raw IQ
  samples to work with?
- Why does a receive-only project like this carry no license requirement, while transmitting on the
  same frequencies would?
