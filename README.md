# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Keiiiiigo/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Keiiiiigo/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page newspaper front page summing up the world news of Monday 23 November 2026: Ukraine sinking a Russian warship off Libya, Nvidia bringing back Jensen Huang as CEO, NATO sending a radar plane to Poland, Trump's order to speed up federal executions, and the deadly candy factory fire in Indonesia. The image is drawn programmatically with Python (PIL) in `draw_image.py` so every headline is crisp, legible text — no AI-generated garble. It is stored in this repo as `entry.png.b64` (base64 text of the PNG) and `main.ts` decodes it back to `entry.png` at run time. Sources for each story are documented in `news-notes.md`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
