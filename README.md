# RTL-SDR-Receiver

### A $30 USB dongle that receives real radio signals — decode aircraft transponders, weather satellite images, and FM radio. License-free, receive-only.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

> ⬜ **Scaffold pending.** Directory created to portfolio standard; full content to be built. Part of **Chain K — Hardware & Systems Foundations**.

## Why This Was Built

Software-defined radio turns "radio" from a sealed black box into something you can actually see: raw RF
comes in over USB, and software does the demodulation a dedicated chip would normally hide from you. A
receiver has no transmit stage, so there's no license or legal risk — just an antenna, a $30 dongle, and
the actual radio spectrum around you.

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** an RTL-SDR dongle (the RTL2832U + R820T2 chipset combination is the de facto standard —
buy one explicitly sold as "RTL-SDR", not a cheap generic DVB-T TV tuner, which uses different tuner chips
with worse performance), a matched antenna (a basic telescopic whip covers FM/ADS-B reasonably; a dedicated
1090MHz antenna does ADS-B much better), and a USB extension cable (keeps the dongle away from computer
RF noise).

**What to look for:** buy from a vendor explicitly selling "RTL-SDR Blog" branded dongles or equivalent —
these are the ones the open-source SDR community actually tests against and documents. TCXO
(temperature-compensated crystal) versions drift less in frequency and are worth the small premium.

**Red flags:** unbranded "USB TV tuner" listings with no mention of RTL2832U/R820T2 — many are a different,
incompatible chipset despite looking identical in photos.

**Common failure points:** USB port RF noise swamping weak signals (the extension cable fixes this),
running an incompatible/generic dongle and blaming the software, and a whip antenna with no ground plane
underperforming badly indoors.

## Signal Chain Diagram

Not a wiring diagram in the usual sense — there's nothing to solder — but the same idea: antenna → dongle
→ computer over a USB extension (keeps the dongle away from the computer's own RF noise) → SDR software
does the actual demodulation:

![RTL-SDR signal chain diagram](docs/diagrams/wiring.svg)

## Parts & Pricing

Pulled from the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#rtl-sdr-receiver) — check
there for current links; prices drift. **Budget/Mid/Luxury are the same tiers the shopping list calls
Budget/Mid/Premium.**

| Item | Budget | Mid | Luxury |
|---|---|---|---|
| Dongle | [RTL-SDR Blog V4, ~$30](https://www.amazon.com/RTL-SDR-Blog-RTL2832U-Software-Defined/dp/B0F6MQ5N5W) | Same dongle + antenna bundle, ~$40 | Same dongle + dedicated 1090MHz ADS-B antenna, ~$25–40 extra — serious aircraft tracking |
| USB extension | Any basic 3–6ft cable, ~$6–8 | Same | Same — not worth tiering |

Running total: **~$36–38 budget → ~$95–110 luxury**. This is genuinely the cheapest real project in the
whole chain — the budget tier is the correct answer here, not a compromise, per the buying guide above.

## Why This Matters (Industry Application)

RF/SDR skills are directly relevant to telecom, spectrum analysis, and security research (RF is a real
attack surface). It's also one of the fastest ways to make "invisible" infrastructure — flight tracking,
weather data, radio — visible and concrete.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| SDR fundamentals | Sampling, IQ data, and demodulation basics |
| ADS-B | Decoding real aircraft transponder signals |
| APT/weather sats | Receiving and decoding NOAA satellite images |
| FM/AM | The simplest demodulation to start with |
| Antennas | Why a matched antenna changes everything |
| Tooling | GQRX, rtl_433, dump1090 and the SDR software ecosystem |

## How This Connects

Chain K (Hardware & Systems Foundations). Shares RF/antenna fundamentals with **Walkie-Talkie-Build**
and **Cyberdeck-Cellular-And-Media**; the safest, cheapest entry point into RF for anyone new to it.

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
