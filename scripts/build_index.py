import json
import os

ROOT_DIR = "c:/Users/panyo/Documents/antigravity/clever-hubble"
DATA_DIR = os.path.join(ROOT_DIR, "data")

def load_json(slug):
    with open(os.path.join(DATA_DIR, f"{slug}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

manifest = load_json("manifest")
fdm_data = load_json("fdm-printers")["data"]
filament_props = load_json("filament-properties")["data"]
resin_printers = load_json("resin-printers")["data"]
boards_data = load_json("boards")["data"]

# Build compact global search index across all 16 tabs
search_index = []
tab_configs = [
    {"slug": "overview", "name": "Sheets Overview", "title": "ภาพรวมและสารบัญชีต", "cat": "ทั่วไป", "icon": "file-text", "desc": "สารบัญ คำอธิบายแต่ละชีต และอัตราแลกเปลี่ยนอ้างอิง"},
    {"slug": "fdm-printers", "name": "FDM 3D Printer", "title": "เครื่องพิมพ์ FDM 3D Printer", "cat": "เครื่องพิมพ์", "icon": "box", "desc": "สเปกเครื่องพิมพ์ระบบเส้นพลาสติก 216 รุ่น ขนาด ความเร็ว อุณหภูมิ และราคา"},
    {"slug": "fdm-tool-changer", "name": "FDM Tool Changer", "title": "เครื่องพิมพ์ FDM Tool Changer", "cat": "เครื่องพิมพ์", "icon": "layers", "desc": "เครื่องพิมพ์สลับหัวฉีดอัตโนมัติ (Prusa XL, Jubilee, E3D ToolChanger ฯลฯ)"},
    {"slug": "fdm-diy", "name": "FDM DIY & Kits", "title": "เครื่องพิมพ์ FDM DIY & Open-Source", "cat": "เครื่องพิมพ์", "icon": "wrench", "desc": "โปรเจกต์เครื่องพิมพ์ประกอบเอง Voron, RatRig, HevORT, Rook, Ender NG"},
    {"slug": "resin-printers", "name": "Resin 3D Printer", "title": "เครื่องพิมพ์เรซิน (SLA/MSLA/DLP)", "cat": "เครื่องพิมพ์", "icon": "droplet", "desc": "เปรียบเทียบเครื่องพิมพ์เรซิน 125 รุ่น ความละเอียดจอ 4K-16K และ XY Resolution"},
    {"slug": "powder-printers", "name": "Powder 3D Printer", "title": "เครื่องพิมพ์ระบบผง (SLS/SLM)", "cat": "เครื่องพิมพ์", "icon": "sparkles", "desc": "เครื่องพิมพ์เลเซอร์หลอมผงพลาสติกและโลหะระดับโปรและอุตสาหกรรม"},
    {"slug": "filament-material", "name": "Filament Material", "title": "ยี่ห้อและรุ่นเส้น Filament", "cat": "วัสดุ", "icon": "disc", "desc": "รายการเส้นพลาสติกกว่า 430 รุ่นจากทุกแบรนด์ พร้อมอุณหภูมิและราคาต่อกิโลกรัม"},
    {"slug": "filament-properties", "name": "Filament Properties", "title": "คุณสมบัติทางวิศวกรรมของเส้นพลาสติก", "cat": "วัสดุ", "icon": "activity", "desc": "ตารางเปรียบเทียบค่า Tg, Melting Temp, HDT, Tensile Strength ของวัสดุ 61 ชนิด"},
    {"slug": "resin-material", "name": "Resin Material", "title": "ฐานข้อมูลน้ำยาเรซิน (Resin Catalog)", "cat": "วัสดุ", "icon": "flask-conical", "desc": "คลังข้อมูลเรซินกว่า 1,020 รายการ ครบทุกแบรนด์ สี สเปก และราคา"},
    {"slug": "boards", "name": "Boards", "title": "เมนบอร์ดควบคุม (Controller Boards)", "cat": "ฮาร์ดแวร์", "icon": "cpu", "desc": "เปรียบเทียบเมนบอร์ด BTT, MKS, Duet3D, Fly ชิป CPU, ไดรเวอร์ และ CAN Bus"},
    {"slug": "step-driver", "name": "StepDriver", "title": "ไดรเวอร์มอเตอร์ (Stepper Drivers)", "cat": "ฮาร์ดแวร์", "icon": "zap", "desc": "สเปกชิปขับมอเตอร์ TMC2209, TMC5160, TMC2240, A4988 กระแสไฟและโหมดการทำงาน"},
    {"slug": "stepper-motor", "name": "StepperMotor", "title": "สเต็ปเปอร์มอเตอร์ (Stepper Motors)", "cat": "ฮาร์ดแวร์", "icon": "compass", "desc": "ข้อมูลมอเตอร์ LDO, Moons, StepperOnline ขนาด NEMA แรงบิด และกระแสไฟ"},
    {"slug": "mms", "name": "MMS", "title": "ระบบพิมพ์หลากสี (Multi-Material System)", "cat": "อุปกรณ์เสริม", "icon": "palette", "desc": "ระบบสลับเส้นพลาสติกหลากสี Bambu AMS, ERCF, Palette, Creality CFS, ACE Pro"},
    {"slug": "filament-dryer", "name": "Filament Dryer", "title": "กล่องอบเส้นพลาสติก (Filament Dryers)", "cat": "อุปกรณ์เสริม", "icon": "sun", "desc": "ตู้อบไล่ความชื้นเส้นพลาสติก ความจุม้วน อุณหภูมิสูงสุด และกำลังไฟ"},
    {"slug": "useful-links", "name": "Useful Link", "title": "รวมลิงก์และเครื่องมือที่มีประโยชน์", "cat": "อื่น ๆ", "icon": "link", "desc": "แหล่งรวมโปรแกรม Slicer, คู่มือปรับจูน Calibration, ชุมชน และเว็บโหลดโมเดล"},
    {"slug": "contact", "name": "Contact", "title": "ติดต่อผู้จัดทำและส่งข้อมูลเพิ่ม", "cat": "อื่น ๆ", "icon": "mail", "desc": "ช่องทางติดต่อผู้จัดทำ 3D Printer Thailand Master List และ GitHub"}
]

# Populate row counts and sample headers into tab_configs
manifest_map = {m["slug"]: m for m in manifest}
for tc in tab_configs:
    m = manifest_map.get(tc["slug"], {})
    tc["count"] = m.get("count", 1 if tc["slug"] == "contact" else 0)
    tc["headers"] = m.get("headers", [])[:5]

    # Add items to global search index (up to 1500 concise items)
    if tc["slug"] not in ("overview", "contact"):
        rows = load_json(tc["slug"]).get("data", [])
        headers = m.get("headers", [])
        k1 = headers[0] if len(headers) > 0 else ""
        k2 = headers[1] if len(headers) > 1 else ""
        k3 = headers[2] if len(headers) > 2 else ""
        price_col = next((h for h in headers if "price" in h.lower() or "thb" in h.lower()), "")
        for r in rows:
            title_str = f"{r.get(k1, '')} {r.get(k2, '')}".strip()
            sub_str = str(r.get(k3, "")).strip()
            price_str = str(r.get(price_col, "")).strip() if price_col else ""
            if title_str:
                search_index.append({
                    "t": title_str,
                    "s": sub_str,
                    "p": price_str,
                    "cat": tc["title"],
                    "slug": tc["slug"]
                })

index_html = f"""<!DOCTYPE html>
<html lang="th" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3D Printing Knowledge Wiki | คลังข้อมูลและระบบเปรียบเทียบสเปก 3D Printer ประเทศไทย</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Inter', 'Noto Sans Thai', sans-serif;
      background-color: #070b14;
      color: #e2e8f0;
    }}
    .glass-card {{
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(51, 65, 85, 0.6);
    }}
    .hero-glow {{
      background: radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.18), rgba(99, 102, 241, 0.08) 45%, transparent 75%);
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scrollbar::-webkit-scrollbar-track {{
      background: #0f172a;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 3px;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-cyan-500/30 selection:text-cyan-200">
  <div id="header-mount"></div>

  <!-- Hero Section -->
  <section class="relative hero-glow border-b border-slate-800/80 pt-10 pb-14 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center max-w-3xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold mb-5">
          <span>✨ 3D Printer Thailand Master List</span>
          <span class="text-slate-600">•</span>
          <span>16 หมวดหมู่ครบวงจร</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight">
          คลังความรู้และฐานข้อมูลสเปก <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-indigo-400">3D Printing</span>
        </h1>
        <p class="text-slate-400 text-sm sm:text-base mt-4 leading-relaxed">
          ค้นหา กรองข้อมูล และเปรียบเทียบสเปกเครื่องพิมพ์ 3 มิติ (FDM, Resin, SLS), คุณสมบัติเส้นพลาสติก, น้ำยาเรซิน, เมนบอร์ด และฮาร์ดแวร์กว่า <span class="text-white font-semibold">2,150+ รายการ</span> ในที่เดียว
        </p>

        <!-- Global Search Bar -->
        <div class="mt-8 relative max-w-2xl mx-auto text-left">
          <div class="relative flex items-center">
            <i data-lucide="search" class="w-5 h-5 text-cyan-400 absolute left-4 pointer-events-none"></i>
            <input id="global-search-input" type="text" placeholder="ค้นหาข้ามทุกหมวดหมู่ เช่น Bambu Lab, Voron 2.4, PLA, PETG, TMC2209, Elegoo..."
              class="w-full pl-12 pr-28 py-4 bg-slate-900/95 border-2 border-slate-700/80 focus:border-cyan-400 rounded-2xl text-sm sm:text-base text-white placeholder-slate-500 shadow-2xl shadow-cyan-950/30 focus:outline-none transition">
            <div class="absolute right-3 flex items-center gap-1.5">
              <button id="clear-global-search" class="hidden p-1.5 text-slate-400 hover:text-white rounded-lg">
                <i data-lucide="x" class="w-4 h-4"></i>
              </button>
              <a href="#compare-section" class="px-3 py-1.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs transition flex items-center gap-1">
                <i data-lucide="git-compare" class="w-3.5 h-3.5"></i> เปรียบเทียบ
              </a>
            </div>
          </div>

          <!-- Global Search Results Dropdown -->
          <div id="global-search-results" class="hidden absolute left-0 right-0 mt-2 bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl overflow-hidden z-50 max-h-96 overflow-y-auto custom-scrollbar">
          </div>
        </div>

        <!-- Quick Jump Pills -->
        <div class="flex flex-wrap items-center justify-center gap-2 mt-4 text-xs text-slate-400">
          <span>คำค้นยอดฮิต:</span>
          <button onclick="triggerQuickSearch('Bambu')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">Bambu Lab</button>
          <button onclick="triggerQuickSearch('Creality')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">Creality</button>
          <button onclick="triggerQuickSearch('Voron')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">Voron</button>
          <button onclick="triggerQuickSearch('PEEK')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">PEEK</button>
          <button onclick="triggerQuickSearch('TMC2209')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">TMC2209</button>
          <button onclick="triggerQuickSearch('Siraya')" class="px-2.5 py-1 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition">Siraya Tech</button>
        </div>
      </div>

      <!-- Summary Stat Banner -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-10 max-w-5xl mx-auto">
        <div class="glass-card rounded-2xl p-4 flex items-center gap-3.5">
          <div class="w-11 h-11 rounded-xl bg-cyan-500/15 border border-cyan-500/30 flex items-center justify-center text-cyan-400 flex-shrink-0">
            <i data-lucide="layers" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="text-xl sm:text-2xl font-extrabold text-white">16 หมวดหมู่</div>
            <div class="text-xs text-slate-400">ครบทุก Tab จากชีตต้นฉบับ</div>
          </div>
        </div>
        <div class="glass-card rounded-2xl p-4 flex items-center gap-3.5">
          <div class="w-11 h-11 rounded-xl bg-indigo-500/15 border border-indigo-500/30 flex items-center justify-center text-indigo-400 flex-shrink-0">
            <i data-lucide="box" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="text-xl sm:text-2xl font-extrabold text-white">435+ รุ่น</div>
            <div class="text-xs text-slate-400">เครื่องพิมพ์ FDM, Resin & SLS</div>
          </div>
        </div>
        <div class="glass-card rounded-2xl p-4 flex items-center gap-3.5">
          <div class="w-11 h-11 rounded-xl bg-rose-500/15 border border-rose-500/30 flex items-center justify-center text-rose-400 flex-shrink-0">
            <i data-lucide="disc" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="text-xl sm:text-2xl font-extrabold text-white">1,510+ รายการ</div>
            <div class="text-xs text-slate-400">เส้นพลาสติก, เรซิน & คุณสมบัติ</div>
          </div>
        </div>
        <div class="glass-card rounded-2xl p-4 flex items-center gap-3.5">
          <div class="w-11 h-11 rounded-xl bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center text-emerald-400 flex-shrink-0">
            <i data-lucide="cpu" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="text-xl sm:text-2xl font-extrabold text-white">175+ ชิ้นส่วน</div>
            <div class="text-xs text-slate-400">บอร์ด, ไดรเวอร์, มอเตอร์ & MMS</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16">
    
    <!-- Section 1: Table of Contents (16 Tabs Directory with Category Filter) -->
    <section id="directory-section">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-6">
        <div>
          <span class="text-xs font-semibold uppercase tracking-wider text-cyan-400">Table of Contents</span>
          <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">สารบัญข้อมูลทั้งหมด (16 Tabs)</h2>
          <p class="text-slate-400 text-sm mt-1">เลือกหมวดหมู่ที่ต้องการสำรวจข้อมูลตารางแบบละเอียด</p>
        </div>

        <!-- Category Filter Pills -->
        <div id="cat-pills" class="flex flex-wrap gap-2">
          <button data-cat="all" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">ทั้งหมด (16)</button>
          <button data-cat="เครื่องพิมพ์" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">เครื่องพิมพ์ (5)</button>
          <button data-cat="วัสดุ" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">วัสดุการพิมพ์ (3)</button>
          <button data-cat="ฮาร์ดแวร์" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">ฮาร์ดแวร์ (3)</button>
          <button data-cat="อุปกรณ์เสริม" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">อุปกรณ์เสริม (2)</button>
          <button data-cat="อื่น ๆ" class="cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition">ทั่วไป & ลิงก์ (3)</button>
        </div>
      </div>

      <!-- 16 Cards Grid -->
      <div id="tabs-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      </div>
    </section>

    <!-- Section 2: Interactive Spec Comparison Engine -->
    <section id="compare-section" class="scroll-mt-20">
      <div class="glass-card rounded-3xl p-6 sm:p-8 border border-cyan-500/25 shadow-2xl">
        <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-6 border-b border-slate-800">
          <div>
            <div class="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider text-cyan-400">
              <i data-lucide="git-compare" class="w-4 h-4"></i> Interactive Comparison Tool
            </div>
            <h2 class="text-2xl sm:text-3xl font-bold text-white mt-1">ระบบเปรียบเทียบสเปกแบบ Side-by-Side</h2>
            <p class="text-slate-400 text-sm mt-1">เลือกรุ่นเครื่องพิมพ์ วัสดุ หรือเมนบอร์ดสูงสุด 3 รายการเพื่อเปรียบเทียบข้อมูลทางเทคนิคเคียงข้างกัน</p>
          </div>

          <!-- Comparison Mode Tabs -->
          <div class="flex flex-wrap gap-2 bg-slate-950/90 p-1.5 rounded-2xl border border-slate-800">
            <button onclick="switchCompareMode('fdm')" id="cmp-tab-fdm" class="cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition flex items-center gap-1.5">
              <i data-lucide="box" class="w-3.5 h-3.5"></i> FDM Printers (216)
            </button>
            <button onclick="switchCompareMode('filament')" id="cmp-tab-filament" class="cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition flex items-center gap-1.5">
              <i data-lucide="activity" class="w-3.5 h-3.5"></i> Filament Properties (61)
            </button>
            <button onclick="switchCompareMode('resin')" id="cmp-tab-resin" class="cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition flex items-center gap-1.5">
              <i data-lucide="droplet" class="w-3.5 h-3.5"></i> Resin Printers (125)
            </button>
            <button onclick="switchCompareMode('boards')" id="cmp-tab-boards" class="cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition flex items-center gap-1.5">
              <i data-lucide="cpu" class="w-3.5 h-3.5"></i> Boards (48)
            </button>
          </div>
        </div>

        <!-- Filter & Selectors Row -->
        <div class="mt-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4">
              <label class="block text-xs font-semibold text-cyan-400 uppercase tracking-wider mb-2">รายการเปรียบเทียบที่ 1</label>
              <select id="cmp-select-0" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"></select>
            </div>
            <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4">
              <label class="block text-xs font-semibold text-indigo-400 uppercase tracking-wider mb-2">รายการเปรียบเทียบที่ 2</label>
              <select id="cmp-select-1" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"></select>
            </div>
            <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4">
              <label class="block text-xs font-semibold text-emerald-400 uppercase tracking-wider mb-2">รายการเปรียบเทียบที่ 3</label>
              <select id="cmp-select-2" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2.5 text-sm text-white focus:outline-none focus:border-cyan-500"></select>
            </div>
          </div>

          <!-- Comparison Table Output -->
          <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-950/60">
            <table class="w-full text-left border-collapse text-sm">
              <thead>
                <tr id="cmp-head" class="bg-slate-900 border-b border-slate-800"></tr>
              </thead>
              <tbody id="cmp-body" class="divide-y divide-slate-800/70"></tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

  </main>

  <div id="footer-mount"></div>

  <!-- Embedded Datasets -->
  <script id="tabs-config-data" type="application/json">{json.dumps(tab_configs, ensure_ascii=False)}</script>
  <script id="search-index-data" type="application/json">{json.dumps(search_index, ensure_ascii=False)}</script>
  <script id="cmp-fdm-data" type="application/json">{json.dumps(fdm_data, ensure_ascii=False)}</script>
  <script id="cmp-filament-data" type="application/json">{json.dumps(filament_props, ensure_ascii=False)}</script>
  <script id="cmp-resin-data" type="application/json">{json.dumps(resin_printers, ensure_ascii=False)}</script>
  <script id="cmp-boards-data" type="application/json">{json.dumps(boards_data, ensure_ascii=False)}</script>

  <script src="./assets/common.js"></script>
  <script>
    renderWikiHeader('', true);

    const TABS_CONFIG = JSON.parse(document.getElementById('tabs-config-data').textContent);
    const SEARCH_INDEX = JSON.parse(document.getElementById('search-index-data').textContent);
    const CMP_DATA = {{
      fdm: {{
        items: JSON.parse(document.getElementById('cmp-fdm-data').textContent),
        labelFn: r => `${{r['Seller'] || ''}} - ${{r['Printer'] || ''}}`,
        fields: [
          'Seller', 'Printer', 'Motion Type', 'Build Length (mm)', 'Build Width (mm)',
          'Build Height (mm)', 'Volume (L)', 'Speed (mm/s)', 'Accelation (mm/s^2)',
          'HotEnd Max Temp (°C)', 'Heatbed Max Temp (°C)', 'Extruder',
          'Support MultiMaterial System', 'Enclosed', 'Heated Chember', 'EST Price (THB)', 'Release Year'
        ],
        defaults: [0, 15, 42]
      }},
      filament: {{
        items: JSON.parse(document.getElementById('cmp-filament-data').textContent),
        labelFn: r => `${{r['Material'] || ''}} (${{r['Name'] || ''}})`,
        fields: [
          'Material', 'Name', 'Glass Transition Temp (°C)', 'Melting Temp (°C)',
          'Heat Deflection Temp (°C)', 'Tensile Strength (MPa)', 'Elongation at Break (%)',
          'Impact Strength (kJ/m²)', 'UV Resistance', 'Chemical Resistance',
          'Print Difficulty', 'Nozzle Temp (°C)', 'Bed Temp (°C)', 'Other Notes'
        ],
        defaults: [0, 27, 30]
      }},
      resin: {{
        items: JSON.parse(document.getElementById('cmp-resin-data').textContent),
        labelFn: r => `${{r['Seller'] || ''}} - ${{r['Printer'] || ''}}`,
        fields: [
          'Seller', 'Printer', 'Technology Type', 'Build Length (mm)', 'Build Width (mm)',
          'Build Height (mm)', 'Volume (L)', 'LCD Screen', 'LCD Resolution',
          'XY Resolution (µm)', 'Max Print Speed (mm/h)', 'Current Price (THB)', 'Release Date'
        ],
        defaults: [0, 5, 12]
      }},
      boards: {{
        items: JSON.parse(document.getElementById('cmp-boards-data').textContent),
        labelFn: r => `${{r['Brand'] || ''}} - ${{r['Name'] || ''}}`,
        fields: [
          'Brand', 'Name', 'Compatible Uses', 'CPU', 'StepperMotor Drivers',
          'Voltage', 'CAN Bus', 'Firmware', 'Wifi', 'USB', 'Estimated Price'
        ],
        defaults: [0, 2, 8]
      }}
    }};

    // 1. Render 16 Tabs Grid
    let selectedCat = 'all';
    function renderTabsGrid() {{
      const grid = document.getElementById('tabs-grid');
      const list = TABS_CONFIG.filter(t => {{
        if (selectedCat === 'all') return true;
        if (selectedCat === 'อื่น ๆ') return t.cat === 'อื่น ๆ' || t.cat === 'ทั่วไป';
        return t.cat === selectedCat;
      }});

      grid.innerHTML = list.map((t, i) => `
        <a href="./pages/${{t.slug}}.html" class="glass-card rounded-2xl p-5 hover:border-cyan-500/60 hover:-translate-y-1 transition-all duration-200 flex flex-col justify-between group">
          <div>
            <div class="flex items-center justify-between gap-2 mb-4">
              <div class="w-11 h-11 rounded-xl bg-slate-800/90 border border-slate-700 group-hover:border-cyan-500/40 group-hover:bg-cyan-500/15 flex items-center justify-center text-cyan-400 transition">
                <i data-lucide="${{t.icon}}" class="w-5 h-5"></i>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-slate-800 text-slate-300 border border-slate-700">${{t.cat}}</span>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">${{t.count.toLocaleString()}} รายการ</span>
              </div>
            </div>
            <div class="text-xs font-mono text-slate-400">${{t.name}}</div>
            <h3 class="text-base font-bold text-white group-hover:text-cyan-300 transition mt-0.5">${{t.title}}</h3>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed line-clamp-2">${{t.desc}}</p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-800/70 flex items-center justify-between text-xs">
            <span class="text-slate-500 truncate max-w-[170px]">${{(t.headers || []).slice(0, 3).join(' • ')}}</span>
            <span class="text-cyan-400 font-semibold flex items-center gap-1 group-hover:translate-x-0.5 transition">
              เปิดดู <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </span>
          </div>
        </a>
      `).join('');
      if (window.lucide) window.lucide.createIcons();
    }}

    document.querySelectorAll('.cat-pill').forEach(btn => {{
      btn.addEventListener('click', () => {{
        selectedCat = btn.getAttribute('data-cat');
        document.querySelectorAll('.cat-pill').forEach(b => {{
          const active = b.getAttribute('data-cat') === selectedCat;
          b.className = active
            ? 'cat-pill px-3.5 py-1.5 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition'
            : 'cat-pill px-3.5 py-1.5 rounded-xl text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition';
        }});
        renderTabsGrid();
      }});
    }});

    // 2. Global Search
    const searchInput = document.getElementById('global-search-input');
    const searchResults = document.getElementById('global-search-results');
    const clearBtn = document.getElementById('clear-global-search');

    function performGlobalSearch(q) {{
      const query = q.toLowerCase().trim();
      clearBtn.classList.toggle('hidden', !query);
      if (!query) {{
        searchResults.classList.add('hidden');
        return;
      }}

      const matches = SEARCH_INDEX.filter(item =>
        item.t.toLowerCase().includes(query) ||
        item.s.toLowerCase().includes(query) ||
        item.cat.toLowerCase().includes(query)
      ).slice(0, 25);

      if (matches.length === 0) {{
        searchResults.innerHTML = `<div class="p-6 text-center text-sm text-slate-400">ไม่พบผลลัพธ์สำหรับ "${{q}}"</div>`;
      }} else {{
        searchResults.innerHTML = `
          <div class="px-4 py-2 bg-slate-950 border-b border-slate-800 text-[11px] text-slate-400 flex justify-between">
            <span>ผลการค้นหาที่ตรงกัน (แสดงสูงสุด 25 รายการแรก)</span>
            <span>คลิกเพื่อเปิดดูในหมวดหมู่</span>
          </div>
          <div class="divide-y divide-slate-800/70">
            ${{matches.map(m => `
              <a href="./pages/${{m.slug}}.html" class="flex items-center justify-between px-4 py-3 hover:bg-slate-800/70 transition">
                <div>
                  <div class="text-sm font-semibold text-white">${{m.t}}</div>
                  <div class="text-xs text-slate-400">${{m.cat}} ${{m.s ? '• ' + m.s : ''}}</div>
                </div>
                <div class="flex items-center gap-2">
                  ${{m.p ? `<span class="text-xs font-semibold text-emerald-400">฿${{m.p}}</span>` : ''}}
                  <i data-lucide="chevron-right" class="w-4 h-4 text-slate-500"></i>
                </div>
              </a>
            `).join('')}}
          </div>
        `;
      }}
      searchResults.classList.remove('hidden');
      if (window.lucide) window.lucide.createIcons();
    }}

    window.triggerQuickSearch = function(term) {{
      searchInput.value = term;
      performGlobalSearch(term);
      searchInput.focus();
    }};

    searchInput.addEventListener('input', e => performGlobalSearch(e.target.value));
    clearBtn.addEventListener('click', () => {{
      searchInput.value = '';
      performGlobalSearch('');
    }});
    document.addEventListener('click', e => {{
      if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {{
        searchResults.classList.add('hidden');
      }}
    }});

    // 3. Comparison Engine
    let currentCmpMode = 'fdm';
    let selectedIndices = [0, 1, 2];

    window.switchCompareMode = function(mode) {{
      currentCmpMode = mode;
      ['fdm', 'filament', 'resin', 'boards'].forEach(m => {{
        const btn = document.getElementById('cmp-tab-' + m);
        btn.className = m === mode
          ? 'cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition flex items-center gap-1.5'
          : 'cmp-mode-btn px-3.5 py-2 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition flex items-center gap-1.5';
      }});

      const cfg = CMP_DATA[mode];
      selectedIndices = cfg.defaults.map(i => Math.min(i, cfg.items.length - 1));
      populateCompareSelects();
      renderCompareTable();
    }};

    function populateCompareSelects() {{
      const cfg = CMP_DATA[currentCmpMode];
      [0, 1, 2].forEach(slot => {{
        const sel = document.getElementById('cmp-select-' + slot);
        sel.innerHTML = cfg.items.map((item, idx) => `
          <option value="${{idx}}" ${{idx === selectedIndices[slot] ? 'selected' : ''}}>
            ${{cfg.labelFn(item)}}
          </option>
        `).join('');
        sel.onchange = (e) => {{
          selectedIndices[slot] = parseInt(e.target.value, 10);
          renderCompareTable();
        }};
      }});
    }}

    function renderCompareTable() {{
      const cfg = CMP_DATA[currentCmpMode];
      const chosen = selectedIndices.map(i => cfg.items[i] || {{}});
      
      const head = document.getElementById('cmp-head');
      head.innerHTML = `
        <th class="px-5 py-4 text-xs font-bold uppercase tracking-wider text-slate-400 w-1/4">คุณสมบัติ (Specification)</th>
        <th class="px-5 py-4 text-sm font-bold text-cyan-400 w-1/4">${{cfg.labelFn(chosen[0])}}</th>
        <th class="px-5 py-4 text-sm font-bold text-indigo-400 w-1/4">${{cfg.labelFn(chosen[1])}}</th>
        <th class="px-5 py-4 text-sm font-bold text-emerald-400 w-1/4">${{cfg.labelFn(chosen[2])}}</th>
      `;

      const body = document.getElementById('cmp-body');
      body.innerHTML = cfg.fields.map(field => {{
        const v0 = chosen[0][field] || '-';
        const v1 = chosen[1][field] || '-';
        const v2 = chosen[2][field] || '-';
        return `
          <tr class="hover:bg-slate-900/50 transition">
            <td class="px-5 py-3.5 font-medium text-slate-400 bg-slate-900/30">${{field}}</td>
            <td class="px-5 py-3.5 font-semibold text-white">${{v0}}</td>
            <td class="px-5 py-3.5 font-semibold text-white">${{v1}}</td>
            <td class="px-5 py-3.5 font-semibold text-white">${{v2}}</td>
          </tr>
        `;
      }}).join('');
    }}

    // Initialize
    renderTabsGrid();
    switchCompareMode('fdm');
  </script>
</body>
</html>
"""

with open(os.path.join(ROOT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Generated index.html successfully!")
