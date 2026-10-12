import urllib.request
import urllib.parse
import json
import csv
import io
import os

tabs = [
    {"name": "Sheets", "slug": "overview", "title": "ภาพรวมและสารบัญชีต"},
    {"name": "FDM 3D Printer", "slug": "fdm-printers", "title": "เครื่องพิมพ์ FDM 3D Printer"},
    {"name": "FDM Tool Changer", "slug": "fdm-tool-changer", "title": "เครื่องพิมพ์ FDM Tool Changer"},
    {"name": "FDM DIY", "slug": "fdm-diy", "title": "เครื่องพิมพ์ FDM DIY & Kits"},
    {"name": "Boards", "slug": "boards", "title": "เมนบอร์ดควบคุม (Controller Boards)"},
    {"name": "StepDriver", "slug": "step-driver", "title": "ไดรเวอร์มอเตอร์ (Stepper Drivers)"},
    {"name": "StepperMotor", "slug": "stepper-motor", "title": "สเต็ปเปอร์มอเตอร์ (Stepper Motors)"},
    {"name": "MMS", "slug": "mms", "title": "ระบบมัลติคัลเลอร์ (Multi-Material System)"},
    {"name": "Filament Dryer", "slug": "filament-dryer", "title": "กล่องอบเส้นพลาสติก (Filament Dryers)"},
    {"name": "Filament Material", "slug": "filament-material", "title": "ยี่ห้อและรุ่นเส้น Filament"},
    {"name": "Filament Properties", "slug": "filament-properties", "title": "คุณสมบัติเชิงกลและความร้อนของเส้น Filament"},
    {"name": "Resin 3D Printer", "slug": "resin-printers", "title": "เครื่องพิมพ์ Resin 3D Printer"},
    {"name": "Powder 3D Printer", "slug": "powder-printers", "title": "เครื่องพิมพ์ Powder 3D Printer (SLS)"},
    {"name": "Resin Material", "slug": "resin-material", "title": "วัสดุเรซิน (Resin Materials)"},
    {"name": "Useful Link", "slug": "useful-links", "title": "ลิงก์และแหล่งข้อมูลที่เป็นประโยชน์"},
    {"name": "Contact", "slug": "contact", "title": "ข้อมูลติดต่อผู้จัดทำ"}
]

os.makedirs("c:/Users/panyo/Documents/antigravity/clever-hubble/data", exist_ok=True)
base_url = "https://docs.google.com/spreadsheets/d/1bEBUpAaxm3Cxigb7G_JMSFGm43-6OwxU-FXXBbUp2Mg/gviz/tq?tqx=out:csv&headers=1&sheet="

summary = []

for item in tabs:
    t_name = item["name"]
    slug = item["slug"]
    url = base_url + urllib.parse.quote(t_name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            raw_csv = resp.read().decode('utf-8')
        
        with open(f"c:/Users/panyo/Documents/antigravity/clever-hubble/data/{slug}.csv", "w", encoding="utf-8") as f:
            f.write(raw_csv)
        
        reader = list(csv.reader(io.StringIO(raw_csv)))
        if reader:
            headers = [h.strip() for h in reader[0]]
            while headers and not headers[-1]:
                headers.pop()
            
            rows = []
            for r in reader[1:]:
                if any(cell.strip() for cell in r):
                    row_dict = {}
                    for i, h in enumerate(headers):
                        val = r[i].strip() if i < len(r) else ""
                        row_dict[h if h else f"col_{i}"] = val
                    rows.append(row_dict)
            
            data_obj = {
                "name": t_name,
                "slug": slug,
                "title": item["title"],
                "headers": headers,
                "total_rows": len(rows),
                "data": rows
            }
            
            with open(f"c:/Users/panyo/Documents/antigravity/clever-hubble/data/{slug}.json", "w", encoding="utf-8") as f:
                json.dump(data_obj, f, ensure_ascii=False, indent=2)
            
            summary.append({
                "name": t_name,
                "slug": slug,
                "title": item["title"],
                "headers": headers,
                "count": len(rows)
            })
            print(f"Downloaded {t_name:<20} -> {slug}.json ({len(rows)} rows, headers: {headers[:3]})")
    except Exception as e:
        print(f"Failed {t_name}: {e}")

with open("c:/Users/panyo/Documents/antigravity/clever-hubble/data/manifest.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
