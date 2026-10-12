import json
import os
import html

ROOT_DIR = "c:/Users/panyo/Documents/antigravity/clever-hubble"
DATA_DIR = os.path.join(ROOT_DIR, "data")
PAGES_DIR = os.path.join(ROOT_DIR, "pages")

os.makedirs(PAGES_DIR, exist_ok=True)

TABS_META = [
    {
        "slug": "overview",
        "name": "Sheets",
        "title": "สารบัญและภาพรวมข้อมูล (Master List Overview)",
        "subtitle": "รายละเอียดโครงสร้างข้อมูลทั้งหมดใน 3D Printer Thailand Master List รวบรวมโดย Terasit J.",
        "icon": "file-text",
        "category": "ทั่วไป",
        "accent": "cyan",
        "filter_cols": [],
        "primary_cols": ["3D Printer Master List", "Compiled By Terasit J.", "Currency", "Value"]
    },
    {
        "slug": "fdm-printers",
        "name": "FDM 3D Printer",
        "title": "เครื่องพิมพ์ FDM 3D Printer",
        "subtitle": "ฐานข้อมูลสเปกเครื่องพิมพ์ 3 มิติระบบฉีดเส้นพลาสติก (FDM/FFF) กว่า 216 รุ่น เปรียบเทียบขนาด ความเร็ว และราคา",
        "icon": "box",
        "category": "เครื่องพิมพ์",
        "accent": "cyan",
        "filter_cols": ["Seller", "Motion Type", "Enclosed", "Support MultiMaterial System"],
        "primary_cols": ["Seller", "Printer", "Motion Type", "Build Length (mm)", "Build Width (mm)", "Build Height (mm)", "Volume (L)", "Speed (mm/s)", "HotEnd Max Temp (°C)", "Enclosed", "EST Price (THB)", "Release Year"]
    },
    {
        "slug": "fdm-tool-changer",
        "name": "FDM Tool Changer",
        "title": "เครื่องพิมพ์ FDM Tool Changer",
        "subtitle": "เครื่องพิมพ์ 3 มิติระบบสลับหัวพิมพ์ (Multiple Toolheads / IDEX / Toolchanger) สำหรับงานพิมพ์หลายวัสดุขั้นสูง",
        "icon": "layers",
        "category": "เครื่องพิมพ์",
        "accent": "indigo",
        "filter_cols": ["Seller", "Motion Type", "ToolsHead"],
        "primary_cols": ["Seller", "Printer", "Motion Type", "ToolsHead", "Build Length (mm)", "Build Width (mm)", "Build Height (mm)", "Speed (mm/s)", "HotEnd Max Temp (°C)", "EST Price (THB)", "Release Year"]
    },
    {
        "slug": "fdm-diy",
        "name": "FDM DIY",
        "title": "เครื่องพิมพ์ FDM DIY & Open-Source Kits",
        "subtitle": "รวบรวมโปรเจกต์เครื่องพิมพ์ 3D สายประกอบเอง (Voron, RatRig, HevORT, Rook, Prusa Bear ฯลฯ)",
        "icon": "wrench",
        "category": "เครื่องพิมพ์",
        "accent": "amber",
        "filter_cols": ["Seller", "Motion Type", "Enclosed"],
        "primary_cols": ["Seller", "Printer", "Motion Type", "Build Length (mm)", "Build Width (mm)", "Build Height (mm)", "Speed (mm/s)", "HotEnd Max Temp (C)", "Enclosed", "Current Price (THB)", "Links"]
    },
    {
        "slug": "boards",
        "name": "Boards",
        "title": "เมนบอร์ดควบคุม (Controller Boards)",
        "subtitle": "เปรียบเทียบสเปกบอร์ดควบคุมเครื่องพิมพ์ 3 มิติ ชิปประมวลผล CPU, จำนวนไดรเวอร์, CAN Bus และรองรับ Klipper/Marlin/RRF",
        "icon": "cpu",
        "category": "ฮาร์ดแวร์",
        "accent": "emerald",
        "filter_cols": ["Brand", "Firmware", "CAN Bus", "Wifi"],
        "primary_cols": ["Brand", "Name", "CPU", "StepperMotor Drivers", "Voltage", "CAN Bus", "Firmware", "Wifi", "Estimated Price"]
    },
    {
        "slug": "step-driver",
        "name": "StepDriver",
        "title": "ไดรเวอร์มอเตอร์ (Stepper Motor Drivers)",
        "subtitle": "ข้อมูลทางเทคนิคชิปและโมดูล Stepper Driver (TMC2209, TMC5160, TMC2240, A4988 ฯลฯ) กระแส แรงดัน และฟีเจอร์",
        "icon": "zap",
        "category": "ฮาร์ดแวร์",
        "accent": "yellow",
        "filter_cols": ["Interface", "stealthChop", "stallGuard"],
        "primary_cols": ["Stepper Motor Driver", "Interface", "Config", "Max Microstep", "Voltage (V)", "RMS Current (A)", "Peak Current (A)", "stealthChop", "stallGuard"]
    },
    {
        "slug": "stepper-motor",
        "name": "StepperMotor",
        "title": "สเต็ปเปอร์มอเตอร์ (Stepper Motors)",
        "subtitle": "สเปกมอเตอร์สำหรับเครื่องพิมพ์ 3 มิติ ขนาด NEMA 14/17/23, Step Angle 0.9°/1.8°, แรงบิด Holding Torque และกระแสไฟ",
        "icon": "compass",
        "category": "ฮาร์ดแวร์",
        "accent": "blue",
        "filter_cols": ["Manufacturer", "Size (NEMA)", "Step Angle (°)"],
        "primary_cols": ["Manufacturer", "Model / Name", "Size (NEMA)", "Length (mm)", "Step Angle (°)", "Holding Torque (N.cm)", "Rated Current (A/Phase)", "Weight (g)", "Approx. Price", "Link"]
    },
    {
        "slug": "mms",
        "name": "MMS",
        "title": "ระบบพิมพ์หลากสี (Multi-Material Systems - MMS)",
        "subtitle": "อุปกรณ์เสริมสำหรับโหลดและสลับเส้นพลาสติกอัตโนมัติ (Bambu AMS, ERCF, Mosaic Palette, CFS, ACE Pro ฯลฯ)",
        "icon": "palette",
        "category": "อุปกรณ์เสริม",
        "accent": "pink",
        "filter_cols": ["Seller", "Filament Cutting", "Open Source"],
        "primary_cols": ["Seller", "Name", "Max Filament/Unit", "Max Unit", "Filament Cutting", "Open Source", "Estimated Price (THB)"]
    },
    {
        "slug": "filament-dryer",
        "name": "Filament Dryer",
        "title": "กล่องและตู้อบเส้นพลาสติก (Filament Dryers)",
        "subtitle": "เปรียบเทียบกล่องอบไล่ความชื้นเส้น Filament ความจุม้วน 1KG-3KG อุณหภูมิสูงสุด กำลังไฟ และฟีเจอร์เสริม",
        "icon": "sun",
        "category": "อุปกรณ์เสริม",
        "accent": "orange",
        "filter_cols": ["Manufacturer", "1KG Spool Support", "2KG Spool Support", "Max Temp (°C)"],
        "primary_cols": ["Manufacturer", "Series", "1KG Spool Support", "2KG Spool Support", "Min Temp (°C)", "Max Temp (°C)", "Max Dryer Time (Hr)", "Rated Power (W)", "Features", "Estimated price (THB)"]
    },
    {
        "slug": "filament-material",
        "name": "Filament Material",
        "title": "ฐานข้อมูลเส้นพลาสติก (Filament Materials Catalog)",
        "subtitle": "รวบรวมเส้นพลาสติกกว่า 430 รายการจากหลากหลายแบรนด์ในตลาด ทั้งอุณหภูมิแนะนำ ความแข็งแรง และราคาต่อกิโลกรัม",
        "icon": "disc",
        "category": "วัสดุ",
        "accent": "violet",
        "filter_cols": ["Manufacturer", "Materials Type", "Spool Type"],
        "primary_cols": ["Manufacturer", "Series", "Materials Type", "Number of Color", "Recommand Nozzle Temp (°C)", "Recommand Bed Temp  (°C)", "Tensile Strength, Break (MPa)", "Heat Deflection Temp (°C)", "Estimated price (THB)", "Price per KG (THB)"]
    },
    {
        "slug": "filament-properties",
        "name": "Filament Properties",
        "title": "คุณสมบัติทางวิศวกรรมของเส้นพลาสติก (Filament Properties)",
        "subtitle": "ตารางเปรียบเทียบคุณสมบัติเชิงกลและอุณหภูมิของพลาสติก 61 ชนิด (Tg, Melting Temp, HDT, Tensile Strength, ความยากในการพิมพ์)",
        "icon": "activity",
        "category": "วัสดุ",
        "accent": "rose",
        "filter_cols": ["Print Difficulty", "UV Resistance", "Chemical Resistance"],
        "primary_cols": ["Material", "Name", "Glass Transition Temp (°C)", "Melting Temp (°C)", "Heat Deflection Temp (°C)", "Tensile Strength (MPa)", "Impact Strength (kJ/m²)", "UV Resistance", "Print Difficulty", "Nozzle Temp (°C)", "Bed Temp (°C)"]
    },
    {
        "slug": "resin-printers",
        "name": "Resin 3D Printer",
        "title": "เครื่องพิมพ์เรซิน (Resin 3D Printers - MSLA/SLA/DLP)",
        "subtitle": "เปรียบเทียบเครื่องพิมพ์เรซิน 125 รุ่น ความละเอียดหน้าจอ 4K-16K, ขนาดพิกเซล XY Resolution (µm) และพื้นที่การพิมพ์",
        "icon": "droplet",
        "category": "เครื่องพิมพ์",
        "accent": "purple",
        "filter_cols": ["Seller", "Technology Type", "LCD Resolution"],
        "primary_cols": ["Seller", "Printer", "Technology Type", "Build Length (mm)", "Build Width (mm)", "Build Height (mm)", "LCD Screen", "LCD Resolution", "XY Resolution (µm)", "Current Price (THB)", "Release Date"]
    },
    {
        "slug": "powder-printers",
        "name": "Powder 3D Printer",
        "title": "เครื่องพิมพ์ระบบผงเลเซอร์ (Powder 3D Printers - SLS/SLM)",
        "subtitle": "เครื่องพิมพ์อุตสาหกรรมและตั้งโต๊ะระบบหลอมผงด้วยเลเซอร์ (SLS / Direct Metal Laser Sintering)",
        "icon": "sparkles",
        "category": "เครื่องพิมพ์",
        "accent": "sky",
        "filter_cols": ["Seller", "Technology Type", "Laser Type"],
        "primary_cols": ["Seller", "Printer", "Technology Type", "Build Length (mm)", "Build Width (mm)", "Build Height (mm)", "Laser Type", "Laser Power (W)", "Supported Materials", "EST Price (THB)", "Release Year"]
    },
    {
        "slug": "resin-material",
        "name": "Resin Material",
        "title": "ฐานข้อมูลน้ำยาเรซิน (Resin Materials - 1,020 รายการ)",
        "subtitle": "คลังข้อมูลน้ำยาเรซินสำหรับเครื่องพิมพ์ SLA/MSLA/DLP ครอบคลุมทุกแบรนด์ สี สเปกทางเทคนิค และราคาเปรียบเทียบ",
        "icon": "flask-conical",
        "category": "วัสดุ",
        "accent": "fuchsia",
        "filter_cols": ["Manufacturer", "weight (g)", "is verified"],
        "primary_cols": ["Manufacturer", "Series", "Number of Color", "Color", "Technical Spec", "weight (g)", "Estimated price (THB)", "Price per KG (THB)"]
    },
    {
        "slug": "useful-links",
        "name": "Useful Link",
        "title": "รวมลิงก์และเครื่องมือที่มีประโยชน์ (Useful Links & Resources)",
        "subtitle": "แหล่งรวมเว็บไซต์ โปรแกรม Slicer, คู่มือตั้งค่า Calibration, ชุมชน 3D Printing และแหล่งดาวน์โหลดโมเดล 3 มิติ",
        "icon": "link",
        "category": "อื่น ๆ",
        "accent": "teal",
        "filter_cols": ["Category"],
        "primary_cols": ["Category", "Source Name", "Description", "URL"]
    },
    {
        "slug": "contact",
        "name": "Contact",
        "title": "ติดต่อผู้จัดทำและชุมชน (Contact & Community)",
        "subtitle": "ช่องทางติดต่อผู้รวบรวมข้อมูล 3D Printer Thailand Master List และการมีส่วนร่วมอัปเดตข้อมูล",
        "icon": "mail",
        "category": "อื่น ๆ",
        "accent": "cyan",
        "filter_cols": [],
        "primary_cols": ["Email", "blazelabshop@gmail.com"]
    }
]

