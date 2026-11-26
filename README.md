# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun · u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dunz72/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/dunz72/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

An entry for the [Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) bounty on make.fun: one original line, at most 160 characters, a deadpan TV weather forecast for a city that does not exist — absurd, yet delivered as if read straight off the map by a real forecaster.

## The line

> In Bumbletown, expect a high of 23 degrees, scattered showers of confetti, and winds at 18 miles per hour, with visibility down to three confused pigeons.

Bumbletown gets the full broadcast treatment — a high temperature, confetti showers, a wind speed, and a visibility report measured in pigeons. The numbers make the imaginary place feel real; the pigeons make it funny. Delivered deadpan, exactly as a forecaster would.

## How to run

```sh
python3 main.py
```

`main.py` (stdlib only) validates the line in `entry.txt` is 1–160 characters, contains a concrete number, and is a single line, then copies it byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `./output/entry.txt` when that variable is unset), verifying the output is byte-identical by SHA-256.

## License

MIT — see [LICENSE](LICENSE).
