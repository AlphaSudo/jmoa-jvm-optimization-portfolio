from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "ASSETS"
FONT = Path("C:/Windows/Fonts/segoeui.ttf")
BOLD = Path("C:/Windows/Fonts/segoeuib.ttf")

BG = "#0b1118"
PANEL = "#111a24"
INK = "#f5f2ed"
MUTED = "#aab5c1"
RED = "#dc2f2f"
CYAN = "#19a7ce"
GREEN = "#69c13d"

SERVICES = [
    {
        "name": "PetClinic customers",
        "deployment": "Exploded Boot / JarLauncher",
        "policy": "NO_CDS_LOW_DIRTY",
        "pss_kb": 6012,
        "wins": "2/3",
        "color": CYAN,
    },
    {
        "name": "Doctor service",
        "deployment": "Corrected Spring Boot fat JAR",
        "policy": "APPLICATION_CDS",
        "pss_kb": 5156,
        "wins": "3/3",
        "color": GREEN,
    },
    {
        "name": "Patient service",
        "deployment": "Corrected Spring Boot fat JAR",
        "policy": "JDK_BASE_CDS_LOW_DIRTY",
        "pss_kb": 8279,
        "wins": "3/3",
        "color": RED,
    },
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(BOLD if bold else FONT), size)


def draw_hero() -> None:
    image = Image.new("RGB", (1600, 800), BG)
    draw = ImageDraw.Draw(image)
    draw.text((72, 72), "JMOA", fill=INK, font=font(92, True))
    draw.rounded_rectangle((307, 79, 382, 157), radius=7, fill=RED)
    draw.text((72, 182), "Evidence-driven JVM footprint optimization", fill=INK, font=font(38, True))
    draw.text((72, 240), "3 services  |  3 confirmed V1 to V2 wins  |  5-8 MiB median PSS reduction", fill=MUTED, font=font(23))

    card_y = 342
    card_w = 456
    for index, service in enumerate(SERVICES):
        x = 72 + index * 500
        draw.rounded_rectangle((x, card_y, x + card_w, 650), radius=8, fill=PANEL, outline="#344251", width=2)
        draw.rectangle((x + 28, card_y + 30, x + 112, card_y + 36), fill=service["color"])
        draw.text((x + 28, card_y + 62), service["name"], fill=INK, font=font(28, True))
        draw.text((x + 28, card_y + 112), service["deployment"], fill=MUTED, font=font(18))
        draw.text((x + 28, card_y + 148), service["policy"], fill=service["color"], font=font(17, True))
        mib = service["pss_kb"] / 1024
        draw.text((x + 28, card_y + 202), f"-{service['pss_kb']:,} KB", fill=INK, font=font(40, True))
        draw.text((x + 28, card_y + 254), f"median PSS  |  {mib:.1f} MiB  |  {service['wins']} wins", fill=MUTED, font=font(17))

    draw.text((72, 713), "6/6 valid runs per service  |  zero workload errors  |  V2-C confirmed  |  V2-D attribution", fill=INK, font=font(21, True))
    image.save(ASSETS / "jmoa-portfolio-hero.png", optimize=True)


def draw_chart() -> None:
    image = Image.new("RGB", (1400, 800), "#f5f7fa")
    draw = ImageDraw.Draw(image)
    navy = "#152033"
    draw.text((78, 55), "Final V2 Median PSS Reduction", fill=navy, font=font(48, True))
    draw.text((80, 118), "Accepted V1 artifact to final V2 artifact", fill="#4b5c70", font=font(23))
    left, top, right, bottom = 150, 200, 1290, 650
    for tick in range(0, 10, 2):
        y = bottom - (tick / 10) * (bottom - top)
        draw.line((left, y, right, y), fill="#d7dee7", width=2)
        draw.text((70, y - 13), f"{tick} MiB", fill="#60738a", font=font(18))
    slot = (right - left) / 3
    for index, service in enumerate(SERVICES):
        value = service["pss_kb"] / 1024
        x1 = left + index * slot + 88
        x2 = x1 + 200
        y1 = bottom - (value / 10) * (bottom - top)
        draw.rounded_rectangle((x1, y1, x2, bottom), radius=8, fill=service["color"])
        draw.text((x1 + 34, y1 - 52), f"{value:.1f} MiB", fill=navy, font=font(28, True))
        label = service["name"].replace(" customers", "")
        bbox = draw.textbbox((0, 0), label, font=font(23, True))
        draw.text(((x1 + x2 - (bbox[2] - bbox[0])) / 2, bottom + 24), label, fill=navy, font=font(23, True))
        policy = service["policy"]
        bbox = draw.textbbox((0, 0), policy, font=font(15))
        draw.text(((x1 + x2 - (bbox[2] - bbox[0])) / 2, bottom + 62), policy, fill="#60738a", font=font(15))
    image.save(ASSETS / "charts" / "median-pss-savings.png", optimize=True)


