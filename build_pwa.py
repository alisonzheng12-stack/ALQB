"""產生 PWA 所需檔案：manifest.json、sw.js、icon PNG"""
import struct, zlib, json
from pathlib import Path

BASE = Path(__file__).parent

# ── 產生純色 PNG（不需要 Pillow）──────────────────────────
def make_png(size, bg, fg=None):
    """建立 size×size 的 PNG，bg=(r,g,b)，中間畫十字標示"""
    rows = []
    cx = size // 2
    for y in range(size):
        row = []
        for x in range(size):
            # 圓角遮罩（maskable icon 安全區）
            r2 = (x - cx)**2 + (y - cx)**2
            if r2 > (cx * 0.98)**2:
                row += [0, 0, 0, 0]  # 透明
            else:
                row += list(bg) + [255]
        rows.append(bytes(row))

    def chunk(tag, data):
        c = struct.pack('>I', len(data)) + tag + data
        return c + struct.pack('>I', zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = b''.join(b'\x00' + r for r in rows)
    ihdr = struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0)  # RGBA
    png  = (b'\x89PNG\r\n\x1a\n'
            + chunk(b'IHDR', ihdr)
            + chunk(b'IDAT', zlib.compress(raw, 9))
            + chunk(b'IEND', b''))
    return png

# 嘗試用 Pillow 做更漂亮的圖示
def make_icon_pillow(size):
    try:
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        r = int(size * 0.22)
        d.ellipse([0, 0, size, size], fill=(30, 30, 43, 255))
        # 書本圖案
        pad = size // 5
        d.rectangle([pad, pad, size-pad, size-pad-size//8],
                    fill=(79, 125, 243, 255), outline=(255,255,255,80), width=2)
        d.line([size//2, pad, size//2, size-pad-size//8],
               fill=(255, 255, 255, 120), width=max(2, size//40))
        from io import BytesIO
        buf = BytesIO()
        img.save(buf, 'PNG')
        return buf.getvalue()
    except ImportError:
        return None

# 產生圖示
for sz, name in [(192, 'icon-192.png'), (512, 'icon-512.png')]:
    data = make_icon_pillow(sz)
    if data is None:
        data = make_png(sz, (30, 30, 43))
    (BASE / name).write_bytes(data)
    print(f"{name}  ({len(data)//1024} KB)")

# ── manifest.json ─────────────────────────────────────────
manifest = {
    "name": "考試題庫",
    "short_name": "題庫",
    "description": "行政法・法學緒論・行政學選擇題練習",
    "start_url": "./index.html",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait-primary",
    "background_color": "#13131c",
    "theme_color": "#4f7df3",
    "lang": "zh-Hant",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png",
         "purpose": "maskable"},
    ],
    "shortcuts": [
        {"name": "行政法練習", "url": "./index.html?subj=adminlaw",
         "description": "直接開始行政法答題"},
        {"name": "法學緒論練習", "url": "./index.html?subj=faxu",
         "description": "直接開始法學緒論答題"},
        {"name": "行政學練習",  "url": "./index.html?subj=adminsci",
         "description": "直接開始行政學答題"},
    ]
}
(BASE / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print("manifest.json")

# ── service-worker.js ─────────────────────────────────────
sw = r"""/* 考試題庫 Service Worker */
const CACHE_NAME = 'quiz-cache-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './data_adminlaw.js',
  './data_faxu.js',
  './data_adminsci.js',
];

// 安裝：預先快取所有資源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

// 啟動：清除舊版快取
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// 攔截請求：Cache First（離線優先）
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(res => {
        // 只快取同域請求
        if (!res || res.status !== 200 || res.type !== 'basic') return res;
        const clone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
        return res;
      }).catch(() => caches.match('./index.html'));
    })
  );
});
"""
(BASE / "sw.js").write_text(sw, encoding="utf-8")
print("sw.js")

# ── 更新 index.html：加入 PWA 設定 ───────────────────────
html = (BASE / "index.html").read_text(encoding="utf-8")

PWA_HEAD = """<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-title" content="題庫">
<meta name="theme-color" content="#4f7df3" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#13131c" media="(prefers-color-scheme: dark)">"""

SW_SCRIPT = """<script>
if('serviceWorker' in navigator){
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .then(r => console.log('SW registered:', r.scope))
      .catch(e => console.log('SW error:', e));
  });
}
// URL 參數：?subj=adminlaw 直接跳科目
(function(){
  const p = new URLSearchParams(location.search).get('subj');
  if(p) window.__initSubj = p;
})();
</script>"""

# 只注入一次
if 'rel="manifest"' not in html:
    html = html.replace(
        '<meta name="apple-mobile-web-app-capable" content="yes">',
        '<meta name="apple-mobile-web-app-capable" content="yes">\n' + PWA_HEAD
    )
    print("注入 PWA <head> 標籤")

if 'serviceWorker' not in html:
    html = html.replace('</head>', SW_SCRIPT + '\n</head>', 1)
    print("注入 Service Worker 註冊")

# 讀取 URL 參數科目
if '__initSubj' not in html:
    html = html.replace(
        'initSubject(SUBJECTS[0].id);',
        'initSubject(window.__initSubj || SUBJECTS[0].id);'
    )
    print("加入 URL 參數科目跳轉")

(BASE / "index.html").write_text(html, encoding="utf-8")

print("\n完成！題庫合集資料夾：")
for f in sorted(BASE.iterdir()):
    if not f.name.startswith('.'):
        print(f"  {f.name:25} {f.stat().st_size//1024:>6} KB")
