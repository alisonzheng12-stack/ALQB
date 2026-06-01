"""產生合併題庫網站：一個 index.html + 三個資料檔"""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent

SUBJECTS = [
    {
        "id":    "adminlaw",
        "name":  "行政法",
        "icon":  "⚖️",
        "color": "#4f7df3",
        "color2":"#3a66d8",
        "bg":    "#f0f2f5",
        "store": "al_stats",
        "wstore":"al_wrong",
        "json":  r"C:\Users\USER\Desktop\行政法題庫\questions.json",
        "groups": [
            ("行政處分","#6366f1",["行政處分","授益處分","負擔處分","撤銷","廢止","無效","行政行為","構成要件","行政命令","法規命令","行政規則","職權命令"]),
            ("附款","#8b5cf6",["附款","條件","期限","負擔","廢止權保留","停止條件","解除條件","不當聯結"]),
            ("行政契約","#a855f7",["行政契約","雙務契約","行政協定","和解契約","私法契約"]),
            ("行政程序","#3b82f6",["行政程序","陳述意見","聽證","閱覽","送達","期日","期間","行政程序法","告知","通知","公告"]),
            ("行政罰","#f97316",["行政罰","裁罰","罰鍰","沒入","一行為不二罰","故意","過失","行政秩序罰","裁處","處罰"]),
            ("行政執行","#ef4444",["行政執行","強制執行","即時強制","代履行","怠金","直接強制","間接強制"]),
            ("訴願","#f59e0b",["訴願","訴願人","訴願管轄","訴願法","訴願決定","訴願機關"]),
            ("行政訴訟","#eab308",["行政訴訟","撤銷訴訟","課予義務","確認訴訟","一般給付","行政法院","起訴"]),
            ("行政組織","#22c55e",["行政機關","管轄","委任","委託","委辦","公法人","行政法人","機關"]),
            ("地方自治","#10b981",["地方自治","自治條例","自治規則","地方制度","直轄市","自治事項","委辦事項"]),
            ("法律原則","#14b8a6",["比例原則","信賴保護","平等原則","依法行政","法律保留","法律優位","明確性原則","誠信原則"]),
            ("裁量判斷","#06b6d4",["裁量","判斷餘地","不確定法律概念","裁量濫用","裁量怠惰","裁量基準","自由裁量"]),
            ("公務員","#0ea5e9",["公務員","公務人員","特別權力","職務","懲戒","記過","考績","任用"]),
            ("國家賠償","#64748b",["國家賠償","損失補償","徵收","損害賠償","賠償責任","國賠","特別犧牲"]),
            ("行政指導","#84cc16",["行政指導","行政計畫","計畫確定","指導","非權力"]),
        ],
    },
    {
        "id":    "faxu",
        "name":  "法學緒論",
        "icon":  "📖",
        "color": "#7c3aed",
        "color2":"#6d28d9",
        "bg":    "#f5f0ff",
        "store": "fx_stats",
        "wstore":"fx_wrong",
        "json":  r"C:\Users\USER\Desktop\法緒題庫\questions.json",
        "groups": [
            ("法律的概念","#7c3aed",["法律的意義","法律定義","法律與道德","規範","社會規範","法的意義","成文法","不成文法","制定法"]),
            ("法律的分類","#6d28d9",["公法","私法","社會法","國際法","實體法","程序法","強行法","任意法","普通法","特別法"]),
            ("法源","#4f46e5",["法源","習慣","判例","法理","條約","慣例","不文法","法律淵源"]),
            ("法律的效力","#2563eb",["效力","法律效力","時間效力","空間效力","人的效力","屬地","屬人","溯及既往","不溯及既往"]),
            ("法律的解釋","#0891b2",["解釋","文義解釋","目的解釋","體系解釋","合憲解釋","擴張解釋","限縮解釋","類推適用"]),
            ("法律的適用","#0d9488",["法律適用","特別法","後法","新法","舊法","衝突","法律競合","優先適用","準用"]),
            ("權利與義務","#059669",["權利","義務","公權利","私權利","形成權","請求權","抗辯權","支配權","人格權","財產權"]),
            ("法律關係","#16a34a",["法律關係","主體","客體","法律事實","法律行為","事件","權利主體","義務主體"]),
            ("法律行為","#65a30d",["法律行為","意思表示","行為能力","意思能力","瑕疵","無效","得撤銷","代理","無權代理","表見代理"]),
            ("民法","#ca8a04",["民法","民事","物權","債權","契約","侵權","親屬","繼承","時效","所有權","占有","抵押","保證","買賣","租賃"]),
            ("刑法","#dc2626",["刑法","刑事","犯罪","故意","過失","既遂","未遂","共犯","正犯","教唆","幫助","罪刑","刑罰","構成要件"]),
            ("憲法","#db2777",["憲法","基本權","人權","自由","平等","正當程序","大法官","釋憲","修憲","違憲","國家機關","立法院","行政院"]),
            ("訴訟程序","#9333ea",["訴訟","訴訟程序","起訴","上訴","再審","管轄","法院","裁判","判決","裁定","證據","原告","被告"]),
            ("責任與制裁","#64748b",["責任","制裁","民事責任","刑事責任","行政責任","賠償","損害","違法","處罰"]),
            ("國際法","#0ea5e9",["國際法","條約","國際習慣","國際公法","國際私法","外交","主權","國籍","引渡"]),
        ],
    },
    {
        "id":    "adminsci",
        "name":  "行政學",
        "icon":  "🏛️",
        "color": "#0891b2",
        "color2":"#0e7490",
        "bg":    "#f0f9ff",
        "store": "as_stats",
        "wstore":"as_wrong",
        "json":  r"C:\Users\USER\Desktop\行政學題庫\questions.json",
        "groups": [
            ("行政學概念","#0891b2",["行政","公共行政","行政學","行政意義","行政定義","行政功能","行政目標"]),
            ("組織理論","#6366f1",["組織","組織理論","組織結構","科層","官僚","韋伯","層級","分工","正式組織","非正式組織","矩陣","委員會"]),
            ("管理理論","#8b5cf6",["管理","科學管理","泰勒","費堯","管理原則","POSDCORB","古立克","行為科學","霍桑","人際關係","系統理論","權變理論"]),
            ("領導與激勵","#a855f7",["領導","領導理論","領導風格","激勵","需求層次","馬斯洛","赫茲伯格","雙因素","期望理論","X理論","Y理論","Z理論","授權","賦權"]),
            ("決策理論","#3b82f6",["決策","決策理論","理性模型","有限理性","漸進主義","混合掃描","垃圾桶","決策過程","西蒙","林布隆"]),
            ("溝通與協調","#0ea5e9",["溝通","協調","橫向協調","縱向協調","正式溝通","非正式溝通","溝通障礙","衝突管理"]),
            ("人事行政","#22c55e",["人事","人事行政","文官","功績制","分類","職位分類","品位制","考試","任用","銓敘","考績","訓練","俸給","退休"]),
            ("財務行政","#16a34a",["財務","預算","財務行政","公共預算","編列","審議","決算","會計","審計","採購","績效預算","零基預算","PPBS"]),
            ("行政監督","#f59e0b",["監督","行政監督","課責","立法監督","司法監督","行政控制","監察","督導","績效管理","評估"]),
            ("公共政策","#f97316",["公共政策","政策","政策分析","政策制定","政策執行","政策評估","政策終結","議程設定","政策規劃","利害關係人"]),
            ("行政倫理","#ef4444",["行政倫理","倫理","廉政","貪腐","利益衝突","公務倫理","道德","行政責任","課責","中立"]),
            ("地方政府","#10b981",["地方政府","地方行政","地方自治","縣市","鄉鎮","區","地方財政","地方立法","中央地方"]),
            ("政府改造","#14b8a6",["政府改造","行政革新","新公共管理","NPM","治理","電子化政府","民營化","委外","績效","顧客導向","企業型政府"]),
            ("比較行政","#06b6d4",["比較行政","比較","各國行政","開發中國家","行政文化","行政生態","官僚文化","政治文化"]),
            ("非營利組織","#84cc16",["非營利","NPO","NGO","第三部門","公民社會","志願服務","社會企業","基金會","協會"]),
        ],
    },
]

