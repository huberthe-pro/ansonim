from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1200
HEIGHT = 630
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "og" / "why-i-built-agentsmail.png"


def load_font(path: str, size: int):
    return ImageFont.truetype(path, size=size)


font_sans_bold = load_font("/System/Library/Fonts/Supplemental/Verdana Bold.ttf", 62)
font_sans = load_font("/System/Library/Fonts/Supplemental/Verdana.ttf", 20)
font_sans_small = load_font("/System/Library/Fonts/Supplemental/Verdana.ttf", 18)
font_mono = load_font("/System/Library/Fonts/SFNSMono.ttf", 24)
font_mono_small = load_font("/System/Library/Fonts/SFNSMono.ttf", 20)


img = Image.new("RGB", (WIDTH, HEIGHT), "#081015")
draw = ImageDraw.Draw(img)

# Background gradient glow
glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse((650, -60, 1280, 540), fill=(7, 203, 176, 55))
gdraw.ellipse((-140, 220, 520, 860), fill=(67, 216, 255, 35))
gdraw.ellipse((760, 320, 1350, 900), fill=(57, 255, 20, 20))
glow = glow.filter(ImageFilter.GaussianBlur(70))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
draw = ImageDraw.Draw(img)

# Grid
for x in range(0, WIDTH, 40):
    draw.line((x, 0, x, HEIGHT), fill="#10252a", width=1)
for y in range(0, HEIGHT, 40):
    draw.line((0, y, WIDTH, y), fill="#10252a", width=1)

# Border frame
draw.rounded_rectangle((24, 24, WIDTH - 24, HEIGHT - 24), radius=24, outline="#1a4047", width=2)

# Left rail / eyebrow
draw.rounded_rectangle((58, 52, 278, 92), radius=10, fill="#0c1a1f", outline="#1a4047", width=2)
draw.text((78, 64), "ANSON.IM / BLOG", font=font_mono_small, fill="#55f0d2")

# Headline
draw.text((62, 130), "Why I Built", font=font_sans_bold, fill="#effffb")
draw.text((62, 202), "AgentsMail", font=font_sans_bold, fill="#57f2cf")
draw.text((62, 292), "The 19-Step Gmail Nightmare", font=font_sans, fill="#a6d8d0")

# Supporting copy
copy = [
    "Gmail asked an AI agent to survive",
    "OAuth, 2FA, redirect URIs,",
    "refresh tokens, and security warnings.",
    "Agents need mailboxes of their own.",
]
y = 352
for line in copy:
    draw.text((64, y), line, font=font_sans, fill="#d8f3ec")
    y += 29

# CTA pill
draw.rounded_rectangle((62, 535, 332, 578), radius=14, fill="#0d2527", outline="#2ce1c3", width=2)
draw.text((84, 548), "One POST. No OAuth.", font=font_mono_small, fill="#7affea")

# Terminal card
panel = (720, 78, 1125, 548)
draw.rounded_rectangle(panel, radius=24, fill="#0b1418", outline="#1f4a52", width=2)
draw.rounded_rectangle((740, 108, 1105, 508), radius=18, fill="#071014", outline="#173740", width=1)

# Window dots
for i, color in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
    x = 752 + i * 20
    draw.ellipse((x, 122, x + 10, 132), fill=color)

# Terminal title
draw.text((840, 120), "agent-mailbox", font=font_mono_small, fill="#5ed8cd")

# Nightmare steps
steps = [
    "01  Google Cloud project",
    "02  OAuth consent screen",
    "03  Redirect URIs",
    "04  Refresh tokens",
    "05  2FA",
    "06  Security warning",
    "...",
    "19  give up",
]
sy = 168
for idx, step in enumerate(steps):
    color = "#f6876b" if idx < 6 or step == "19  give up" else "#8aa3a8"
    draw.text((764, sy), step, font=font_mono_small, fill=color)
    sy += 31

# Divider and success block
draw.line((760, 408, 1086, 408), fill="#173740", width=2)
draw.text((764, 430), "POST /api/getemailaddress", font=font_mono, fill="#62ffe3")
draw.text((764, 466), '{"agent_name":"my-agent"}', font=font_mono_small, fill="#d8f3ec")
draw.text((764, 497), '-> mailbox + api_key', font=font_mono_small, fill="#7affea")

# Envelope icon
icon_x, icon_y = 610, 210
draw.rounded_rectangle((icon_x, icon_y, icon_x + 82, icon_y + 58), radius=14, outline="#48e6d3", width=3)
draw.line((icon_x + 6, icon_y + 8, icon_x + 41, icon_y + 34), fill="#48e6d3", width=3)
draw.line((icon_x + 76, icon_y + 8, icon_x + 41, icon_y + 34), fill="#48e6d3", width=3)

# Footer
draw.text((62, 592), "agentsmail.org", font=font_mono_small, fill="#5ed8cd")
draw.text((660, 592), "free  |  encrypted  |  agent-native", font=font_mono_small, fill="#6ba8a7")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT, format="PNG", optimize=True)
print(f"saved {OUT}")
