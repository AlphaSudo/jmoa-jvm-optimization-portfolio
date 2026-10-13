"""Render current publication scope as SVG; stable legacy filename for callers.

Uses only the Python standard library. Run from any directory. Figures describe
different services and qualification states, not a version-to-version speedup.
"""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parents[1]

def main():
    stable = json.loads((ROOT / "EVIDENCE/v2.1/petclinic-direct-ram-win.json").read_text())
    patient = json.loads((ROOT / "EVIDENCE/v2.15/patient-scoped-ram-benchmark.json").read_text())
    assert stable["claimable"] and stable["packagingInclusive"]
    assert not patient["performanceBoundsQualified"] and not patient["fullProductAcceptance"]
    assert not patient["originalNull"]["memoryPassed"]
    rows = [
        ("Stable 2.1 / PetClinic", "Java 17 / no CDS", "R41F fat JAR versus B0 exploded Boot",
         f"{-stable['processPssKiB']['median']/1024:.2f} MiB lower process PSS",
         "Accepted packaging-inclusive result; frozen cost gates passed"),
        ("Provisional 2.15 / Patient", "Java 26 / Leyden", "Separate frozen application/cache identities",
         f"{patient['medianSavingMiB']:.2f} MiB lower median stopped PSS",
         "Original calibration failed; approved exception; costs unqualified or failed")
    ]
    elements = []
    for index, row in enumerate(rows):
        y = 110 + index * 190
        elements.append(f'<rect x="30" y="{y}" width="1140" height="170" rx="8" fill="#f1f5f9"/>')
        for line_index, text in enumerate(row):
            size = 24 if line_index == 0 else 18
            elements.append(f'<text x="55" y="{y+32+line_index*28}" font-size="{size}">{escape(text)}</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="590" viewBox="0 0 1200 590" role="img" aria-labelledby="title desc">
<title id="title">JMOA current publication scopes</title>
<desc id="desc">Stable PetClinic and provisional Patient are different service/runtime studies. Patient calibration and performance limitations remain.</desc>
<rect width="1200" height="590" fill="white"/>
<g font-family="Arial, sans-serif" fill="#172033">
<text x="30" y="48" font-size="28">Runtime policy and qualification belong with the RAM number</text>
<text x="30" y="82" font-size="18">Different services and protocols; no version-to-version effect is inferred.</text>
{''.join(elements)}
<text x="30" y="530" font-size="18">Patient: conditional lower bound {patient['lowerSavingBoundMiB']:.2f} MiB; warmth and production/binary parity unqualified.</text>
<text x="30" y="560" font-size="18">2.15 adds evidence only. Stable Maven binaries remain 2.1.0.</text>
</g></svg>"""
    output = ROOT / "ASSETS/diagrams/runtime-modes.svg"
    output.write_text(svg + "\n", encoding="utf-8")
    print("Rendered current runtime publication scopes.")

if __name__ == "__main__":
    main()