# ── 產生三個資料 JS 檔 ──────────────────────────────────────
for subj in SUBJECTS:
    jpath = Path(subj["json"])
    if not jpath.exists():
        print(f"找不到：{jpath}")
        continue
    data = json.loads(jpath.read_text(encoding="utf-8"))
    js_var = f"const DATA_{subj['id'].upper()}={json.dumps(data, ensure_ascii=True)};"
    out = BASE / f"data_{subj['id']}.js"
    out.write_text(js_var, encoding="utf-8")
    sys.stdout.buffer.write(f"data_{subj['id']}.js  ({len(js_var)//1024} KB, {len(data)} 題)\n".encode("utf-8"))
    sys.stdout.flush()

# ── 產生 index.html ─────────────────────────────────────────
# 把分組設定序列化成 JS
def groups_to_js(groups):
    parts = []
    for name, color, keywords in groups:
        kws = json.dumps(keywords, ensure_ascii=False)
        parts.append(f"{{name:{json.dumps(name,ensure_ascii=False)},color:{json.dumps(color,ensure_ascii=False)},keywords:{kws}}}")
    return "[" + ",".join(parts) + "]"

subjects_js = json.dumps([
    {
        "id": s["id"], "name": s["name"], "icon": s["icon"],
        "color": s["color"], "color2": s["color2"], "bg": s["bg"],
        "store": s["store"], "wstore": s["wstore"],
        "dataVar": f"DATA_{s['id'].upper()}",
    }
    for s in SUBJECTS
], ensure_ascii=False)

groups_map_js = "{" + ",".join(
    f"{json.dumps(s['id'],ensure_ascii=False)}:{groups_to_js(s['groups'])}"
    for s in SUBJECTS
) + "}"

html = r"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>考試題庫</title>
<script src="data_adminlaw.js"></script>
<script src="data_faxu.js"></script>
<script src="data_adminsci.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Noto Sans TC",sans-serif;background:#f0f2f5;color:#1a1a2e;min-height:100vh;padding-top:58px;padding-bottom:70px}

