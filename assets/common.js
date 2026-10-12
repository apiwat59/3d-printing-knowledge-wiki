// Shared Navigation and Footer Component for 3D Printing Knowledge Wiki

const WIKI_TABS = [
  { slug: "overview", name: "Overview ชีต", file: "overview.html", icon: "file-text", cat: "ทั่วไป" },
  { slug: "fdm-printers", name: "FDM 3D Printer", file: "fdm-printers.html", icon: "box", cat: "เครื่องพิมพ์" },
  { slug: "fdm-tool-changer", name: "FDM Tool Changer", file: "fdm-tool-changer.html", icon: "layers", cat: "เครื่องพิมพ์" },
  { slug: "fdm-diy", name: "FDM DIY & Kits", file: "fdm-diy.html", icon: "wrench", cat: "เครื่องพิมพ์" },
  { slug: "resin-printers", name: "Resin 3D Printer", file: "resin-printers.html", icon: "droplet", cat: "เครื่องพิมพ์" },
  { slug: "powder-printers", name: "Powder 3D Printer (SLS)", file: "powder-printers.html", icon: "sparkles", cat: "เครื่องพิมพ์" },
  { slug: "filament-material", name: "Filament Material (ยี่ห้อเส้น)", file: "filament-material.html", icon: "disc", cat: "วัสดุ" },
  { slug: "filament-properties", name: "Filament Properties (คุณสมบัติ)", file: "filament-properties.html", icon: "activity", cat: "วัสดุ" },
  { slug: "resin-material", name: "Resin Material (เรซิน)", file: "resin-material.html", icon: "flask-conical", cat: "วัสดุ" },
  { slug: "boards", name: "Boards (เมนบอร์ด)", file: "boards.html", icon: "cpu", cat: "ฮาร์ดแวร์" },
  { slug: "step-driver", name: "StepDriver (ไดรเวอร์)", file: "step-driver.html", icon: "zap", cat: "ฮาร์ดแวร์" },
  { slug: "stepper-motor", name: "StepperMotor (มอเตอร์)", file: "stepper-motor.html", icon: "compass", cat: "ฮาร์ดแวร์" },
  { slug: "mms", name: "MMS (พิมพ์หลากสี)", file: "mms.html", icon: "palette", cat: "อุปกรณ์เสริม" },
  { slug: "filament-dryer", name: "Filament Dryer (ตู้อบ)", file: "filament-dryer.html", icon: "sun", cat: "อุปกรณ์เสริม" },
  { slug: "useful-links", name: "Useful Links", file: "useful-links.html", icon: "link", cat: "อื่น ๆ" },
  { slug: "contact", name: "Contact", file: "contact.html", icon: "mail", cat: "อื่น ๆ" }
];