def load_tab_json(slug):
    path = os.path.join(DATA_DIR, f"{slug}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_tab_page(meta):
    slug = meta["slug"]
    tab_data = load_tab_json(slug)
    
    # For contact page, build a specialized rich contact & community page
    if slug == "contact":
        return generate_contact_page(meta, tab_data)
    if slug == "overview":
        return generate_overview_page(meta, tab_data)

    json_payload = json.dumps(tab_data, ensure_ascii=False)
    meta_payload = json.dumps(meta, ensure_ascii=False)
    tabs_list_payload = json.dumps(TABS_META, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="th" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(meta['title'])} | 3D Printing Knowledge Wiki</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Inter', 'Noto Sans Thai', sans-serif;
      background-color: #0b0f19;
      color: #e2e8f0;
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
    .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
      background: #475569;
    }}
    .glass-card {{
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(51, 65, 85, 0.6);
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-cyan-500/30 selection:text-cyan-200">
  <div id="header-mount"></div>

  <!-- Main Content -->
  <main class="flex-grow max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Breadcrumb & Quick Tab Switcher -->
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
      <nav class="flex items-center space-x-2 text-xs sm:text-sm text-slate-400">
        <a href="../index.html" class="hover:text-cyan-400 flex items-center gap-1 transition">
          <i data-lucide="home" class="w-3.5 h-3.5"></i> หน้าแรก
        </a>
        <span>/</span>
        <span class="text-slate-500">{html.escape(meta['category'])}</span>
        <span>/</span>
        <span class="text-cyan-400 font-medium">{html.escape(meta['name'])}</span>
      </nav>

      <div class="flex items-center gap-2">
        <a href="../index.html#compare-section" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 text-xs font-medium transition">
          <i data-lucide="git-compare" class="w-3.5 h-3.5"></i> เปรียบเทียบสเปก
        </a>
        <a href="../data/{slug}.csv" download="{slug}.csv" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-medium transition">
          <i data-lucide="download" class="w-3.5 h-3.5 text-cyan-400"></i> ดาวน์โหลด CSV
        </a>
      </div>
    </div>

    <!-- Hero Header -->
    <div class="glass-card rounded-2xl p-6 sm:p-8 mb-8 relative overflow-hidden">
      <div class="absolute -top-24 -right-24 w-72 h-72 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div class="flex items-start gap-4">
          <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-cyan-500/20 to-indigo-500/20 border border-cyan-500/30 flex items-center justify-center flex-shrink-0 text-cyan-400 shadow-lg shadow-cyan-950/50">
            <i data-lucide="{meta['icon']}" class="w-7 h-7"></i>
          </div>
          <div>
            <div class="flex items-center gap-2.5 flex-wrap">
              <span class="px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 uppercase tracking-wider">
                {html.escape(meta['category'])}
              </span>
              <span class="text-xs text-slate-400 font-mono">Tab: {html.escape(meta['name'])}</span>
            </div>
            <h1 class="text-2xl sm:text-3xl font-bold text-white mt-1.5">{html.escape(meta['title'])}</h1>
            <p class="text-slate-400 text-sm sm:text-base mt-1 max-w-3xl">{html.escape(meta['subtitle'])}</p>
          </div>
        </div>
      </div>

      <!-- Dynamic Stat Cards -->
      <div id="stats-container" class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6 pt-6 border-t border-slate-800/80">
      </div>
    </div>

    <!-- Filter & Search Controls -->
    <div class="glass-card rounded-2xl p-4 sm:p-5 mb-6">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-3 items-center">
        <!-- Search Input -->
        <div class="md:col-span-4 lg:col-span-5 relative">
          <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none"></i>
          <input id="search-input" type="text" placeholder="ค้นหาในหมวดนี้ (ชื่อรุ่น, ยี่ห้อ, สเปก...)" 
            class="w-full pl-10 pr-9 py-2.5 bg-slate-900/90 border border-slate-700/80 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition">
          <button id="clear-search" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>

        <!-- Dynamic Filter Selectors -->
        <div id="dynamic-filters" class="md:col-span-5 lg:col-span-5 grid grid-cols-1 sm:grid-cols-3 gap-2.5">
        </div>

        <!-- View Mode & Reset -->
        <div class="md:col-span-3 lg:col-span-2 flex items-center justify-end gap-2">
          <div class="inline-flex bg-slate-900 p-1 rounded-xl border border-slate-800">
            <button id="btn-view-table" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-cyan-500/20 text-cyan-300 flex items-center gap-1 transition" title="มุมมองตาราง">
              <i data-lucide="table" class="w-3.5 h-3.5"></i> ตาราง
            </button>
            <button id="btn-view-cards" class="px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white flex items-center gap-1 transition" title="มุมมองการ์ด">
              <i data-lucide="layout-grid" class="w-3.5 h-3.5"></i> การ์ด
            </button>
          </div>
          <button id="btn-reset" class="p-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700/80 transition" title="ล้างตัวกรองทั้งหมด">
            <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

      <!-- Active Status & Page Size -->
      <div class="flex flex-wrap items-center justify-between gap-2 mt-3 pt-3 border-t border-slate-800/60 text-xs text-slate-400">
        <div>
          แสดงผล <span id="showing-count" class="text-cyan-400 font-semibold">0</span> จากทั้งหมด <span id="total-count" class="text-white font-semibold">0</span> รายการ
          <span id="active-filter-badge" class="hidden ml-2 px-2 py-0.5 rounded bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">กำลังใช้ตัวกรอง</span>
        </div>
        <div class="flex items-center gap-2">
          <span>แสดงหน้าละ:</span>
          <select id="page-size" class="bg-slate-900 border border-slate-700 rounded-lg px-2 py-1 text-slate-200 focus:outline-none focus:border-cyan-500">
            <option value="25">25 รายการ</option>
            <option value="50">50 รายการ</option>
            <option value="100">100 รายการ</option>
            <option value="9999">ทั้งหมด</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Table View Container -->
    <div id="table-view-container" class="glass-card rounded-2xl overflow-hidden shadow-2xl">
      <div class="overflow-x-auto custom-scrollbar">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr id="table-head-row" class="bg-slate-900/95 border-b border-slate-800 text-[11px] font-semibold text-slate-400 uppercase tracking-wider select-none">
            </tr>
          </thead>
          <tbody id="table-body" class="divide-y divide-slate-800/60 text-xs sm:text-sm">
          </tbody>
        </table>
      </div>
    </div>

    <!-- Card Grid View Container -->
    <div id="cards-view-container" class="hidden grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    </div>

    <!-- Empty State -->
    <div id="empty-state" class="hidden glass-card rounded-2xl p-12 text-center my-6">
      <div class="w-16 h-16 rounded-full bg-slate-800/80 flex items-center justify-center mx-auto mb-4 text-slate-500">
        <i data-lucide="search-x" class="w-8 h-8"></i>
      </div>
      <h3 class="text-lg font-semibold text-white">ไม่พบข้อมูลที่ตรงกับเงื่อนไข</h3>
      <p class="text-slate-400 text-sm mt-1">ลองเปลี่ยนคำค้นหา หรือกดปุ่มรีเซ็ตตัวกรองเพื่อดูข้อมูลทั้งหมด</p>
      <button onclick="resetAllFilters()" class="mt-4 px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold text-xs transition">
        ล้างตัวกรองทั้งหมด
      </button>
    </div>

    <!-- Pagination -->
    <div id="pagination-bar" class="flex flex-wrap items-center justify-between gap-4 mt-6 px-2">
      <div id="page-info" class="text-xs text-slate-400"></div>
      <div id="page-buttons" class="flex items-center gap-1.5"></div>
    </div>

  </main>

  <!-- Detail Modal -->
  <div id="detail-modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm">
    <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-2xl w-full max-h-[88vh] flex flex-col shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-150">
      <div class="flex items-center justify-between px-6 py-4 bg-slate-800/70 border-b border-slate-700">
        <div>
          <span class="text-[11px] uppercase tracking-wider text-cyan-400 font-semibold">{html.escape(meta['name'])} Specification</span>
          <h3 id="modal-title" class="text-lg font-bold text-white mt-0.5">รายละเอียดข้อมูล</h3>
        </div>
        <button onclick="closeModal()" class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-700 transition">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      <div id="modal-body" class="p-6 overflow-y-auto custom-scrollbar space-y-3 text-sm">
      </div>
      <div class="px-6 py-3.5 bg-slate-950/70 border-t border-slate-800 flex justify-end gap-2">
        <button onclick="closeModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium transition">
          ปิดหน้าต่าง
        </button>
      </div>
    </div>
  </div>

  <div id="footer-mount"></div>

  <!-- Embedded Data -->
  <script id="tab-data" type="application/json">{json_payload}</script>
  <script id="meta-data" type="application/json">{meta_payload}</script>
  <script src="../assets/common.js"></script>
  <script>
    const TAB_DATA = JSON.parse(document.getElementById('tab-data').textContent);
    const META = JSON.parse(document.getElementById('meta-data').textContent);

    renderWikiHeader(META.slug, false);

    const allRows = TAB_DATA.data || [];
    const allHeaders = TAB_DATA.headers || [];
    const displayCols = (META.primary_cols && META.primary_cols.length > 0)
      ? META.primary_cols.filter(c => allHeaders.includes(c))
      : allHeaders.slice(0, 10);

    // State
    let searchQuery = '';
    let activeFilters = {{}};
    let sortCol = null;
    let sortAsc = true;
    let currentPage = 1;
    let pageSize = 25;
    let viewMode = 'table'; // 'table' | 'cards'
    let filteredRows = [...allRows];

    // Helper: parse number from string
    function parseNum(val) {{
      if (val === null || val === undefined) return NaN;
      const s = String(val).replace(/,/g, '').trim();
      const m = s.match(/-?\\d+(\\.\\d+)?/);
      return m ? parseFloat(m[0]) : NaN;
    }}

    // Build Stat Cards
    function buildStats() {{
      const container = document.getElementById('stats-container');
      const total = allRows.length;
      
      // Find first brand/seller/manufacturer column
      const brandCol = ['Seller', 'Brand', 'Manufacturer', 'Material', 'Category', 'Stepper Motor Driver'].find(c => allHeaders.includes(c)) || allHeaders[0];
      const uniqueBrands = new Set(allRows.map(r => (r[brandCol] || '').trim()).filter(Boolean)).size;

      // Find price or numeric column
      const priceCol = allHeaders.find(h => /price|thb/i.test(h));
      let thirdStatLabel = 'คอลัมน์ข้อมูล (Specs)';
      let thirdStatVal = allHeaders.length + ' รายการ';
      if (priceCol) {{
        const prices = allRows.map(r => parseNum(r[priceCol])).filter(n => !isNaN(n) && n > 0);
        if (prices.length > 0) {{
          const minP = Math.min(...prices).toLocaleString();
          const maxP = Math.max(...prices).toLocaleString();
          thirdStatLabel = 'ช่วงราคาโดยประมาณ (THB)';
          thirdStatVal = `฿${{minP}} - ฿${{maxP}}`;
        }}
      }}

      const typeCol = ['Motion Type', 'Technology Type', 'Materials Type', 'Interface', 'Size (NEMA)', 'Print Difficulty', 'Firmware'].find(c => allHeaders.includes(c));
      let fourthLabel = 'สถานะฐานข้อมูล';
      let fourthVal = 'อัปเดตล่าสุด 2026';
      if (typeCol) {{
        const uniqueTypes = new Set(allRows.map(r => (r[typeCol] || '').trim()).filter(Boolean)).size;
        fourthLabel = `ประเภท (${{typeCol}})`;
        fourthVal = `${{uniqueTypes}} รูปแบบ`;
      }}

      const stats = [
        {{ label: 'จำนวนรายการทั้งหมด', val: total.toLocaleString() + ' รายการ', icon: 'database', color: 'text-cyan-400' }},
        {{ label: `จำนวน ${{brandCol || 'กลุ่ม'}}`, val: uniqueBrands.toLocaleString() + ' แบรนด์/ชนิด', icon: 'tag', color: 'text-indigo-400' }},
        {{ label: thirdStatLabel, val: thirdStatVal, icon: 'bar-chart-3', color: 'text-emerald-400' }},
        {{ label: fourthLabel, val: fourthVal, icon: 'sparkles', color: 'text-amber-400' }}
      ];

      container.innerHTML = stats.map(s => `
        <div class="bg-slate-900/70 border border-slate-800/90 rounded-xl p-3.5 flex items-center gap-3">
          <div class="w-10 h-10 rounded-lg bg-slate-800 flex items-center justify-center ${{s.color}} flex-shrink-0">
            <i data-lucide="${{s.icon}}" class="w-5 h-5"></i>
          </div>
          <div class="min-w-0">
            <p class="text-[11px] text-slate-400 truncate">${{s.label}}</p>
            <p class="text-sm sm:text-base font-bold text-white truncate">${{s.val}}</p>
          </div>
        </div>
      `).join('');
    }}

    // Build Filter Dropdowns
    function buildFilters() {{
      const filterContainer = document.getElementById('dynamic-filters');
      const cols = (META.filter_cols || []).filter(c => allHeaders.includes(c)).slice(0, 3);
      
      filterContainer.innerHTML = cols.map((col, idx) => {{
        const vals = Array.from(new Set(allRows.map(r => (r[col] || '').trim()).filter(Boolean))).sort();
        return `
          <select data-filter-col="${{col.replace(/"/g, '&quot;')}}" class="filter-select w-full bg-slate-900/90 border border-slate-700/80 rounded-xl px-3 py-2.5 text-xs text-slate-200 focus:outline-none focus:border-cyan-500 transition truncate">
            <option value="">ทั้งหมด: ${{col}}</option>
            ${{vals.map(v => `<option value="${{v.replace(/"/g, '&quot;')}}">${{v}}</option>`).join('')}}
          </select>
        `;
      }}).join('');

      document.querySelectorAll('.filter-select').forEach(sel => {{
        sel.addEventListener('change', (e) => {{
          const col = e.target.getAttribute('data-filter-col');
          activeFilters[col] = e.target.value;
          currentPage = 1;
          applyFiltersAndRender();
        }});
      }});
    }}

    // Format cell value with smart badges
    function formatCell(col, val) {{
      if (val === undefined || val === null || String(val).trim() === '' || val === '-') {{
        return '<span class="text-slate-600">-</span>';
      }}
      const str = String(val).trim();

      // URLs
      if (/^https?:\\/\\//i.test(str)) {{
        return `<a href="${{str}}" target="_blank" rel="noopener" onclick="event.stopPropagation()" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-cyan-500/15 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/30 text-xs font-medium transition">
          <span>เปิดลิงก์</span> <i data-lucide="external-link" class="w-3 h-3"></i>
        </a>`;
      }}

      // Boolean / Yes-No
      if (/^(yes|true|✔|✓|1)$/i.test(str) && /enclosed|touch|verified|cut|open|support|wifi|usb|sd|can|stealth|spread|cool|stall|1kg|2kg|3kg/i.test(col)) {{
        return '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-medium bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">✔ รองรับ</span>';
      }}
      if (/^(no|false|✘|✗|0)$/i.test(str) && /enclosed|touch|verified|cut|open|support|wifi|usb|sd|can|stealth|spread|cool|stall|1kg|2kg|3kg/i.test(col)) {{
        return '<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-medium bg-slate-800 text-slate-400">ไม่รองรับ</span>';
      }}

      // Difficulty / Resistance badges
      if (/^(easy|low)$/i.test(str)) {{
        return `<span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">${{str}}</span>`;
      }}
      if (/^(medium)$/i.test(str)) {{
        return `<span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-amber-500/15 text-amber-300 border border-amber-500/30">${{str}}</span>`;
      }}
      if (/^(hard|high)$/i.test(str)) {{
        return `<span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-rose-500/15 text-rose-300 border border-rose-500/30">${{str}}</span>`;
      }}

      // Motion Type / Tech Type pill
      if (/motion type|technology type|materials type|interface/i.test(col)) {{
        return `<span class="px-2.5 py-0.5 rounded-lg text-xs font-medium bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 whitespace-nowrap">${{str}}</span>`;
      }}

      // Price formatting
      if (/price|thb/i.test(col)) {{
        const n = parseFloat(str.replace(/,/g, ''));
        if (!isNaN(n) && /^\\d+(\\.\\d+)?$/.test(str.replace(/,/g, ''))) {{
          return `<span class="font-semibold text-emerald-400 whitespace-nowrap">฿${{n.toLocaleString()}}</span>`;
        }}
        return `<span class="font-medium text-emerald-400">${{str}}</span>`;
      }}

      // Visual bar for Filament Properties temperatures & tensile strength
      if (META.slug === 'filament-properties' && /temp|strength/i.test(col)) {{
        const n = parseNum(str);
        const maxVal = /strength/i.test(col) ? 130 : 360;
        if (!isNaN(n) && n > 0) {{
          const pct = Math.min(100, Math.max(8, Math.round((n / maxVal) * 100)));
          const barColor = /strength/i.test(col) ? 'bg-rose-500' : 'bg-cyan-500';
          return `
            <div class="min-w-[90px]">
              <div class="flex justify-between text-xs mb-1"><span class="font-semibold text-white">${{str}}</span></div>
              <div class="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="${{barColor}} h-full rounded-full" style="width:${{pct}}%"></div>
              </div>
            </div>
          `;
        }}
      }}

      if (str.length > 65) {{
        return `<span title="${{str.replace(/"/g, '&quot;')}}" class="line-clamp-2 max-w-xs">${{str}}</span>`;
      }}
      return str;
    }}

    // Render Table Header
    function renderTableHeader() {{
      const tr = document.getElementById('table-head-row');
      tr.innerHTML = displayCols.map(col => {{
        const isSorted = sortCol === col;
        const icon = isSorted ? (sortAsc ? 'arrow-up' : 'arrow-down') : 'arrow-up-down';
        const activeClass = isSorted ? 'text-cyan-400 bg-slate-800/60' : 'hover:text-slate-200 hover:bg-slate-800/40';
        return `
          <th onclick="handleSort('${{col.replace(/'/g, "\\\\'")}}')" class="px-4 py-3.5 cursor-pointer transition whitespace-nowrap ${{activeClass}}">
            <div class="flex items-center gap-1.5">
              <span>${{col}}</span>
              <i data-lucide="${{icon}}" class="w-3.5 h-3.5 ${{isSorted ? 'text-cyan-400' : 'text-slate-600'}}"></i>
            </div>
          </th>
        `;
      }}).join('') + `<th class="px-4 py-3.5 text-right whitespace-nowrap">รายละเอียด</th>`;
    }}

    window.handleSort = function(col) {{
      if (sortCol === col) {{
        sortAsc = !sortAsc;
      }} else {{
        sortCol = col;
        sortAsc = true;
      }}
      applyFiltersAndRender();
    }};

    function applyFiltersAndRender() {{
      const q = searchQuery.toLowerCase().trim();
      filteredRows = allRows.filter(row => {{
        // Check dropdown filters
        for (const [col, val] of Object.entries(activeFilters)) {{
          if (val && String(row[col] || '').trim() !== val) return false;
        }}
        // Check search query
        if (!q) return true;
        return Object.values(row).some(v => String(v || '').toLowerCase().includes(q));
      }});

      // Check active filter badge
      const hasFilter = q !== '' || Object.values(activeFilters).some(Boolean);
      document.getElementById('active-filter-badge').classList.toggle('hidden', !hasFilter);

      // Sort
      if (sortCol) {{
        filteredRows.sort((a, b) => {{
          const va = a[sortCol] ?? '';
          const vb = b[sortCol] ?? '';
          const na = parseNum(va);
          const nb = parseNum(vb);
          if (!isNaN(na) && !isNaN(nb)) {{
            return sortAsc ? na - nb : nb - na;
          }}
          return sortAsc
            ? String(va).localeCompare(String(vb), 'th')
            : String(vb).localeCompare(String(va), 'th');
        }});
      }}

      // Counts
      document.getElementById('total-count').textContent = allRows.length.toLocaleString();
      document.getElementById('showing-count').textContent = filteredRows.length.toLocaleString();

      // Empty state
      const isEmpty = filteredRows.length === 0;
      document.getElementById('empty-state').classList.toggle('hidden', !isEmpty);
      document.getElementById('table-view-container').classList.toggle('hidden', isEmpty || viewMode !== 'table');
      document.getElementById('cards-view-container').classList.toggle('hidden', isEmpty || viewMode !== 'cards');

      // Slice page
      const totalPages = Math.max(1, Math.ceil(filteredRows.length / pageSize));
      if (currentPage > totalPages) currentPage = totalPages;
      const startIdx = (currentPage - 1) * pageSize;
      const pageItems = filteredRows.slice(startIdx, startIdx + pageSize);

      renderTableHeader();

      if (viewMode === 'table') {{
        const tbody = document.getElementById('table-body');
        tbody.innerHTML = pageItems.map((row, idx) => {{
          const globalIdx = allRows.indexOf(row);
          return `
            <tr onclick="openModal(${{globalIdx}})" class="hover:bg-slate-800/50 transition cursor-pointer group">
              ${{displayCols.map((col, cIdx) => `
                <td class="px-4 py-3 ${{cIdx <= 1 ? 'font-medium text-white' : 'text-slate-300'}}">
                  ${{formatCell(col, row[col])}}
                </td>
              `).join('')}}
              <td class="px-4 py-3 text-right whitespace-nowrap">
                <button onclick="event.stopPropagation(); openModal(${{globalIdx}})" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-slate-800 group-hover:bg-cyan-500/20 text-slate-300 group-hover:text-cyan-300 border border-slate-700 group-hover:border-cyan-500/40 text-xs transition">
                  <i data-lucide="maximize-2" class="w-3 h-3"></i> ดูสเปก
                </button>
              </td>
            </tr>
          `;
        }}).join('');
      }} else {{
        const grid = document.getElementById('cards-view-container');
        grid.innerHTML = pageItems.map(row => {{
          const globalIdx = allRows.indexOf(row);
          const titleCol = displayCols[1] || displayCols[0];
          const subCol = displayCols[0];
          const restCols = displayCols.slice(2, 8);
          return `
            <div onclick="openModal(${{globalIdx}})" class="glass-card rounded-2xl p-5 hover:border-cyan-500/50 transition cursor-pointer flex flex-col justify-between group">
              <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                  <span class="text-xs font-semibold text-cyan-400 uppercase tracking-wider">${{row[subCol] || '-'}}</span>
                  <span class="text-[11px] text-slate-500">#${{globalIdx + 1}}</span>
                </div>
                <h3 class="text-base font-bold text-white group-hover:text-cyan-300 transition mb-4">${{row[titleCol] || '-'}}</h3>
                <div class="space-y-2 border-t border-slate-800/80 pt-3 text-xs">
                  ${{restCols.map(c => `
                    <div class="flex items-center justify-between gap-2">
                      <span class="text-slate-400 truncate">${{c}}:</span>
                      <span class="text-slate-200 font-medium text-right">${{formatCell(c, row[c])}}</span>
                    </div>
                  `).join('')}}
                </div>
              </div>
              <div class="mt-4 pt-3 border-t border-slate-800/60 flex justify-end">
                <span class="text-xs text-cyan-400 group-hover:underline flex items-center gap-1">
                  ดูสเปกทั้งหมด (${{allHeaders.length}} รายการ) <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                </span>
              </div>
            </div>
          `;
        }}).join('');
      }}

      renderPagination(filteredRows.length, totalPages);
      if (window.lucide) window.lucide.createIcons();
    }}

    function renderPagination(totalItems, totalPages) {{
      const info = document.getElementById('page-info');
      const btns = document.getElementById('page-buttons');
      if (totalItems === 0) {{
        info.textContent = '';
        btns.innerHTML = '';
        return;
      }}
      const start = (currentPage - 1) * pageSize + 1;
      const end = Math.min(totalItems, currentPage * pageSize);
      info.textContent = `หน้า ${{currentPage}} จาก ${{totalPages}} (รายการที่ ${{start}} - ${{end}})`;

      if (totalPages <= 1) {{
        btns.innerHTML = '';
        return;
      }}

      let htmlBtns = '';
      htmlBtns += `<button onclick="goToPage(${{currentPage - 1}})" ${{currentPage === 1 ? 'disabled' : ''}} class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:pointer-events-none text-xs text-slate-200 border border-slate-700 transition">ก่อนหน้า</button>`;

      const maxButtons = 5;
      let startP = Math.max(1, currentPage - 2);
      let endP = Math.min(totalPages, startP + maxButtons - 1);
      if (endP - startP < maxButtons - 1) startP = Math.max(1, endP - maxButtons + 1);

      for (let p = startP; p <= endP; p++) {{
        const active = p === currentPage;
        htmlBtns += `<button onclick="goToPage(${{p}})" class="w-8 h-8 rounded-lg text-xs font-semibold transition ${{active ? 'bg-cyan-500 text-slate-950' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}}">${{p}}</button>`;
      }}

      htmlBtns += `<button onclick="goToPage(${{currentPage + 1}})" ${{currentPage === totalPages ? 'disabled' : ''}} class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:pointer-events-none text-xs text-slate-200 border border-slate-700 transition">ถัดไป</button>`;
      btns.innerHTML = htmlBtns;
    }}

    window.goToPage = function(p) {{
      currentPage = p;
      applyFiltersAndRender();
      window.scrollTo({{ top: 260, behavior: 'smooth' }});
    }};

    window.openModal = function(idx) {{
      const row = allRows[idx];
      if (!row) return;
      const title = (row[displayCols[0]] ? row[displayCols[0]] + ' — ' : '') + (row[displayCols[1]] || '');
      document.getElementById('modal-title').textContent = title || 'รายละเอียดสเปก';
      
      const body = document.getElementById('modal-body');
      body.innerHTML = `
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          ${{allHeaders.map(h => `
            <div class="bg-slate-950/60 border border-slate-800/80 rounded-xl p-3">
              <div class="text-[11px] text-slate-400 mb-1">${{h}}</div>
              <div class="text-sm font-medium text-white break-words">${{formatCell(h, row[h])}}</div>
            </div>
          `).join('')}}
        </div>
      `;
      const modal = document.getElementById('detail-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      if (window.lucide) window.lucide.createIcons();
    }};

    window.closeModal = function() {{
      const modal = document.getElementById('detail-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }};

    window.resetAllFilters = function() {{
      searchQuery = '';
      activeFilters = {{}};
      sortCol = null;
      currentPage = 1;
      document.getElementById('search-input').value = '';
      document.getElementById('clear-search').classList.add('hidden');
      document.querySelectorAll('.filter-select').forEach(s => s.value = '');
      applyFiltersAndRender();
    }};

    // Event Listeners
    document.getElementById('search-input').addEventListener('input', (e) => {{
      searchQuery = e.target.value;
      document.getElementById('clear-search').classList.toggle('hidden', !searchQuery);
      currentPage = 1;
      applyFiltersAndRender();
    }});

    document.getElementById('clear-search').addEventListener('click', () => {{
      searchQuery = '';
      document.getElementById('search-input').value = '';
      document.getElementById('clear-search').classList.add('hidden');
      currentPage = 1;
      applyFiltersAndRender();
    }});

    document.getElementById('page-size').addEventListener('change', (e) => {{
      pageSize = parseInt(e.target.value, 10) || 25;
      currentPage = 1;
      applyFiltersAndRender();
    }});

    document.getElementById('btn-view-table').addEventListener('click', () => {{
      viewMode = 'table';
      document.getElementById('btn-view-table').className = 'px-2.5 py-1.5 rounded-lg text-xs font-medium bg-cyan-500/20 text-cyan-300 flex items-center gap-1 transition';
      document.getElementById('btn-view-cards').className = 'px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white flex items-center gap-1 transition';
      applyFiltersAndRender();
    }});

    document.getElementById('btn-view-cards').addEventListener('click', () => {{
      viewMode = 'cards';
      document.getElementById('btn-view-cards').className = 'px-2.5 py-1.5 rounded-lg text-xs font-medium bg-cyan-500/20 text-cyan-300 flex items-center gap-1 transition';
      document.getElementById('btn-view-table').className = 'px-2.5 py-1.5 rounded-lg text-xs font-medium text-slate-400 hover:text-white flex items-center gap-1 transition';
      applyFiltersAndRender();
    }});

    document.getElementById('btn-reset').addEventListener('click', resetAllFilters);

    document.getElementById('detail-modal').addEventListener('click', (e) => {{
      if (e.target.id === 'detail-modal') closeModal();
    }});

    // Init
    buildStats();
    buildFilters();
    applyFiltersAndRender();
  </script>
</body>
</html>"""
    return html_content

def generate_overview_page(meta, tab_data):
    tabs_json = json.dumps(TABS_META, ensure_ascii=False)
    data_json = json.dumps(tab_data, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="th" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>สารบัญและภาพรวมข้อมูล (Master List Overview) | 3D Printing Wiki</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', 'Noto Sans Thai', sans-serif; background-color: #0b0f19; color: #e2e8f0; }}
    .glass-card {{ background: rgba(15, 23, 42, 0.78); backdrop-filter: blur(12px); border: 1px solid rgba(51, 65, 85, 0.6); }}
  </style>
</head>
<body class="min-h-screen flex flex-col">
  <div id="header-mount"></div>
  <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div class="glass-card rounded-2xl p-6 sm:p-8 mb-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">Tab 1: Sheets Overview</span>
          <h1 class="text-2xl sm:text-3xl font-bold text-white mt-2">สารบัญและรายละเอียดชีตทั้งหมด (Master List Sheets)</h1>
          <p class="text-slate-400 text-sm mt-1">รวบรวมและจัดทำข้อมูลต้นฉบับโดย <span class="text-cyan-300 font-semibold">Terasit J.</span> สำหรับชุมชน 3D Printer ประเทศไทย</p>
        </div>
        <a href="../data/overview.csv" download="overview.csv" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-medium transition self-start">
          <i data-lucide="download" class="w-4 h-4 text-cyan-400"></i> ดาวน์โหลด CSV
        </a>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
      <div class="lg:col-span-2 glass-card rounded-2xl overflow-hidden">
        <div class="px-6 py-4 bg-slate-900/90 border-b border-slate-800 flex items-center justify-between">
          <h2 class="font-bold text-white flex items-center gap-2"><i data-lucide="list" class="w-4 h-4 text-cyan-400"></i> ตารางสารบัญจาก Google Sheet ต้นฉบับ</h2>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-sm">
            <thead>
              <tr class="bg-slate-900/60 border-b border-slate-800 text-xs text-slate-400 uppercase">
                <th class="px-4 py-3">ชื่อชีต (Sheet Name)</th>
                <th class="px-4 py-3">คำอธิบาย (Description)</th>
                <th class="px-4 py-3 text-right">ลิงก์ไปยังหน้าเว็บ</th>
              </tr>
            </thead>
            <tbody id="overview-tbody" class="divide-y divide-slate-800/60"></tbody>
          </table>
        </div>
      </div>

      <div class="space-y-6">
        <div class="glass-card rounded-2xl p-6">
          <h3 class="font-bold text-white flex items-center gap-2 mb-4">
            <i data-lucide="coins" class="w-4 h-4 text-amber-400"></i> อัตราแลกเปลี่ยนอ้างอิงในชีต
          </h3>
          <p class="text-xs text-slate-400 mb-4">ใช้สำหรับคำนวณราคาประเมิน (EST Price THB) ในตารางเครื่องพิมพ์และอุปกรณ์</p>
          <div id="currency-list" class="space-y-2.5 text-sm"></div>
        </div>

        <div class="glass-card rounded-2xl p-6">
          <h3 class="font-bold text-white flex items-center gap-2 mb-3">
            <i data-lucide="info" class="w-4 h-4 text-cyan-400"></i> เกี่ยวกับโปรเจกต์นี้
          </h3>
          <p class="text-xs text-slate-400 leading-relaxed">
            เว็บไซต์นี้แปลงข้อมูลจาก 3D Printer Thailand Master List ทั้ง 16 แท็บให้อยู่ในรูปแบบ Interactive Wiki ที่ค้นหา กรอง และเปรียบเทียบสเปกได้ทันทีผ่านเบราว์เซอร์
          </p>
        </div>
      </div>
    </div>
  </main>
  <div id="footer-mount"></div>
  <script id="tab-data" type="application/json">{data_json}</script>
  <script id="tabs-meta" type="application/json">{tabs_json}</script>
  <script src="../assets/common.js"></script>
  <script>
    renderWikiHeader('overview', false);
    const data = JSON.parse(document.getElementById('tab-data').textContent).data || [];
    const tabsMeta = JSON.parse(document.getElementById('tabs-meta').textContent);
    const tbody = document.getElementById('overview-tbody');
    const currList = document.getElementById('currency-list');

    const sheetRows = [];
    const currencies = [];

    data.forEach(r => {{
      const sName = r['3D Printer Master List'] || '';
      const desc = r['Compiled By Terasit J.'] || '';
      const curr = r['Currency'] || '';
      const val = r['Value'] || '';
      if (curr && val && curr !== 'Currency') currencies.push({{ curr, val }});
      if (sName && sName !== 'Sheets') sheetRows.push({{ sName, desc }});
    }});

    tbody.innerHTML = tabsMeta.filter(t => t.slug !== 'overview').map(t => {{
      const found = sheetRows.find(s => s.sName.toLowerCase() === t.name.toLowerCase());
      const desc = found ? found.desc : t.subtitle;
      return `
        <tr class="hover:bg-slate-800/40 transition">
          <td class="px-4 py-3.5 font-semibold text-white whitespace-nowrap">${{t.name}}</td>
          <td class="px-4 py-3.5 text-slate-300 text-xs sm:text-sm">${{desc}}</td>
          <td class="px-4 py-3.5 text-right whitespace-nowrap">
            <a href="./${{t.slug}}.html" class="inline-flex items-center gap-1 px-3 py-1 rounded-lg bg-cyan-500/15 hover:bg-cyan-500/25 text-cyan-300 border border-cyan-500/30 text-xs font-medium transition">
              เปิดดู <i data-lucide="arrow-right" class="w-3 h-3"></i>
            </a>
          </td>
        </tr>
      `;
    }}).join('');

    currList.innerHTML = currencies.map(c => `
      <div class="flex items-center justify-between p-3 rounded-xl bg-slate-900/80 border border-slate-800">
        <span class="font-mono font-semibold text-amber-300">1 ${{c.curr}}</span>
        <span class="font-bold text-white">${{c.val}} THB</span>
      </div>
    `).join('');

    if (window.lucide) window.lucide.createIcons();
  </script>
</body>
</html>"""

def generate_contact_page(meta, tab_data):
    return """<!DOCTYPE html>
<html lang="th" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ข้อมูลติดต่อ (Contact & Community) | 3D Printing Wiki</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', 'Noto Sans Thai', sans-serif; background-color: #0b0f19; color: #e2e8f0; }
    .glass-card { background: rgba(15, 23, 42, 0.78); backdrop-filter: blur(12px); border: 1px solid rgba(51, 65, 85, 0.6); }
  </style>
</head>
<body class="min-h-screen flex flex-col">
  <div id="header-mount"></div>
  <main class="flex-grow max-w-5xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="glass-card rounded-3xl p-8 sm:p-10 text-center relative overflow-hidden mb-8">
      <div class="w-16 h-16 rounded-2xl bg-cyan-500/15 border border-cyan-500/30 flex items-center justify-center mx-auto mb-4 text-cyan-400">
        <i data-lucide="mail" class="w-8 h-8"></i>
      </div>
      <span class="px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/15 text-cyan-300 border border-cyan-500/30">Tab 16: Contact & Contribution</span>
      <h1 class="text-3xl font-bold text-white mt-3">ติดต่อผู้จัดทำ & ชุมชน 3D Printing</h1>
      <p class="text-slate-400 max-w-xl mx-auto mt-2 text-sm sm:text-base">
        หากต้องการแจ้งเพิ่มรุ่นเครื่องพิมพ์ อัปเดตสเปกวัสดุ หรือแจ้งแก้ไขข้อมูลใน 3D Printer Thailand Master List สามารถติดต่อได้ตามช่องทางด้านล่างครับ
      </p>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8 text-left">
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-3">
              <div class="p-2.5 rounded-xl bg-cyan-500/15 text-cyan-400"><i data-lucide="at-sign" class="w-5 h-5"></i></div>
              <div>
                <div class="text-xs text-slate-400">อีเมลผู้จัดทำ (Compiled by Terasit J.)</div>
                <div class="text-base font-bold text-white">blazelabshop@gmail.com</div>
              </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
              ติดต่อสอบถาม ส่งข้อมูลสเปกเครื่องพิมพ์ 3 มิติ แผงวงจร หรือรายการเส้นพลาสติกเพิ่มเติมเข้าสู่ฐานข้อมูลหลัก
            </p>
          </div>
          <div class="mt-5 flex items-center gap-2">
            <a href="mailto:blazelabshop@gmail.com" class="px-4 py-2 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-semibold text-xs transition inline-flex items-center gap-1.5">
              <i data-lucide="send" class="w-3.5 h-3.5"></i> ส่งอีเมล
            </a>
            <button onclick="navigator.clipboard.writeText('blazelabshop@gmail.com'); this.textContent='คัดลอกแล้ว!';" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-medium transition">
              คัดลอกอีเมล
            </button>
          </div>
        </div>

        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
          <div>
            <div class="flex items-center gap-3 mb-3">
              <div class="p-2.5 rounded-xl bg-indigo-500/15 text-indigo-400"><i data-lucide="github" class="w-5 h-5"></i></div>
              <div>
                <div class="text-xs text-slate-400">GitHub Repository & Open Data</div>
                <div class="text-base font-bold text-white">3d-printing-knowledge-wiki</div>
              </div>
            </div>
            <p class="text-xs text-slate-400 leading-relaxed">
              ร่วมพัฒนาหน้าเว็บ Wiki เปิด Issue หรือส่ง Pull Request เพื่อเพิ่มเติมฟีเจอร์และอัปเดตข้อมูลบน GitHub
            </p>
          </div>
          <div class="mt-5 flex items-center gap-2">
            <a href="https://github.com/apiwat59/3d-printing-knowledge-wiki" target="_blank" class="px-4 py-2 rounded-xl bg-indigo-500 hover:bg-indigo-400 text-white font-semibold text-xs transition inline-flex items-center gap-1.5">
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i> เปิด GitHub Repo
            </a>
            <a href="./useful-links.html" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-medium transition">
              ดูรวมลิงก์ชุมชน
            </a>
          </div>
        </div>
      </div>
    </div>
  </main>
  <div id="footer-mount"></div>
  <script src="../assets/common.js"></script>
  <script>renderWikiHeader('contact', false);</script>
</body>
</html>"""

# Generate all 16 pages
for meta in TABS_META:
    out_file = os.path.join(PAGES_DIR, f"{meta['slug']}.html")
    content = generate_tab_page(meta)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated page: pages/{meta['slug']}.html")

print("All 16 tab pages generated successfully!")