def write_runtime_svg() -> None:
    cards = []
    for index, service in enumerate(SERVICES):
        x = 70 + index * 510
        cards.append(
            f'''<g transform="translate({x},245)">
  <rect width="465" height="315" rx="8" fill="#111a24" stroke="#344251" stroke-width="2"/>
  <rect x="28" y="28" width="90" height="7" fill="{service['color']}"/>
  <text x="28" y="83" class="title">{service['name']}</text>
  <text x="28" y="126" class="body">{service['deployment']}</text>
  <text x="28" y="166" class="policy" fill="{service['color']}">{service['policy']}</text>
  <text x="28" y="230" class="result">-{service['pss_kb']:,} KB</text>
  <text x="28" y="270" class="body">median PSS | {service['wins']} paired wins</text>
</g>'''
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="720" viewBox="0 0 1600 720">
<rect width="1600" height="720" fill="#0b1118"/>
<style>
.heading {{ font: 700 48px 'Segoe UI', Arial, sans-serif; fill: #f5f2ed; }}
.sub {{ font: 22px 'Segoe UI', Arial, sans-serif; fill: #aab5c1; }}
.title {{ font: 700 28px 'Segoe UI', Arial, sans-serif; fill: #f5f2ed; }}
.body {{ font: 18px 'Segoe UI', Arial, sans-serif; fill: #aab5c1; }}
.policy {{ font: 700 17px 'Consolas', monospace; }}
.result {{ font: 700 40px 'Segoe UI', Arial, sans-serif; fill: #f5f2ed; }}
</style>
<text x="70" y="82" class="heading">Runtime policy is part of the deployment contract</text>
<text x="70" y="128" class="sub">The final V2 matrix uses one frozen, confirmed policy per service.</text>
<path d="M800 158 V210" stroke="#aab5c1" stroke-width="3"/>
<path d="M303 210 H1318" stroke="#aab5c1" stroke-width="3"/>
<path d="M303 210 V235 M810 210 V235 M1318 210 V235" stroke="#aab5c1" stroke-width="3"/>
{''.join(cards)}
<text x="70" y="652" class="sub">Patient no-CDS is independently confirmed; dynamic Patient application CDS remains blocked.</text>
<text x="70" y="687" class="sub">No policy result transfers automatically to another service, artifact, or launch mode.</text>
</svg>'''
    (ASSETS / "diagrams" / "runtime-modes.svg").write_text(svg, encoding="utf-8")


def draw_pdf() -> None:
    pdfmetrics.registerFont(TTFont("Segoe", str(FONT)))
    pdfmetrics.registerFont(TTFont("SegoeBold", str(BOLD)))
    output = ASSETS / "portfolio-summary.pdf"
    width, height = landscape(A4)
    c = canvas.Canvas(str(output), pagesize=(width, height))
    c.setFillColor(HexColor("#f5f7fa"))
    c.rect(0, 0, width, height, stroke=0, fill=1)
    c.setFillColor(HexColor("#152033"))
    c.setFont("SegoeBold", 27)
    c.drawString(42, height - 52, "JMOA V2 - Evidence-Driven JVM Footprint Optimization")
    c.setFont("Segoe", 10.5)
    c.setFillColor(HexColor("#4b5c70"))
    c.drawString(42, height - 75, "Build-time transformation, artifact proof, paired evidence validation, and memory attribution for Spring Boot.")

    y = height - 130
    card_width = 238
    for index, service in enumerate(SERVICES):
        x = 42 + index * 264
        c.setFillColor(HexColor("#ffffff"))
        c.roundRect(x, y - 125, card_width, 125, 6, stroke=0, fill=1)
        c.setStrokeColor(HexColor(service["color"]))
        c.setLineWidth(4)
        c.line(x + 15, y - 18, x + 78, y - 18)
        c.setFillColor(HexColor("#152033"))
        c.setFont("SegoeBold", 13)
        c.drawString(x + 15, y - 42, service["name"])
        c.setFont("Segoe", 8.5)
        c.setFillColor(HexColor("#4b5c70"))
        c.drawString(x + 15, y - 60, service["policy"])
        c.setFont("SegoeBold", 21)
        c.setFillColor(HexColor(service["color"]))
        c.drawString(x + 15, y - 90, f"-{service['pss_kb']:,} KB")
        c.setFont("Segoe", 8.5)
        c.setFillColor(HexColor("#4b5c70"))
        c.drawString(x + 15, y - 108, f"median PSS | {service['wins']} wins | 6/6 valid")

    section_y = y - 168
    c.setFillColor(HexColor("#152033"))
    c.setFont("SegoeBold", 14)
    c.drawString(42, section_y, "Why the result is credible")
    c.setFont("Segoe", 9.5)
    c.setFillColor(HexColor("#26364a"))
    bullets = [
        "Zero workload errors; V2-C CONFIRMED_WIN and V2-D attribution for every final row.",
        "PSS and Private_Dirty are primary; cgroup memory.current, NMT, smaps, heap, and histograms support attribution.",
        "Runtime artifact identity, materialization, class origins, and service-specific policy are part of the measured contract.",
        "Negative ASM, application-class, generated-family, and Patient AppCDS hypotheses remain rejected.",
    ]
    for index, item in enumerate(bullets):
        c.drawString(52, section_y - 21 - index * 18, f"- {item}")

    c.setFont("SegoeBold", 14)
    c.setFillColor(HexColor("#152033"))
    c.drawString(42, 98, "Claim boundary")
    c.setFont("Segoe", 9.5)
    c.setFillColor(HexColor("#26364a"))
    c.drawString(42, 79, "Results are service-, artifact-, launch-mode-, and runtime-policy-specific. No universal CDS, startup, or memory claim.")
    c.setFillColor(HexColor("#4b5c70"))
    c.drawString(42, 47, "Source: github.com/AlphaSudo/jmoa   |   Portfolio: github.com/AlphaSudo/jmoa-jvm-optimization-portfolio")
    c.save()


if __name__ == "__main__":
    draw_hero()
    draw_chart()
    write_runtime_svg()
    draw_pdf()
    print("Rendered V2 portfolio assets.")