function renderWikiHeader(currentSlug, isRoot = false) {
  const rootPath = isRoot ? "./" : "../";
  const pagesPath = isRoot ? "./pages/" : "./";
  
  const headerHtml = `
  <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-50 backdrop-blur-md bg-opacity-95 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center space-x-3">
          <a href="${rootPath}index.html" class="flex items-center space-x-2 text-cyan-400 hover:text-cyan-300 transition-colors">
            <span class="text-2xl">🖨️</span>
            <div>
              <span class="font-bold text-lg text-white">3D Printing</span>
              <span class="text-cyan-400 font-semibold text-lg ml-1">Wiki</span>
              <span class="hidden sm:inline-block text-xs bg-slate-800 text-slate-400 px-2 py-0.5 rounded-full ml-2 border border-slate-700">Thailand Master List</span>
            </div>
          </a>
        </div>
        
        <div class="flex items-center space-x-3">
          <!-- Dropdown Navigation -->
          <div class="relative group">
            <button class="flex items-center space-x-1.5 px-3 py-1.5 text-sm font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg border border-slate-700 transition">
              <span>หมวดหมู่ทั้งหมด (16 Tabs)</span>
              <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400"></i>
            </button>
            <div class="absolute right-0 mt-2 w-72 bg-slate-800 border border-slate-700 rounded-xl shadow-2xl py-2 hidden group-hover:block z-50 max-h-[80vh] overflow-y-auto">
              <a href="${rootPath}index.html" class="flex items-center px-4 py-2 text-sm text-cyan-300 hover:bg-slate-700/60 font-medium">
                <i data-lucide="home" class="w-4 h-4 mr-2.5"></i> หน้าแรก & เปรียบเทียบ
              </a>
              <div class="border-t border-slate-700 my-1"></div>
              ${WIKI_TABS.map(tab => `
                <a href="${pagesPath}${tab.file}" class="flex items-center justify-between px-4 py-2 text-sm ${tab.slug === currentSlug ? 'bg-cyan-500/10 text-cyan-400 font-semibold' : 'text-slate-300 hover:bg-slate-700/50 hover:text-white'}">
                  <span class="flex items-center truncate">
                    <i data-lucide="${tab.icon}" class="w-4 h-4 mr-2.5 flex-shrink-0 text-slate-400"></i>
                    <span class="truncate">${tab.name}</span>
                  </span>
                  <span class="text-[10px] bg-slate-900 text-slate-400 px-1.5 py-0.5 rounded ml-2">${tab.cat}</span>
                </a>
              `).join('')}
            </div>
          </div>

          <a href="https://github.com/apiwat59/3d-printing-knowledge-wiki" target="_blank" class="p-2 text-slate-400 hover:text-white hover:bg-slate-800 rounded-lg transition" title="GitHub Repository">
            <i data-lucide="github" class="w-5 h-5"></i>
          </a>
        </div>
      </div>
    </div>
  </header>
  `;

  const footerHtml = `
  <footer class="bg-slate-950 border-t border-slate-800/80 text-slate-400 py-10 mt-16 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-2 text-cyan-400 mb-3">
            <span class="text-2xl">🖨️</span>
            <span class="font-bold text-lg text-white">3D Printing Knowledge Wiki</span>
          </div>
          <p class="text-slate-400 text-sm max-w-md leading-relaxed">
            แหล่งรวบรวมข้อมูลสเปกเครื่องพิมพ์ 3 มิติ เส้นวัสดุ เรซิน และอุปกรณ์ฮาร์ดแวร์ ครบครันที่สุด แปลงจากข้อมูลต้นฉบับ 3D Printer Thailand Master List
          </p>
          <div class="mt-4 flex items-center space-x-4 text-xs text-slate-500">
            <span>Compiled by Terasit J.</span>
            <span>•</span>
            <span>Created for Community</span>
          </div>
        </div>
        <div>
          <h4 class="text-slate-200 font-semibold text-sm mb-3">หมวดหมู่แนะนำ</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="${pagesPath}fdm-printers.html" class="hover:text-cyan-400 transition">FDM 3D Printers</a></li>
            <li><a href="${pagesPath}filament-properties.html" class="hover:text-cyan-400 transition">Filament Properties</a></li>
            <li><a href="${pagesPath}resin-printers.html" class="hover:text-cyan-400 transition">Resin 3D Printers</a></li>
            <li><a href="${pagesPath}boards.html" class="hover:text-cyan-400 transition">Controller Boards</a></li>
          </ul>
        </div>
        <div>
          <h4 class="text-slate-200 font-semibold text-sm mb-3">ลิงก์ที่เป็นประโยชน์</h4>
          <ul class="space-y-2 text-xs">
            <li><a href="${rootPath}index.html" class="hover:text-cyan-400 transition">หน้าแรก & ระบบเปรียบเทียบ</a></li>
            <li><a href="${pagesPath}useful-links.html" class="hover:text-cyan-400 transition">Useful Links & Tools</a></li>
            <li><a href="${pagesPath}contact.html" class="hover:text-cyan-400 transition">ข้อมูลติดต่อ (Contact)</a></li>
            <li><a href="https://github.com/apiwat59/3d-printing-knowledge-wiki" target="_blank" class="hover:text-cyan-400 transition">GitHub Repository</a></li>
          </ul>
        </div>
      </div>
      <div class="pt-6 border-t border-slate-800 text-center text-xs text-slate-500 flex flex-col sm:flex-row justify-between items-center gap-2">
        <span>© 2026 3D Printing Knowledge Wiki. Open for all makers.</span>
        <span>Hosted with GitHub Pages</span>
      </div>
    </div>
  </footer>
  `;

  const headerMount = document.getElementById("header-mount");
  if (headerMount) headerMount.innerHTML = headerHtml;
  const footerMount = document.getElementById("footer-mount");
  if (footerMount) footerMount.innerHTML = footerHtml;

  if (window.lucide) {
    window.lucide.createIcons();
  }
}
