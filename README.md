# The World in One Image — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/1Serv0x/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/1Serv0x/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A single-page newspaper front page that sums up one day of world
news in one picture. Every mark on the page is drawn in code: there
are no photographs, no downloaded images and no pasted-in graphics.

## What is on the page

The front page leads with the US–Iran talks stalling over uranium,
then covers the strikes in Yemen and the Houthi response, the
EU–Britain reset deal, the COP31 deadlock over fossil fuels, and
the Wall Street slide on the AI selloff. A short strip at the foot
catches the Peru earthquake, the SpaceX Dragon leaving the station,
the FBI database-breach probe and the India–New Zealand Test.

## How to run it

```sh
python3 main.py
```

That writes `entry.png` (1024 × 1024) next to the script. The only
dependency is Pillow, and the only input is the list of stories
written into the script itself.

## How it is drawn

The page is built from a small set of drawing helpers: a text
wrapper, a headline and paragraph setter, a kicker and rule, a
globe illustration for the lead story, and a three-column story
grid. Colours are a restrained newsprint palette — paper white,
ink black, red, navy and teal — so the page reads like a paper
rather than a poster.

## Why one image

A front page forces choices: one lead, three stories with room to
breathe, and a strip for everything else. The 21st was a day of
stalled talks — in Geneva, at COP31, and on the markets — so the
page leans into that mood: big sober headlines, one diagram, and
no decoration that does not earn its place.