/* 頂部科目切換 */
.subject-bar{position:fixed;top:0;left:0;right:0;height:54px;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;gap:8px;padding:0 16px;z-index:100;overflow-x:auto;scrollbar-width:none;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.subject-bar::-webkit-scrollbar{display:none}
.subj-btn{flex-shrink:0;padding:7px 18px;border-radius:99px;border:2px solid #e0e0e0;background:#fafafa;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;color:#888;white-space:nowrap}
.subj-btn.active{color:#fff;border-color:transparent}

/* 底部導覽 */
.nav-bar{position:fixed;bottom:0;left:0;right:0;height:62px;background:#fff;border-top:1px solid #eee;display:flex;z-index:100;box-shadow:0 -2px 12px rgba(0,0,0,.06)}
.nav-btn{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;border:none;background:none;cursor:pointer;font-size:11px;color:#aaa;font-weight:600;transition:color .2s}
.nav-btn svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

/* 頁面 */
.page{display:none;max-width:640px;margin:0 auto;padding:16px 16px 0}
.page.active{display:block}
.page-header{font-size:20px;font-weight:800;margin-bottom:16px;padding-top:4px}

/* 通用 */
.card{background:#fff;border-radius:16px;padding:20px 18px;box-shadow:0 2px 12px rgba(0,0,0,.06);margin-bottom:12px}
.setting-label{font-size:12px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:.6px;margin-bottom:7px;display:block}
.setting-group{margin-bottom:14px}
select,input[type=number]{width:100%;padding:10px 13px;border:1.5px solid #e8e8e8;border-radius:10px;font-size:15px;outline:none;background:#fafafa;transition:border-color .2s;color:#1a1a2e}
.btn-primary{width:100%;padding:14px;color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;transition:background .2s,transform .1s;margin-top:6px}
.btn-primary:active{transform:scale(.98)}
.btn-danger{background:#ef4444!important}
.btn-danger:hover{background:#dc2626!important}
.stat-row{display:flex;gap:8px;margin-bottom:12px}
.stat-box{flex:1;background:#fff;border-radius:13px;padding:14px 8px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.06)}
.stat-box .num{font-size:24px;font-weight:800}
.stat-box .lbl{font-size:11px;color:#aaa;margin-top:2px}

/* 答題 overlay */
#quiz-overlay{display:none;position:fixed;inset:0;background:#f0f2f5;z-index:200;overflow-y:auto;padding-bottom:24px;padding-top:0}
.quiz-inner{max-width:640px;margin:0 auto;padding:14px}
.top-bar{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:#888;margin:10px 0 5px}
.btn-quit{background:none;border:none;font-size:13px;color:#aaa;cursor:pointer;padding:4px 8px;border-radius:8px}
.progress-bar-wrap{background:#e0e0e0;border-radius:99px;height:5px;margin-bottom:18px;overflow:hidden}
.progress-bar-fill{height:100%;border-radius:99px;transition:width .4s}
.question-card{background:#fff;border-radius:16px;padding:22px 20px;box-shadow:0 4px 20px rgba(0,0,0,.06);margin-bottom:12px}
.exam-tag{font-size:11px;color:#888;background:#f0f2f5;border-radius:6px;padding:3px 8px;display:inline-block;margin-bottom:8px;max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kw-tags{margin-bottom:10px;display:flex;flex-wrap:wrap;gap:4px}
.kw-tag{font-size:11px;padding:2px 8px;border-radius:99px;font-weight:600}
.question-text{font-size:16px;font-weight:600;line-height:1.65;margin-bottom:18px}
.options{display:flex;flex-direction:column;gap:9px}
.option-btn{display:flex;align-items:flex-start;gap:11px;padding:12px 15px;border:2px solid #e8e8e8;border-radius:11px;background:#fafafa;font-size:14px;line-height:1.5;cursor:pointer;text-align:left;width:100%;transition:border-color .15s,background .15s}
.option-btn:hover:not(:disabled){border-color:var(--accent);background:var(--bg)}
.option-label{flex-shrink:0;width:26px;height:26px;border-radius:50%;background:#e8e8e8;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;transition:background .15s,color .15s}
.option-btn.correct{border-color:#22c55e;background:#f0fdf4}.option-btn.correct .option-label{background:#22c55e;color:#fff}
.option-btn.wrong{border-color:#ef4444;background:#fff5f5}.option-btn.wrong .option-label{background:#ef4444;color:#fff}
.option-btn.show-correct{border-color:#22c55e;background:#f0fdf4}.option-btn.show-correct .option-label{background:#22c55e;color:#fff}
.feedback{margin-top:12px;padding:11px 15px;border-radius:10px;font-size:14px;font-weight:600;display:none}
.feedback.correct{background:#f0fdf4;color:#16a34a}
.feedback.wrong{background:#fff5f5;color:#dc2626}
.btn-next{width:100%;padding:13px;background:#1a1a2e;color:#fff;border:none;border-radius:11px;font-size:15px;font-weight:700;cursor:pointer;display:none;margin-top:4px}

/* 結果 overlay */
#result-overlay{display:none;position:fixed;inset:0;background:#f0f2f5;z-index:300;overflow-y:auto;padding:20px 16px 24px}
.result-inner{max-width:640px;margin:0 auto}
.result-card{background:#fff;border-radius:18px;padding:24px 20px;box-shadow:0 4px 20px rgba(0,0,0,.06);margin-bottom:12px}
.score-row{display:flex;align-items:center;gap:18px;margin-bottom:20px}
.score-circle{width:80px;height:80px;border-radius:50%;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;flex-shrink:0}
.score-circle .num{font-size:26px;font-weight:800;line-height:1}
.score-circle .unit{font-size:11px;opacity:.8;margin-top:2px}
.score-info h2{font-size:18px;font-weight:700;margin-bottom:4px}
.score-info .detail{color:#888;font-size:13px}

/* 分析 */
.analysis-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.analysis-header h2{font-size:20px;font-weight:800}
.btn-clear{font-size:12px;color:#aaa;border:1px solid #e0e0e0;background:#fff;border-radius:8px;padding:5px 11px;cursor:pointer}
.section-title{font-size:13px;font-weight:700;color:#333;margin-bottom:3px}
.section-sub{font-size:11px;color:#aaa;margin-bottom:12px}
.legend{display:flex;gap:14px;margin-bottom:12px;font-size:11px;color:#666}
.legend-item{display:flex;align-items:center;gap:4px}
.legend-dot{width:13px;height:3px;border-radius:2px}
.radar-wrap{display:flex;justify-content:center;margin-bottom:4px}
svg.radar{overflow:visible}
.radar-grid{fill:none;stroke:#e8e8e8;stroke-width:1}
.radar-axis{stroke:#ddd;stroke-width:1}
.radar-area-wrong{fill:#fca5a5;fill-opacity:.55;stroke:#ef4444;stroke-width:2}
.radar-label{font-size:10.5px;fill:#444;font-family:-apple-system,sans-serif}
.radar-dot{fill:#ef4444}
.radar-pct{font-size:9.5px;fill:#ef4444;font-weight:700}
.weak-item{display:flex;align-items:center;justify-content:space-between;padding:8px 11px;border-radius:9px;margin-bottom:5px}
.weak-item-left{display:flex;align-items:center;gap:9px}
.weak-dot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.weak-name{font-size:12px;font-weight:600}
.weak-bar-wrap{flex:1;margin:0 10px;border-radius:99px;height:5px;overflow:hidden}
.weak-bar-fill{height:100%;border-radius:99px}
.weak-pct{font-size:11px;font-weight:700;white-space:nowrap}

/* 錯題 */
.wrong-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.wrong-header h2{font-size:20px;font-weight:800}
.wrong-count-badge{background:#ef4444;color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:99px}
.wrong-filter{display:flex;gap:7px;overflow-x:auto;padding-bottom:3px;margin-bottom:13px;scrollbar-width:none}
.wrong-filter::-webkit-scrollbar{display:none}
.filter-chip{flex-shrink:0;padding:5px 13px;border-radius:99px;font-size:11px;font-weight:600;border:1.5px solid #e0e0e0;background:#fff;cursor:pointer;color:#666;transition:all .15s}
.filter-chip.active{color:#fff;border-color:transparent}
.wq-card{background:#fff;border-radius:14px;padding:16px 16px 10px;box-shadow:0 2px 12px rgba(0,0,0,.06);margin-bottom:10px}
.wq-meta{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.wq-exam{font-size:11px;color:#aaa;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.wq-wrong-count{flex-shrink:0;font-size:11px;font-weight:700;color:#ef4444;background:#fff5f5;padding:2px 7px;border-radius:99px;margin-left:7px}
.wq-groups{display:flex;flex-wrap:wrap;gap:3px;margin-bottom:8px}
.wq-question{font-size:14px;font-weight:600;line-height:1.6;margin-bottom:12px}
.wq-options{display:flex;flex-direction:column;gap:5px;margin-bottom:10px}
.wq-option{display:flex;gap:9px;padding:8px 11px;border-radius:9px;font-size:12px;line-height:1.4;background:#f8f8f8;border:1.5px solid transparent}
.wq-option.is-answer{background:#f0fdf4;border-color:#22c55e}
.wq-option-label{flex-shrink:0;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:10px;background:#e0e0e0}
.wq-option.is-answer .wq-option-label{background:#22c55e;color:#fff}
.wq-note-toggle{font-size:11px;cursor:pointer;background:none;border:none;padding:3px 0;font-weight:600}
.wq-note-area{margin-top:8px;display:none}
.wq-note-area.open{display:block}
.wq-textarea{width:100%;padding:9px 11px;border:1.5px solid #e0e0e0;border-radius:9px;font-size:12px;line-height:1.6;resize:vertical;min-height:70px;outline:none;font-family:inherit;transition:border-color .2s}
.wq-note-actions{display:flex;gap:7px;margin-top:7px}
.wq-save-btn{padding:6px 14px;color:#fff;border:none;border-radius:7px;font-size:12px;font-weight:600;cursor:pointer}
.wq-del-btn{padding:6px 14px;background:#fff;color:#ef4444;border:1.5px solid #ef4444;border-radius:7px;font-size:12px;font-weight:600;cursor:pointer}
.wq-saved-note{margin-top:7px;padding:9px 11px;background:#f0fdf4;border-radius:9px;font-size:12px;color:#166534;line-height:1.6;border-left:3px solid #22c55e;white-space:pre-wrap}
.empty-msg{text-align:center;padding:36px 20px;color:#bbb;font-size:13px;line-height:1.8}
.no-wrong{text-align:center;padding:18px;color:#22c55e;font-weight:600;font-size:13px}
</style>
</head>
<body>

<!-- 頂部科目切換 -->
<div class="subject-bar" id="subject-bar"></div>

<!-- 底部導覽 -->
<nav class="nav-bar" id="nav-bar">
  <button class="nav-btn active" id="nav-practice" onclick="showPage('practice')">
    <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>練習
  </button>
  <button class="nav-btn" id="nav-wrong" onclick="showPage('wrong')">
    <svg viewBox="0 0 24 24"><path d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 10z"/><path d="M15 9l-6 6"/><path d="M9 9l6 6"/></svg>錯題
  </button>
  <button class="nav-btn" id="nav-analysis" onclick="showPage('analysis')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 010 20"/><path d="M2 12h20"/><path d="M12 2c2.8 2.7 4 6 4 10s-1.2 7.3-4 10"/></svg>分析
  </button>
</nav>

<!-- 練習頁 -->
<div class="page active" id="page-practice">
  <div class="page-header" id="page-title">題庫</div>
  <div class="stat-row">
    <div class="stat-box"><div class="num" id="stat-total-q" style="font-size:20px">0</div><div class="lbl">題庫題數</div></div>
    <div class="stat-box"><div class="num" id="stat-done" style="font-size:20px">0</div><div class="lbl">累計作答</div></div>
    <div class="stat-box"><div class="num" id="stat-acc" style="font-size:20px">--</div><div class="lbl">正確率</div></div>
  </div>
  <div class="card">
    <div class="setting-group"><span class="setting-label">出題範圍</span>
      <select id="filter-exam"><option value="all">全部考試</option></select></div>
    <div class="setting-group"><span class="setting-label">出題數量</span>
      <input type="number" id="num-questions" value="20" min="5" max="9999"></div>
    <button class="btn-primary" id="btn-start" onclick="startQuiz()">開始答題</button>
    <button class="btn-primary btn-danger" onclick="resetAll()" style="margin-top:8px">&#128465; 資料全部重置</button>
  </div>
</div>

<!-- 錯題頁 -->
<div class="page" id="page-wrong">
  <div class="wrong-header"><h2>&#128204; 錯題本</h2><span class="wrong-count-badge" id="wrong-badge">0 題</span></div>
  <div class="wrong-filter" id="wrong-filter"></div>
  <div id="wrong-list"></div>
</div>

<!-- 分析頁 -->
<div class="page" id="page-analysis">
  <div class="analysis-header"><h2>&#128202; 錯題分析</h2><button class="btn-clear" onclick="clearStats()">清除統計</button></div>
  <div class="card"><div id="analysis-content"></div></div>
</div>

<!-- 答題 overlay -->
<div id="quiz-overlay">
  <div class="quiz-inner">
    <div class="top-bar"><span id="q-counter"></span><span id="score-live"></span><button class="btn-quit" onclick="quitQuiz()">&#10005; 離開</button></div>
    <div class="progress-bar-wrap"><div class="progress-bar-fill" id="progress-fill" style="width:0%"></div></div>
    <div class="question-card">
      <span class="exam-tag" id="exam-tag"></span>
      <div class="kw-tags" id="kw-tags"></div>
      <div class="question-text" id="question-text"></div>
      <div class="options" id="options"></div>
      <div class="feedback" id="feedback"></div>
    </div>
    <button class="btn-next" id="btn-next" onclick="nextQuestion()"></button>
  </div>
</div>

<!-- 結果 overlay -->
<div id="result-overlay">
  <div class="result-inner">
    <div class="result-card">
      <div class="score-row">
        <div class="score-circle" id="score-circle"><span class="num" id="final-score">0</span><span class="unit">分</span></div>
        <div class="score-info"><h2 id="result-title"></h2><p class="detail" id="result-detail"></p></div>
      </div>
      <div class="section-title" style="margin-bottom:10px">本次錯題分布</div>
      <div class="radar-wrap"><svg class="radar" id="session-radar" viewBox="0 0 500 500" width="280" height="280"></svg></div>
      <div id="session-weak"></div>
    </div>
    <div style="display:flex;gap:10px">
      <button class="btn-primary" id="btn-again" onclick="restartSame()" style="flex:1">再來一次</button>
      <button class="btn-primary" onclick="goHome()" style="flex:1;background:#f0f2f5;color:#444">回首頁</button>
    </div>
  </div>
</div>

<script>
// ── 設定 ────────────────────────────────────────────────
const SUBJECTS = ##SUBJECTS##;
const GROUPS_MAP = ##GROUPS_MAP##;
const DATA_MAP = {
  adminlaw: typeof DATA_ADMINLAW!=='undefined'?DATA_ADMINLAW:[],
  faxu:     typeof DATA_FAXU!=='undefined'?DATA_FAXU:[],
  adminsci: typeof DATA_ADMINSCI!=='undefined'?DATA_ADMINSCI:[],
};
const DIFFICULTY = new Set(['非常簡單','簡單','適中','困難','非常困難','計算中']);

// ── 狀態 ────────────────────────────────────────────────
let curSubjId = SUBJECTS[0].id;
let curSubj   = SUBJECTS[0];
let curGroups = GROUPS_MAP[curSubjId];
let allQ = [];

function qHash(q){let h=0;for(const c of(q.question||''))h=(Math.imul(31,h)+c.charCodeAt(0))|0;return Math.abs(h).toString(36)}
function tagQ(q){
  const txt=(q.question||'')+Object.values(q.options||{}).join('');
  const m=curGroups.filter(g=>g.keywords.some(kw=>txt.includes(kw))).map(g=>g.name);
  return m.length?m:['其他'];
}

// ── 初始化科目 ──────────────────────────────────────────
function initSubject(id){
  curSubjId = id;
  curSubj   = SUBJECTS.find(s=>s.id===id);
  curGroups = GROUPS_MAP[id];

  // CSS 變數
  document.documentElement.style.setProperty('--accent', curSubj.color);
  document.documentElement.style.setProperty('--bg', curSubj.bg);
  document.body.style.background = curSubj.bg;

  // 頂部按鈕樣式
  document.querySelectorAll('.subj-btn').forEach(b=>{
    const active = b.dataset.id===id;
    b.classList.toggle('active',active);
    b.style.background = active ? curSubj.color : '';
    b.style.color      = active ? '#fff' : '';
  });

  // 底部 nav 顏色
  document.querySelectorAll('.nav-btn.active').forEach(b=>{b.style.color=curSubj.color});
  document.querySelector('.nav-bar').style.setProperty('--nb-color', curSubj.color);

  // 標題
  document.getElementById('page-title').textContent = curSubj.icon+' '+curSubj.name+'題庫';
  document.getElementById('btn-start').style.background = curSubj.color;

  // 處理題目資料
  const raw = DATA_MAP[id]||[];
  allQ = raw.filter(q=>
    q.question&&q.question.length>5&&
    q.options&&Object.keys(q.options).length>=2&&
    !DIFFICULTY.has(q.question)
  ).map(q=>({...q,groups:tagQ(q),id:qHash(q)}));
  document.getElementById('stat-total-q').textContent = allQ.length;

  // 年度選單
  const sel = document.getElementById('filter-exam');
  sel.innerHTML = '<option value="all">全部考試</option>';
  [...new Set(allQ.map(q=>{const m=q.exam.match(/^(\d+)年/);return m?m[1]+'年':null}).filter(Boolean))]
    .sort((a,b)=>b.localeCompare(a))
    .forEach(y=>{const o=document.createElement('option');o.value=y;o.textContent=y+' 考試';sel.appendChild(o)});

  updateStats();
  if(curPage==='wrong')renderWrong();
  if(curPage==='analysis')renderAnalysis();
}

// ── 建立科目切換按鈕 ────────────────────────────────────
const bar = document.getElementById('subject-bar');
SUBJECTS.forEach(s=>{
  const btn = document.createElement('button');
  btn.className='subj-btn';
  btn.dataset.id=s.id;
  btn.textContent=s.icon+' '+s.name;
  btn.onclick=()=>initSubject(s.id);
  bar.appendChild(btn);
});

// ── 頁面切換 ────────────────────────────────────────────
let curPage = 'practice';
function showPage(id){
  curPage=id;
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(b=>{b.classList.remove('active');b.style.color=''});
  document.getElementById('page-'+id).classList.add('active');
  const nb=document.getElementById('nav-'+id);nb.classList.add('active');nb.style.color=curSubj.color;
  if(id==='analysis')renderAnalysis();
  if(id==='wrong')renderWrong();
}

// ── localStorage ────────────────────────────────────────
function loadS(){try{return JSON.parse(localStorage.getItem(curSubj.store))||{wrongByGroup:{},totalByGroup:{},totalAnswered:0,totalCorrect:0,sessions:0}}catch{return{wrongByGroup:{},totalByGroup:{},totalAnswered:0,totalCorrect:0,sessions:0}}}
function saveS(s){localStorage.setItem(curSubj.store,JSON.stringify(s))}
function loadWQ(){try{return JSON.parse(localStorage.getItem(curSubj.wstore))||{}}catch{return{}}}
function saveWQ(wq){localStorage.setItem(curSubj.wstore,JSON.stringify(wq))}
function updateStats(){
  const s=loadS();
  document.getElementById('stat-done').textContent=s.totalAnswered||0;
  document.getElementById('stat-acc').textContent=s.totalAnswered>0?Math.round(s.totalCorrect/s.totalAnswered*100)+'%':'--';
}

// ── 答題 ────────────────────────────────────────────────
let quizQ=[],idx=0,score=0,answered=false,sWrong={},sTotal={},lastF='all',lastN=20;
function startQuiz(){
  const f=document.getElementById('filter-exam').value;
  const n=parseInt(document.getElementById('num-questions').value)||20;
  lastF=f;lastN=n;
  let pool=f==='all'?allQ:allQ.filter(q=>q.exam.startsWith(f));
  if(!pool.length){alert('該範圍沒有題目');return}
  quizQ=[...pool].sort(()=>Math.random()-.5).slice(0,Math.min(n,pool.length));
  idx=0;score=0;sWrong={};sTotal={};
  document.getElementById('quiz-overlay').style.background=curSubj.bg;
  document.getElementById('quiz-overlay').style.display='block';
  document.getElementById('progress-fill').style.background=curSubj.color;
  renderQ();
}
function quitQuiz(){if(idx>0&&!confirm('確定要離開？'))return;document.getElementById('quiz-overlay').style.display='none'}
function renderQ(){
  answered=false;const q=quizQ[idx],total=quizQ.length;
  document.getElementById('q-counter').textContent='第 '+(idx+1)+' / '+total+' 題';
  document.getElementById('score-live').textContent='得分 '+score;
  document.getElementById('progress-fill').style.width=(idx/total*100)+'%';
  const m=q.exam.match(/^(\d+年)/),subj=q.exam.replace(/.*[：:]\s*/,'').trim();
  document.getElementById('exam-tag').textContent=(m?m[1]+' · ':'')+subj;
  const kd=document.getElementById('kw-tags');kd.innerHTML='';
  q.groups.forEach(g=>{
    const grp=curGroups.find(x=>x.name===g)||{color:'#94a3b8'};
    const s=document.createElement('span');s.className='kw-tag';
    s.style.cssText='background:'+grp.color+'18;color:'+grp.color+';border:1px solid '+grp.color+'44';
    s.textContent=g;kd.appendChild(s);
  });
  q.groups.forEach(g=>{sTotal[g]=(sTotal[g]||0)+1});
  document.getElementById('question-text').textContent=q.question;
  const od=document.getElementById('options');od.innerHTML='';
  Object.keys(q.options).sort().forEach(k=>{
    const btn=document.createElement('button');btn.className='option-btn';
    btn.innerHTML='<span class="option-label">'+k+'</span><span>'+q.options[k]+'</span>';
    btn.onclick=()=>pick(k,q.answer,btn,od,q);od.appendChild(btn);
  });
  document.getElementById('feedback').style.display='none';
  document.getElementById('btn-next').style.display='none';
}
function pick(chosen,correct,btn,od,q){
  if(answered)return;answered=true;
  const ok=chosen===correct;
  if(ok)score++;
  else{
    q.groups.forEach(g=>{sWrong[g]=(sWrong[g]||0)+1});
    const wq=loadWQ();
    if(!wq[q.id])wq[q.id]={question:q.question,options:q.options,answer:q.answer,exam:q.exam,groups:q.groups,wrongCount:0,note:''};
    wq[q.id].wrongCount++;saveWQ(wq);
  }
  od.querySelectorAll('.option-btn').forEach(b=>{b.disabled=true;if(b.querySelector('.option-label').textContent===correct)b.classList.add(ok?'correct':'show-correct')});
  if(!ok)btn.classList.add('wrong');
  const fb=document.getElementById('feedback');fb.className='feedback '+(ok?'correct':'wrong');
  fb.textContent=ok?'✓ 答對了！':'✗ 答錯了，正確答案是 ('+correct+')';fb.style.display='block';
  document.getElementById('score-live').textContent='得分 '+score;
  const nx=document.getElementById('btn-next');nx.style.display='block';
  nx.textContent=idx+1<quizQ.length?'下一題 →':'查看結果';
}
function nextQuestion(){idx++;idx>=quizQ.length?showResult():renderQ()}
function showResult(){
  document.getElementById('quiz-overlay').style.display='none';
  const s=loadS();s.sessions=(s.sessions||0)+1;s.totalAnswered=(s.totalAnswered||0)+quizQ.length;s.totalCorrect=(s.totalCorrect||0)+score;
  Object.entries(sWrong).forEach(([g,w])=>{s.wrongByGroup[g]=(s.wrongByGroup[g]||0)+w});
  Object.entries(sTotal).forEach(([g,t])=>{s.totalByGroup[g]=(s.totalByGroup[g]||0)+t});
  saveS(s);updateStats();
  const total=quizQ.length,pct=Math.round(score/total*100);
  const circle=document.getElementById('score-circle');
  circle.style.background=pct>=80?'#22c55e':pct>=60?'#f59e0b':'#ef4444';
  document.getElementById('final-score').textContent=pct;
  document.getElementById('result-title').textContent=pct>=80?'表現優異！':pct>=60?'繼續加油！':'還需多練習';
  document.getElementById('result-detail').textContent='答對 '+score+' 題，共 '+total+' 題（正確率 '+pct+'%）';
  document.getElementById('result-overlay').style.background=curSubj.bg;
  document.getElementById('result-overlay').style.display='block';
  document.getElementById('btn-again').style.background=curSubj.color;
  drawRadar('session-radar',sWrong,sTotal,240);
  drawWeak('session-weak',sWrong,sTotal);
}
function restartSame(){document.getElementById('result-overlay').style.display='none';document.getElementById('filter-exam').value=lastF;document.getElementById('num-questions').value=lastN;startQuiz()}
function goHome(){document.getElementById('result-overlay').style.display='none';showPage('practice')}

// ── 錯題 ────────────────────────────────────────────────
let wrongGroupFilter='all';
function renderWrong(){
  const wq=loadWQ(),entries=Object.values(wq);
  document.getElementById('wrong-badge').textContent=entries.length+' 題';
  const fd=document.getElementById('wrong-filter');fd.innerHTML='';
  const groups=['all',...new Set(entries.flatMap(q=>q.groups))];
  groups.forEach(g=>{
    const chip=document.createElement('button');chip.className='filter-chip'+(g===wrongGroupFilter?' active':'');
    chip.textContent=g==='all'?'全部 ('+entries.length+')':g;
    if(g===wrongGroupFilter){chip.style.background=curSubj.color;chip.style.color='#fff'}
    chip.onclick=()=>{wrongGroupFilter=g;renderWrong()};fd.appendChild(chip);
  });
  const list=document.getElementById('wrong-list');list.innerHTML='';
  const filtered=wrongGroupFilter==='all'?entries:entries.filter(q=>q.groups.includes(wrongGroupFilter));
  if(!filtered.length){list.innerHTML='<div class="empty-msg">'+(entries.length?'這個分類沒有錯題 🎉':'還沒有錯題記錄<br>答錯的題目會自動收錄到這裡 📌')+'</div>';return}
  filtered.sort((a,b)=>b.wrongCount-a.wrongCount).forEach(q=>{
    const card=document.createElement('div');card.className='wq-card';
    const yr=q.exam.match(/^(\d+年)/),subj=q.exam.replace(/.*[：:]\s*/,'').trim();
    const tagsHtml=q.groups.map(g=>{const grp=curGroups.find(x=>x.name===g)||{color:'#94a3b8'};return'<span class="kw-tag" style="background:'+grp.color+'18;color:'+grp.color+';border:1px solid '+grp.color+'44">'+g+'</span>'}).join('');
    const optsHtml=Object.keys(q.options).sort().map(k=>'<div class="wq-option'+(k===q.answer?' is-answer':'')+'"><span class="wq-option-label">'+k+'</span><span>'+q.options[k]+'</span></div>').join('');
    const allWQ=loadWQ();const qid=Object.keys(allWQ).find(id=>allWQ[id]===q)||'';
    const hasNote=q.note&&q.note.trim();
    card.innerHTML='<div class="wq-meta"><span class="wq-exam">'+(yr?yr[1]+' · ':'')+subj+'</span><span class="wq-wrong-count">答錯 '+q.wrongCount+' 次</span></div>'
      +'<div class="wq-groups">'+tagsHtml+'</div>'
      +'<div class="wq-question">'+q.question+'</div>'
      +'<div class="wq-options">'+optsHtml+'</div>'
      +(hasNote?'<div class="wq-saved-note">📝 '+q.note+'</div>':'')
      +'<button class="wq-note-toggle" style="color:'+curSubj.color+'" onclick="toggleNote(this)">✏️ '+(hasNote?'編輯詳解':'新增詳解')+'</button>'
      +'<div class="wq-note-area"><textarea class="wq-textarea" style="border-color:#e0e0e0" placeholder="在這裡寫下筆記或詳解…">'+q.note+'</textarea>'
      +'<div class="wq-note-actions"><button class="wq-save-btn" style="background:'+curSubj.color+'" onclick="saveNote(this,\''+qid+'\')">儲存</button>'
      +'<button class="wq-del-btn" onclick="deleteWrong(\''+qid+'\')">移除錯題</button></div></div>';
    list.appendChild(card);
  });
}
function toggleNote(btn){btn.nextElementSibling.classList.toggle('open')}
function saveNote(btn,qid){const ta=btn.closest('.wq-note-area').querySelector('.wq-textarea');const wq=loadWQ();if(!wq[qid])return;wq[qid].note=ta.value;saveWQ(wq);btn.textContent='✓ 已儲存';setTimeout(()=>{btn.textContent='儲存';renderWrong()},800)}
function deleteWrong(qid){if(!confirm('確定移除？'))return;const wq=loadWQ();delete wq[qid];saveWQ(wq);renderWrong()}

// ── 分析 ────────────────────────────────────────────────
function renderAnalysis(){
  const s=loadS(),wrap=document.getElementById('analysis-content');wrap.innerHTML='';
  if(!s.totalAnswered){wrap.innerHTML='<div class="empty-msg">還沒有答題記錄<br>先去練習幾題，分析就會出現在這裡 🎯</div>';return}
  wrap.innerHTML='<div class="section-title">🕸️ 累計錯題率雷達圖</div>'
    +'<div class="section-sub">外圈=錯題率高 · 累計 '+s.totalAnswered+' 題（共 '+(s.sessions||1)+' 次）</div>'
    +'<div class="legend"><div class="legend-item"><div class="legend-dot" style="background:'+curSubj.color+';opacity:.6"></div>出題覆蓋</div>'
    +'<div class="legend-item"><div class="legend-dot" style="background:#ef4444"></div>錯題率</div></div>'
    +'<div class="radar-wrap"><svg class="radar" id="analysis-radar" viewBox="0 0 500 500" width="300" height="300"></svg></div>'
    +'<div id="analysis-weak" style="margin-top:14px"><div class="section-title" style="margin-bottom:8px">📋 各知識點錯題率排名</div></div>';
  setTimeout(()=>{drawRadar('analysis-radar',s.wrongByGroup,s.totalByGroup,280);drawWeak('analysis-weak',s.wrongByGroup,s.totalByGroup,true)},0);
}
function clearStats(){if(!confirm('清除「'+curSubj.name+'」的答題統計？\n（錯題本和詳解不受影響）'))return;localStorage.removeItem(curSubj.store);updateStats();renderAnalysis()}
function resetAll(){
  if(!confirm('確定清除「'+curSubj.name+'」的所有記錄？\n包含：作答統計、錯題本、所有詳解\n此操作無法復原！'))return;
  localStorage.removeItem(curSubj.store);localStorage.removeItem(curSubj.wstore);
  updateStats();alert('已清除「'+curSubj.name+'」所有資料');showPage('practice');
}

// ── 雷達圖 ──────────────────────────────────────────────
function drawRadar(id,wg,tg,R){
  const svg=document.getElementById(id);if(!svg)return;svg.innerHTML='';
  const cx=250,cy=250,groups=curGroups.filter(g=>tg[g.name]);
  if(groups.length<3){svg.style.display='none';return}
  svg.style.display='';
  const n=groups.length,step=(2*Math.PI)/n,sa=-Math.PI/2,ns='http://www.w3.org/2000/svg';
  function pt(i,r){const a=sa+i*step;return[cx+r*Math.cos(a),cy+r*Math.sin(a)]}
  function el(t,a,p){const e=document.createElementNS(ns,t);Object.entries(a).forEach(([k,v])=>e.setAttribute(k,v));if(p)p.appendChild(e);return e}
  [.2,.4,.6,.8,1].forEach(r=>el('circle',{cx,cy,r:R*r,class:'radar-grid'},svg));
  ['20%','40%','60%','80%','100%'].forEach((l,i)=>{const t=el('text',{x:cx+3,y:cy-R*(i+1)*.2+4,style:'font-size:9px;fill:#ccc;font-family:sans-serif'},svg);t.textContent=l});
  groups.forEach((_,i)=>{const[x,y]=pt(i,R);el('line',{x1:cx,y1:cy,x2:x,y2:y,class:'radar-axis'},svg)});
  const aa=el('polygon',{points:groups.map((_,i)=>pt(i,R).join(',')).join(' ')},svg);
  aa.style.fill=curSubj.color+'44';aa.style.stroke=curSubj.color;aa.style.strokeWidth='1.5';aa.style.strokeDasharray='4 3';aa.style.fillOpacity='.4';
  el('polygon',{points:groups.map((g,i)=>{const t=tg[g.name]||1,w=wg[g.name]||0;return pt(i,R*(w/t)).join(',')}).join(' '),class:'radar-area-wrong'},svg);
  groups.forEach((g,i)=>{
    const t=tg[g.name]||1,w=wg[g.name]||0,rate=w/t;
    if(w>0){const[x,y]=pt(i,R*rate);el('circle',{cx:x,cy:y,r:4,class:'radar-dot'},svg);const p=el('text',{x:x+5,y:y-5,class:'radar-pct'},svg);p.textContent=Math.round(rate*100)+'%'}
    const[lx,ly]=pt(i,R+22);const t2=el('text',{x:lx,y:ly,class:'radar-label','text-anchor':lx<cx-5?'end':lx>cx+5?'start':'middle','dominant-baseline':'middle'},svg);t2.textContent=g.name;
  });
}
function drawWeak(cid,wg,tg,append){
  const c=document.getElementById(cid);if(!c)return;
  const entries=Object.entries(wg).map(([g,w])=>({g,w,t:tg[g]||w,rate:w/(tg[g]||w)})).sort((a,b)=>b.rate-a.rate);
  if(!entries.length){const d=document.createElement('div');d.className='no-wrong';d.textContent='🎉 沒有錯誤記錄！';c.appendChild(d);return}
  entries.forEach(({g,w,t,rate})=>{
    const grp=curGroups.find(x=>x.name===g)||{color:'#94a3b8'},pct=Math.round(rate*100);
    const row=document.createElement('div');row.className='weak-item';row.style.background=grp.color+'10';
    row.innerHTML='<div class="weak-item-left"><div class="weak-dot" style="background:'+grp.color+'"></div><span class="weak-name">'+g+'</span></div>'
      +'<div class="weak-bar-wrap" style="background:'+grp.color+'18"><div class="weak-bar-fill" style="width:'+pct+'%;background:'+grp.color+'"></div></div>'
      +'<span class="weak-pct" style="color:'+grp.color+'">'+w+'/'+t+' ('+pct+'%)</span>';
    c.appendChild(row);
  });
}

// ── 啟動 ────────────────────────────────────────────────
initSubject(SUBJECTS[0].id);
</script>
</body>
</html>
"""

html = (html
    .replace('##SUBJECTS##', subjects_js)
    .replace('##GROUPS_MAP##', groups_map_js))

(BASE / "index.html").write_text(html, encoding="utf-8")
sys.stdout.buffer.write(f"index.html ({len(html)//1024} KB)\n".encode("utf-8"))
sys.stdout.flush()
print("完成！題庫合集資料夾內容：")
for f in sorted(BASE.iterdir()):
    print(f"  {f.name}  ({f.stat().st_size//1024} KB)")
