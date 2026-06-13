import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="WasteWise ♻️",
    page_icon="♻️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f9fafb;color:#1a1a1a;}
:root{--color-text-primary:#1a1a1a;--color-text-secondary:#6b7280;--color-text-tertiary:#9ca3af;--color-background-primary:#ffffff;--color-background-secondary:#f3f4f6;--color-border-tertiary:#e5e7eb;--color-border-secondary:#d1d5db;--border-radius-lg:12px;--border-radius-md:8px;}
.app{max-width:520px;margin:0 auto;background:#fff;min-height:100vh;border-left:1px solid #e5e7eb;border-right:1px solid #e5e7eb;}
.ww-header{padding:16px 16px 12px;border-bottom:.5px solid var(--color-border-tertiary);display:flex;align-items:center;gap:12px;position:sticky;top:0;background:#fff;z-index:10;}
.ww-logo{width:48px;height:48px;border-radius:50%;background:#EAF3DE;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0}
.ww-title{font-size:20px;font-weight:600;color:var(--color-text-primary);line-height:1.2}
.ww-sub{font-size:13px;color:var(--color-text-secondary);margin-top:2px}
.search-section{padding:12px 16px}
.search-box{display:flex;align-items:center;gap:10px;background:var(--color-background-secondary);border:.5px solid var(--color-border-secondary);border-radius:var(--border-radius-lg);padding:10px 14px}
.search-box i{font-size:20px;color:var(--color-text-tertiary);flex-shrink:0}
.search-box input{border:none;background:transparent;font-size:16px;color:var(--color-text-primary);flex:1;outline:none}
.search-box input::placeholder{color:var(--color-text-tertiary)}
.cat-section{padding:0 16px 12px}
.cat-label{font-size:11px;color:var(--color-text-tertiary);font-weight:600;letter-spacing:.06em;margin-bottom:8px}
.cat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.cat-btn{border:.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);background:#fff;padding:10px 6px;cursor:pointer;text-align:center;transition:all .15s}
.cat-btn.active{border-width:2px}
.cat-icon{font-size:26px;display:block;margin-bottom:4px}
.cat-name{font-size:12px;font-weight:600;line-height:1.3;color:var(--color-text-primary)}
.cat-hindi{font-size:11px;color:var(--color-text-secondary);margin-top:1px}
.sub-section{padding:0 16px 12px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(90px,1fr));gap:8px}
.sub-btn{border:.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-md);background:#fff;padding:8px 4px;cursor:pointer;text-align:center;transition:all .15s}
.sub-btn.active{border-width:2px}
.sub-icon{font-size:22px;display:block;margin-bottom:3px}
.sub-name{font-size:11px;font-weight:600;line-height:1.3;color:var(--color-text-primary)}
.sub-hindi{font-size:10px;color:var(--color-text-secondary);margin-top:1px}
.items-section{padding:0 16px 16px}
.items-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px}
.item-card{border:.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);background:#fff;padding:12px 8px;cursor:pointer;text-align:center;transition:border-color .15s}
.item-card:hover{border-color:var(--color-border-secondary)}
.item-icon{font-size:32px;display:block;margin-bottom:6px}
.item-name{font-size:13px;font-weight:600;color:var(--color-text-primary);line-height:1.3}
.item-hindi{font-size:11px;color:var(--color-text-secondary);margin-top:2px}
.item-bin{font-size:10px;font-weight:600;margin-top:6px;padding:3px 8px;border-radius:20px;display:inline-block}
.detail-wrap{padding:16px;background:#f3f4f6;min-height:400px}
.detail-card{background:#fff;border-radius:var(--border-radius-lg);border:.5px solid var(--color-border-tertiary);padding:16px}
.detail-top{display:flex;align-items:flex-start;gap:12px;margin-bottom:14px}
.detail-icon{font-size:48px;line-height:1}
.detail-close{margin-left:auto;background:none;border:1px solid var(--color-border-secondary);border-radius:var(--border-radius-md);cursor:pointer;color:var(--color-text-secondary);font-size:13px;padding:6px 10px;display:flex;align-items:center;gap:4px;flex-shrink:0}
.detail-close:hover{background:var(--color-background-secondary)}
.detail-name{font-size:18px;font-weight:600;color:var(--color-text-primary)}
.detail-hindi{font-size:15px;color:var(--color-text-secondary);margin-top:2px}
.bin-pill{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:13px;font-weight:600;margin-bottom:12px}
.steps-title{font-size:11px;font-weight:600;color:var(--color-text-tertiary);letter-spacing:.06em;margin-bottom:8px}
.step-row{display:flex;gap:10px;align-items:flex-start;margin-bottom:10px}
.step-num{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;flex-shrink:0}
.step-en{font-size:13px;color:var(--color-text-primary);line-height:1.5}
.step-hi{font-size:12px;color:var(--color-text-secondary);margin-top:2px;line-height:1.4}
.warn-row{display:flex;gap:8px;align-items:flex-start;padding:10px;border-radius:var(--border-radius-md);background:#FAECE7;margin-top:8px}
.warn-icon{font-size:18px;flex-shrink:0}
.warn-en{font-size:12px;color:#993C1D;line-height:1.5}
.warn-hi{font-size:11px;color:#993C1D;margin-top:2px}
.no-res{text-align:center;padding:40px 16px;color:var(--color-text-secondary);font-size:15px}
.ai-tab-bar{display:flex;gap:0;border-bottom:.5px solid var(--color-border-tertiary);padding:0 16px;position:sticky;top:80px;background:#fff;z-index:9;}
.ai-tab{flex:1;padding:10px 0;font-size:13px;font-weight:600;color:var(--color-text-secondary);border:none;background:none;cursor:pointer;border-bottom:2px solid transparent;transition:all .15s}
.ai-tab.active{color:#3B6D11;border-bottom-color:#3B6D11}
.tab-panel{display:none}
.tab-panel.active{display:block}
.ai-chat-wrap{display:flex;flex-direction:column;height:520px;}
.ai-messages{flex:1;overflow-y:auto;padding:12px 16px;display:flex;flex-direction:column;gap:10px;}
.msg{max-width:85%;padding:10px 13px;border-radius:var(--border-radius-lg);font-size:13px;line-height:1.6}
.msg.user{align-self:flex-end;background:#EAF3DE;color:#27500A;border-bottom-right-radius:4px}
.msg.bot{align-self:flex-start;background:var(--color-background-secondary);color:var(--color-text-primary);border-bottom-left-radius:4px}
.msg.bot .msg-label{font-size:10px;font-weight:600;color:#3B6D11;letter-spacing:.05em;margin-bottom:4px}
.typing{display:flex;gap:4px;align-items:center;padding:4px 0}
.typing span{width:6px;height:6px;border-radius:50%;background:#9ca3af;animation:blink 1.2s infinite}
.typing span:nth-child(2){animation-delay:.2s}
.typing span:nth-child(3){animation-delay:.4s}
@keyframes blink{0%,80%,100%{opacity:.3}40%{opacity:1}}
.ai-input-bar{padding:10px 16px;border-top:.5px solid var(--color-border-tertiary);display:flex;gap:8px;align-items:center;}
.ai-input-bar input{flex:1;border:.5px solid var(--color-border-secondary);border-radius:var(--border-radius-lg);padding:9px 13px;font-size:14px;outline:none;background:var(--color-background-secondary);color:var(--color-text-primary);}
.ai-input-bar input:focus{border-color:#3B6D11;background:#fff}
.ai-send-btn{width:38px;height:38px;border-radius:50%;background:#3B6D11;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:opacity .15s}
.ai-send-btn:disabled{opacity:.4;cursor:not-allowed}
.ai-send-btn i{color:#fff;font-size:18px}
.quick-chips{display:flex;flex-wrap:wrap;gap:6px;padding:8px 16px 4px}
.chip{font-size:11px;padding:5px 11px;border-radius:20px;border:.5px solid var(--color-border-secondary);background:#fff;cursor:pointer;color:var(--color-text-secondary);transition:all .15s}
.chip:hover{background:#EAF3DE;color:#27500A;border-color:#3B6D11}
</style>
</head>
<body>
<div class="app">

<div class="ww-header">
  <div class="ww-logo">♻</div>
  <div>
    <div class="ww-title">WasteWise <span style="font-size:14px;font-weight:400;color:#6b7280">/ वेस्टवाइज़</span></div>
    <div class="ww-sub">श्रेणी चुनें या AI से पूछें</div>
  </div>
</div>

<div class="ai-tab-bar">
  <button class="ai-tab active" onclick="switchTab('browse')">🗂 Browse / ब्राउज़</button>
  <button class="ai-tab" onclick="switchTab('ai')">✨ Ask AI / AI से पूछें</button>
</div>

<div id="tab-browse" class="tab-panel active">
  <div class="search-section">
    <div class="search-box">
      <i class="ti ti-search"></i>
      <input id="srch" type="text" placeholder="Search… jaise battery, onion, दवाई, newspaper" oninput="onSearch()">
      <button id="srch-clear" onclick="clearSearch()" style="background:none;border:none;cursor:pointer;display:none;padding:0">
        <i class="ti ti-x" style="font-size:18px;color:#9ca3af"></i>
      </button>
    </div>
  </div>
  <div id="main-view">
    <div class="cat-section">
      <div class="cat-label">CHOOSE A CATEGORY / श्रेणी चुनें</div>
      <div class="cat-grid" id="catGrid"></div>
    </div>
    <div id="subSection" style="display:none" class="sub-section">
      <div class="cat-label" id="subLabel">SELECT TYPE / प्रकार चुनें</div>
      <div class="sub-grid" id="subGrid"></div>
    </div>
    <div id="itemsSection" style="display:none" class="items-section">
      <div class="cat-label" id="itemsLabel">TAP AN ITEM / वस्तु चुनें</div>
      <div class="items-grid" id="itemsGrid"></div>
    </div>
  </div>
  <div id="search-view" style="display:none" class="items-section">
    <div class="cat-label">SEARCH RESULTS / खोज परिणाम</div>
    <div class="items-grid" id="searchGrid"></div>
    <div class="no-res" id="searchNone" style="display:none">
      <i class="ti ti-mood-sad" style="font-size:36px;display:block;margin-bottom:8px"></i>
      No results found<br><span style="font-size:13px">कोई परिणाम नहीं मिला</span>
    </div>
  </div>
  <div id="detailView" style="display:none">
    <div class="detail-wrap">
      <div class="detail-card" id="detailCard"></div>
    </div>
  </div>
</div>

<div id="tab-ai" class="tab-panel">
  <div class="ai-chat-wrap">
    <div class="ai-messages" id="aiMessages">
      <div class="msg bot">
        <div class="msg-label">WASTEWISE AI</div>
        नमस्ते! 👋 I'm your waste disposal assistant. Ask me anything about recycling, disposal, or waste management in India — in English or Hindi!
      </div>
    </div>
    <div class="quick-chips" id="quickChips">
      <span class="chip" onclick="askChip('How do I dispose of old medicines safely?')">💊 Old medicines</span>
      <span class="chip" onclick="askChip('Where to drop e-waste in India?')">💻 E-waste drop</span>
      <span class="chip" onclick="askChip('Can I compost onion peels at home?')">🧅 Composting</span>
      <span class="chip" onclick="askChip('What is the green bin for?')">🟢 Green bin</span>
      <span class="chip" onclick="askChip('How to dispose used cooking oil?')">🍳 Cooking oil</span>
    </div>
    <div class="ai-input-bar">
      <input id="aiInput" type="text" placeholder="Ask about any waste item… कुछ भी पूछें" onkeydown="if(event.key==='Enter')sendAI()"/>
      <button class="ai-send-btn" id="aiSendBtn" onclick="sendAI()">
        <i class="ti ti-send"></i>
      </button>
    </div>
  </div>
</div>

</div>

<script>
const CATS=[
  {id:'kitchen',icon:'🍳',name:'Kitchen',hindi:'रसोई',color:'#3B6D11',bg:'#EAF3DE'},
  {id:'ewaste',icon:'💻',name:'Electronic',hindi:'इलेक्ट्रॉनिक',color:'#185FA5',bg:'#E6F1FB'},
  {id:'bathroom',icon:'🚿',name:'Bathroom & Sanitary',hindi:'बाथरूम / सफाई',color:'#534AB7',bg:'#EEEDFE'},
  {id:'clothes',icon:'👕',name:'Clothes & Fabric',hindi:'कपड़े',color:'#854F0B',bg:'#FAEEDA'},
  {id:'books',icon:'📚',name:'Books & Stationery',hindi:'किताबें / स्टेशनरी',color:'#0F6E56',bg:'#E1F5EE'},
  {id:'medicine',icon:'💊',name:'Medicines',hindi:'दवाइयाँ',color:'#993C1D',bg:'#FAECE7'},
];

const SUBS={
  kitchen:[
    {id:'k-veg',icon:'🥦',name:'Vegetable & Fruit Waste',hindi:'सब्जी / फल कचरा'},
    {id:'k-oil',icon:'🫙',name:'Used Oil & Liquids',hindi:'तेल / तरल पदार्थ'},
    {id:'k-plastic',icon:'🥤',name:'Food Packaging',hindi:'खाद्य पैकेजिंग'},
    {id:'k-glass',icon:'🍶',name:'Glass Bottles & Jars',hindi:'कांच की बोतलें'},
    {id:'k-metal',icon:'🥫',name:'Tins & Metal Cans',hindi:'टिन / धातु के डब्बे'},
    {id:'k-food',icon:'🍛',name:'Leftover Food',hindi:'बचा हुआ खाना'},
  ],
  ewaste:[
    {id:'e-phone',icon:'📱',name:'Phones & Tablets',hindi:'मोबाइल / टैबलेट'},
    {id:'e-battery',icon:'🔋',name:'Batteries',hindi:'बैटरी'},
    {id:'e-bulb',icon:'💡',name:'Bulbs & Tubes',hindi:'बल्ब / ट्यूब लाइट'},
    {id:'e-cable',icon:'🔌',name:'Wires & Chargers',hindi:'तार / चार्जर'},
    {id:'e-tv',icon:'📺',name:'TV & Appliances',hindi:'टीवी / उपकरण'},
    {id:'e-comp',icon:'🖥️',name:'Computers & Laptops',hindi:'कंप्यूटर / लैपटॉप'},
  ],
  bathroom:[
    {id:'b-plastic',icon:'🧴',name:'Shampoo & Soap Bottles',hindi:'शैंपू / साबुन की बोतलें'},
    {id:'b-razor',icon:'🪒',name:'Razors & Blades',hindi:'रेज़र / ब्लेड'},
    {id:'b-sanitary',icon:'🩹',name:'Sanitary Pads & Diapers',hindi:'सैनिटरी पैड / डायपर'},
    {id:'b-cotton',icon:'🧻',name:'Cotton & Tissue',hindi:'रूई / टिश्यू'},
    {id:'b-toothbrush',icon:'🪥',name:'Toothbrush & Toothpaste Tube',hindi:'टूथब्रश / टूथपेस्ट ट्यूब'},
    {id:'b-aerosol',icon:'💨',name:'Aerosol Cans',hindi:'एरोसोल कैन'},
  ],
  clothes:[
    {id:'c-old',icon:'👗',name:'Old Wearable Clothes',hindi:'पुराने पहनने योग्य कपड़े'},
    {id:'c-torn',icon:'🧣',name:'Torn / Unusable Fabric',hindi:'फटे / बेकार कपड़े'},
    {id:'c-shoes',icon:'👟',name:'Old Shoes & Chappals',hindi:'पुराने जूते / चप्पल'},
    {id:'c-blanket',icon:'🛏️',name:'Blankets & Bedsheets',hindi:'कम्बल / चादरें'},
  ],
  books:[
    {id:'s-paper',icon:'📰',name:'Newspaper & Paper',hindi:'अखबार / कागज'},
    {id:'s-book',icon:'📖',name:'Old Books & Notebooks',hindi:'पुरानी किताबें / कॉपियाँ'},
    {id:'s-pen',icon:'🖊️',name:'Pens & Markers',hindi:'पेन / मार्कर'},
    {id:'s-cardboard',icon:'📦',name:'Cardboard & Boxes',hindi:'गत्ता / डिब्बे'},
    {id:'s-tape',icon:'🖇️',name:'Tapes & Staples',hindi:'टेप / स्टेपल'},
  ],
  medicine:[
    {id:'m-tablet',icon:'💊',name:'Expired Tablets & Capsules',hindi:'एक्सपायर्ड गोलियाँ'},
    {id:'m-syrup',icon:'🧪',name:'Liquid Medicine & Syrup',hindi:'सिरप / तरल दवाई'},
    {id:'m-syringe',icon:'💉',name:'Syringes & Lancets',hindi:'सिरिंज / लैंसेट'},
    {id:'m-strip',icon:'🩻',name:'Medicine Strips & Blister Packs',hindi:'दवाई की पट्टी'},
    {id:'m-bandage',icon:'🩹',name:'Used Bandages & Cotton',hindi:'इस्तेमाल की पट्टी / रूई'},
    {id:'m-bottle',icon:'🫙',name:'Empty Medicine Bottles',hindi:'खाली दवाई की बोतलें'},
  ],
};

const ITEMS={
  'k-veg':[
    {icon:'🧅',name:'Onion & Garlic Peels',hindi:'प्याज / लहसुन के छिलके',bin:'Green Bin',binColor:'#3B6D11',binBg:'#EAF3DE',steps:[{en:'Collect in a small container near sink.',hi:'सिंक के पास छोटे डब्बे में इकट्ठा करें।'},{en:'Put in green/wet waste bin daily.',hi:'रोज हरी/गीली कचरा बिन में डालें।'},{en:'Can be composted at home in a mud pit.',hi:'मिट्टी के गड्ढे में घर पर खाद बना सकते हैं।'}],warn:'Never mix with plastic bags.',warnHi:'प्लास्टिक बैग के साथ कभी न मिलाएं।'},
    {icon:'🍌',name:'Banana & Fruit Peels',hindi:'केला / फल के छिलके',bin:'Green Bin',binColor:'#3B6D11',binBg:'#EAF3DE',steps:[{en:'Toss directly into green/wet waste bin.',hi:'सीधे हरी/गीली कचरा बिन में डालें।'},{en:'Can be used as garden fertilizer.',hi:'बगीचे की खाद के रूप में उपयोग करें।'}],warn:null,warnHi:null},
    {icon:'🥬',name:'Vegetable Scraps',hindi:'सब्जी के टुकड़े',bin:'Green Bin',binColor:'#3B6D11',binBg:'#EAF3DE',steps:[{en:'Collect in green bin — do not store for too long to avoid odor.',hi:'हरी बिन में रखें — बदबू से बचने के लिए ज्यादा देर न रखें।'},{en:'Municipal trucks collect for composting or biogas.',hi:'नगर निगम के ट्रक खाद/बायोगैस के लिए ले जाते हैं।'}],warn:null,warnHi:null},
  ],
  'k-oil':[
    {icon:'🍳',name:'Used Cooking Oil',hindi:'इस्तेमाल किया खाना पकाने का तेल',bin:'Special Collection',binColor:'#854F0B',binBg:'#FAEEDA',steps:[{en:'Let oil cool completely.',hi:'तेल को पूरी तरह ठंडा होने दें।'},{en:'Pour into a sealed bottle — never pour down drain.',hi:'सीलबंद बोतल में डालें — नाली में कभी न बहाएं।'},{en:'Give to municipal cooking oil collection or biodiesel vendor.',hi:'नगर निगम के संग्रह अभियान या बायोडीजल विक्रेता को दें।'}],warn:'Draining oil clogs pipes and pollutes groundwater.',warnHi:'नाली में तेल डालने से पाइप बंद होते हैं और पानी प्रदूषित होता है।'},
  ],
  'k-plastic':[
    {icon:'🥤',name:'Plastic Bottles & Containers',hindi:'प्लास्टिक बोतलें / डब्बे',bin:'Blue Bin (Dry)',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Rinse thoroughly to remove food.',hi:'खाना हटाने के लिए अच्छे से धोएं।'},{en:'Crush/flatten to save space.',hi:'जगह बचाने के लिए चपटा करें।'},{en:'Put in blue/dry waste bin.',hi:'नीली/सूखी कचरा बिन में डालें।'}],warn:'Multi-layer pouches (chips/gutka) cannot be recycled — red bin.',warnHi:'मल्टी-लेयर पाउच (चिप्स/गुटखा) रीसाइकिल नहीं होते — लाल बिन।'},
    {icon:'🛍️',name:'Plastic Carry Bags',hindi:'प्लास्टिक थैलियाँ',bin:'Designated Drop Point',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Bundle together and take to plastic collection point.',hi:'एक साथ बांधकर प्लास्टिक संग्रह केंद्र पर ले जाएं।'},{en:'Many grocery stores accept old carry bags.',hi:'कई किराना दुकानें पुराने थैले वापस लेती हैं।'}],warn:'Never burn plastic bags — releases toxic fumes.',warnHi:'प्लास्टिक की थैलियाँ कभी न जलाएं — जहरीला धुआं निकलता है।'},
  ],
  'k-glass':[
    {icon:'🍶',name:'Glass Bottles & Jars',hindi:'कांच की बोतलें / जार',bin:'Blue Bin / Kabadiwala',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Rinse clean and remove lids.',hi:'साफ धोएं और ढक्कन हटाएं।'},{en:'Wrap cracked/broken glass in newspaper before binning.',hi:'टूटे कांच को अखबार में लपेटकर बिन में डालें।'},{en:'Sell whole bottles to local kabadiwala — best recycling outcome.',hi:'साबुत बोतलें स्थानीय कबाड़ीवाले को बेचें।'}],warn:'Never throw broken glass loose in bin — causes injury.',warnHi:'टूटा कांच बिन में खुला न डालें — चोट लग सकती है।'},
  ],
  'k-metal':[
    {icon:'🥫',name:'Tins & Metal Cans',hindi:'टिन / धातु के डब्बे',bin:'Blue Bin / Kabadiwala',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Rinse and dry the can.',hi:'कैन को धोकर सुखाएं।'},{en:'Crush flat if possible.',hi:'यदि संभव हो तो चपटा करें।'},{en:'Blue bin or sell to kabadiwala.',hi:'नीली बिन में डालें या कबाड़ीवाले को बेचें।'}],warn:null,warnHi:null},
  ],
  'k-food':[
    {icon:'🍛',name:'Leftover Cooked Food',hindi:'बचा हुआ पका खाना',bin:'Green Bin',binColor:'#3B6D11',binBg:'#EAF3DE',steps:[{en:'First try to donate edible food to neighbours or food banks.',hi:'पहले खाने योग्य भोजन पड़ोसियों को दें।'},{en:'If spoiled, wrap and put in green/wet bin.',hi:'अगर खराब हो गया है, लपेटकर हरी/गीली बिन में डालें।'},{en:'Can be used in home compost.',hi:'घरेलू खाद में उपयोग करें।'}],warn:'Never pour gravy/liquid food down the drain — blocks pipes.',warnHi:'तरल खाना नाली में न बहाएं — पाइप जाम होते हैं।'},
  ],
  'e-phone':[
    {icon:'📱',name:'Old Mobile Phone',hindi:'पुराना मोबाइल फोन',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Do factory reset — delete all personal data.',hi:'फैक्ट्री रीसेट करें — सभी डेटा मिटाएं।'},{en:'Remove SIM and memory card.',hi:'SIM और मेमोरी कार्ड निकालें।'},{en:'Take to authorized e-waste centre or brand take-back programme.',hi:'अधिकृत ई-वेस्ट केंद्र या ब्रांड टेक-बैक कार्यक्रम में दें।'}],warn:'Never throw phone in regular bin or burn — toxic fumes.',warnHi:'फोन को सामान्य बिन में न डालें और न जलाएं — जहरीला धुआं।'},
    {icon:'💻',name:'Old Laptop / Tablet',hindi:'पुराना लैपटॉप / टैबलेट',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Backup and wipe data completely.',hi:'डेटा बैकअप करें और पूरी तरह मिटाएं।'},{en:'Take to authorized e-waste recycler.',hi:'अधिकृत ई-वेस्ट रीसाइकलर को दें।'},{en:'Many brands (Dell, HP, Apple) have take-back schemes.',hi:'कई ब्रांड (Dell, HP, Apple) टेक-बैक योजनाएं देते हैं।'}],warn:null,warnHi:null},
  ],
  'e-battery':[
    {icon:'🔋',name:'AA / AAA Batteries',hindi:'AA / AAA बैटरी',bin:'Hazardous Bin / E-Waste',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Never throw in regular trash or burn.',hi:'सामान्य कचरे में न फेंकें और न जलाएं।'},{en:'Store in a dry box separately.',hi:'अलग सूखे डब्बे में रखें।'},{en:'Drop at e-waste collection point or electronics store.',hi:'ई-वेस्ट केंद्र या इलेक्ट्रॉनिक्स दुकान पर जमा करें।'}],warn:'Batteries contain lead & mercury — poison for soil and water.',warnHi:'बैटरी में सीसा और पारा होता है — मिट्टी और पानी के लिए ज़हर।'},
  ],
  'e-bulb':[
    {icon:'💡',name:'CFL / Tube Light',hindi:'CFL / ट्यूब लाइट',bin:'Hazardous E-Waste',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Handle carefully — contains mercury vapour.',hi:'सावधानी से संभालें — इसमें पारा वाष्प होती है।'},{en:'Wrap in newspaper before disposal.',hi:'निपटान से पहले अखबार में लपेटें।'},{en:'Take to e-waste or hazardous waste centre — not regular bin.',hi:'ई-वेस्ट या खतरनाक अपशिष्ट केंद्र पर ले जाएं।'}],warn:'If broken: ventilate room, sweep gently into sealed bag.',warnHi:'अगर टूटे: कमरे को हवादार करें, धीरे से सीलबंद बैग में झाड़ें।'},
    {icon:'💡',name:'LED Bulb',hindi:'LED बल्ब',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'LEDs have no mercury but still contain electronics.',hi:'LED में पारा नहीं होता लेकिन इलेक्ट्रॉनिक्स होते हैं।'},{en:'Take to e-waste collection centre.',hi:'ई-वेस्ट संग्रह केंद्र पर ले जाएं।'}],warn:null,warnHi:null},
  ],
  'e-cable':[
    {icon:'🔌',name:'Old Chargers & Cables',hindi:'पुराने चार्जर / तार',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Bundle cables together neatly.',hi:'तारों को साफ-सुथरा बांधें।'},{en:'Take to e-waste centre or electronics store.',hi:'ई-वेस्ट केंद्र या इलेक्ट्रॉनिक्स दुकान पर दें।'},{en:'Metal inside wires is valuable — do not burn to extract it.',hi:'तारों के अंदर धातु कीमती होती है — निकालने के लिए न जलाएं।'}],warn:'Never burn wires — releases highly toxic fumes.',warnHi:'तार कभी न जलाएं — अत्यंत जहरीला धुआं निकलता है।'},
  ],
  'e-tv':[
    {icon:'📺',name:'Old TV / Refrigerator',hindi:'पुराना TV / फ्रिज',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Contact authorized e-waste recycler for pickup.',hi:'पिकअप के लिए अधिकृत ई-वेस्ट रीसाइकलर से संपर्क करें।'},{en:'Many dealers offer exchange offers — take advantage.',hi:'कई डीलर एक्सचेंज ऑफर देते हैं — इसका उपयोग करें।'},{en:'Do not leave on roadside — causes soil contamination.',hi:'सड़क किनारे न छोड़ें — मिट्टी प्रदूषण होता है।'}],warn:'CRT TVs contain lead glass — must go through certified recycler.',warnHi:'CRT TV में सीसे का कांच होता है — प्रमाणित रीसाइकलर को ही दें।'},
  ],
  'e-comp':[
    {icon:'🖥️',name:'Old Computer / Monitor',hindi:'पुराना कंप्यूटर / मॉनिटर',bin:'E-Waste Centre',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Wipe hard drive data — use disk wiping software.',hi:'हार्ड ड्राइव का डेटा मिटाएं — डिस्क वाइपिंग सॉफ्टवेयर उपयोग करें।'},{en:'Donate to schools/NGOs if still working.',hi:'यदि काम कर रहा हो तो स्कूलों/NGO को दान करें।'},{en:'Take to authorized e-waste centre.',hi:'अधिकृत ई-वेस्ट केंद्र पर ले जाएं।'}],warn:null,warnHi:null},
  ],
  'b-plastic':[
    {icon:'🧴',name:'Shampoo & Soap Bottles',hindi:'शैंपू / साबुन की बोतलें',bin:'Blue Bin (Dry)',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Squeeze out all remaining product.',hi:'बची हुई सभी सामग्री निचोड़ लें।'},{en:'Rinse with water 2–3 times.',hi:'2–3 बार पानी से धोएं।'},{en:'Put in blue/dry recyclable bin.',hi:'नीली/सूखी रीसाइकिल बिन में डालें।'}],warn:null,warnHi:null},
  ],
  'b-razor':[
    {icon:'🪒',name:'Used Razors & Blades',hindi:'इस्तेमाल किए रेज़र / ब्लेड',bin:'Sharps — Sealed Disposal',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Never throw loose blade in bin — causes injury.',hi:'बिन में खुला ब्लेड कभी न डालें — चोट लग सकती है।'},{en:'Place in a thick plastic bottle or small metal tin with lid.',hi:'ढक्कन वाली मोटी प्लास्टिक बोतल या छोटे धातु के डब्बे में रखें।'},{en:'Seal tightly and label "sharp waste" before binning.',hi:'कसकर सील करें और "नुकीला कचरा" लिखकर बिन में डालें।'}],warn:'Loose blades are a safety hazard for waste collectors.',warnHi:'खुले ब्लेड कचरा उठाने वालों के लिए खतरनाक होते हैं।'},
  ],
  'b-sanitary':[
    {icon:'🩹',name:'Sanitary Pads',hindi:'सैनिटरी पैड',bin:'Red Bag / Sealed Trash',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Wrap used pad in its own wrapper or newspaper.',hi:'इस्तेमाल के बाद पैड को उसके रैपर या अखबार में लपेटें।'},{en:'Put in a sealed red/sanitary bag — not open bin.',hi:'सीलबंद लाल/सेनेटरी बैग में डालें — खुली बिन में नहीं।'},{en:'Many areas have special sanitary waste pickup — check with municipality.',hi:'कई इलाकों में सैनिटरी कचरा विशेष पिकअप होता है।'}],warn:'Never flush pads — blocks sewage pipes severely.',warnHi:'पैड कभी flush न करें — सीवर पाइप बंद हो जाते हैं।'},
    {icon:'👶',name:'Used Diapers',hindi:'इस्तेमाल किए डायपर',bin:'Red Bag / Sealed Trash',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Fold and seal inside its sticky tabs.',hi:'चिपकने वाले टैब से मोड़कर सील करें।'},{en:'Place in a red/sealed bag.',hi:'लाल/सीलबंद थैले में डालें।'},{en:'Dispose in solid waste bin daily — do not store.',hi:'रोज ठोस कचरा बिन में डालें — जमा न करें।'}],warn:'Diapers take 500+ years to decompose — consider cloth diapers.',warnHi:'डायपर को सड़ने में 500+ साल लगते हैं — कपड़े के डायपर उपयोग करें।'},
  ],
  'b-cotton':[
    {icon:'🧻',name:'Tissue Paper & Cotton',hindi:'टिश्यू / रूई',bin:'Green Bin (Wet Waste)',binColor:'#3B6D11',binBg:'#EAF3DE',steps:[{en:'Used tissue and plain cotton go in green/wet bin.',hi:'इस्तेमाल टिश्यू और सादी रूई हरी/गीली बिन में जाती है।'},{en:'Blood-stained cotton/tissue → red/biomedical bag.',hi:'खून लगी रूई/टिश्यू → लाल/जैव-चिकित्सा बैग।'}],warn:'Never flush cotton down toilet — blocks drain.',warnHi:'रूई को toilet में कभी flush न करें — नाली बंद होती है।'},
  ],
  'b-toothbrush':[
    {icon:'🪥',name:'Old Toothbrush',hindi:'पुराना टूथब्रश',bin:'Dry Bin / Repurpose',binColor:'#534AB7',binBg:'#EEEDFE',steps:[{en:'Old toothbrushes make great cleaning tools — repurpose before discarding.',hi:'पुराने टूथब्रश सफाई के काम आते हैं — फेंकने से पहले उपयोग करें।'},{en:'Plastic body goes in dry/blue bin.',hi:'प्लास्टिक बॉडी सूखी/नीली बिन में जाती है।'}],warn:null,warnHi:null},
    {icon:'🪥',name:'Toothpaste Tube',hindi:'टूथपेस्ट ट्यूब',bin:'Dry Bin',binColor:'#534AB7',binBg:'#EEEDFE',steps:[{en:'Cut open tube to use every last bit.',hi:'हर आखिरी बचा हिस्सा इस्तेमाल करने के लिए ट्यूब काटें।'},{en:'Rinse and put in dry/blue waste bin.',hi:'धोकर सूखी/नीली कचरा बिन में डालें।'}],warn:'Multi-layer tubes are not easily recyclable in most Indian cities.',warnHi:'ज्यादातर भारतीय शहरों में मल्टी-लेयर ट्यूब आसानी से रीसाइकिल नहीं होती।'},
  ],
  'b-aerosol':[
    {icon:'💨',name:'Aerosol Spray Cans',hindi:'एरोसोल स्प्रे कैन',bin:'Hazardous — Dry Bin',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Never puncture or crush aerosol cans — risk of explosion.',hi:'एरोसोल कैन को कभी न पंक्चर करें और न कुचलें — विस्फोट का खतरा।'},{en:'Ensure can is fully empty before disposal.',hi:'डिस्पोज़ करने से पहले कैन पूरी तरह खाली करें।'},{en:'Place in dry waste bin away from heat sources.',hi:'गर्मी के स्रोतों से दूर सूखी कचरा बिन में रखें।'}],warn:'Never throw aerosol cans into fire — they can explode.',warnHi:'एरोसोल कैन को आग में कभी न फेंकें — विस्फोट हो सकता है।'},
  ],
  'c-old':[
    {icon:'👗',name:'Old Wearable Clothes',hindi:'पुराने पहनने योग्य कपड़े',bin:'Donate / Cloth Bank',binColor:'#854F0B',binBg:'#FAEEDA',steps:[{en:'Wash and fold before donating.',hi:'दान करने से पहले धोएं और तह करें।'},{en:'Donate to NGOs, Goonj, local cloth banks, or temples.',hi:'NGO, गूंज, स्थानीय कपड़ा बैंक, या मंदिरों को दान करें।'},{en:'Many cities have donation bins in malls and RWAs.',hi:'कई शहरों में मॉल और RWA में दान बिन होते हैं।'}],warn:null,warnHi:null},
  ],
  'c-torn':[
    {icon:'🧶',name:'Torn / Worn-out Fabric',hindi:'फटे / घिसे हुए कपड़े',bin:'Rag Use / Dry Bin',binColor:'#854F0B',binBg:'#FAEEDA',steps:[{en:'Cut into rags for household cleaning before discarding.',hi:'फेंकने से पहले घरेलू सफाई के लिए टुकड़ों में काटें।'},{en:'Textile recyclers and NGOs (Goonj) accept torn fabric too.',hi:'कपड़ा रीसाइकलर और NGO (गूंज) फटे कपड़े भी लेते हैं।'},{en:'Remaining fabric goes in dry/blue waste bin.',hi:'बचे हुए कपड़े सूखी/नीली कचरा बिन में।'}],warn:'Do not mix with wet/food waste — ruins recyclability.',warnHi:'गीले/खाने के कचरे के साथ न मिलाएं — रीसाइक्लिंग खराब होती है।'},
  ],
  'c-shoes':[
    {icon:'👟',name:'Old Shoes & Chappals',hindi:'पुराने जूते / चप्पल',bin:'Donate / Dry Bin',binColor:'#854F0B',binBg:'#FAEEDA',steps:[{en:'Donate if still usable — Goonj and NGOs accept footwear.',hi:'अगर अभी भी उपयोगी हो तो दान करें — गूंज और NGO स्वीकार करते हैं।'},{en:'Rubber soles can be repaired by local cobblers — extend life.',hi:'रबर तले स्थानीय मोची से ठीक कराएं — उपयोग बढ़ाएं।'},{en:'Worn out shoes go in dry waste bin.',hi:'बहुत घिसे जूते सूखी कचरा बिन में डालें।'}],warn:null,warnHi:null},
  ],
  'c-blanket':[
    {icon:'🛏️',name:'Old Blankets & Bedsheets',hindi:'पुराने कम्बल / चादरें',bin:'Donate',binColor:'#854F0B',binBg:'#FAEEDA',steps:[{en:'Wash before donating.',hi:'दान करने से पहले धोएं।'},{en:'NGOs, shelter homes, and temples accept blankets especially in winter.',hi:'NGO, आश्रय गृह, और मंदिर विशेषकर सर्दियों में कम्बल स्वीकार करते हैं।'},{en:'Cut worn blankets into floor mats or cleaning rags.',hi:'पुराने कम्बलों को फर्श की चटाई या सफाई के लिए काटें।'}],warn:null,warnHi:null},
  ],
  's-paper':[
    {icon:'📰',name:'Newspaper & Magazines',hindi:'अखबार / पत्रिकाएं',bin:'Blue Bin / Kabadiwala',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Bundle neatly with string.',hi:'रस्सी से साफ-सुथरा बांधें।'},{en:'Keep dry — wet paper cannot be recycled.',hi:'सूखा रखें — गीला कागज रीसाइकिल नहीं होता।'},{en:'Sell to kabadiwala — best recycling outcome.',hi:'कबाड़ीवाले को बेचें — सबसे अच्छा रीसाइक्लिंग परिणाम।'}],warn:null,warnHi:null},
  ],
  's-book':[
    {icon:'📚',name:'Old Textbooks & Notebooks',hindi:'पुरानी किताबें / कॉपियाँ',bin:'Donate / Kabadiwala',binColor:'#0F6E56',binBg:'#E1F5EE',steps:[{en:'Donate usable books to schools, libraries, or NGOs.',hi:'उपयोगी किताबें स्कूलों, पुस्तकालयों, या NGO को दान करें।'},{en:'Remove plastic covers before recycling.',hi:'रीसाइक्लिंग से पहले प्लास्टिक कवर हटाएं।'},{en:'Sell paper waste to kabadiwala.',hi:'कागज का कचरा कबाड़ीवाले को बेचें।'}],warn:null,warnHi:null},
  ],
  's-pen':[
    {icon:'🖊️',name:'Used Pens & Markers',hindi:'इस्तेमाल किए पेन / मार्कर',bin:'Dry Bin / Terracycle',binColor:'#534AB7',binBg:'#EEEDFE',steps:[{en:'Try refilling cartridge before discarding.',hi:'फेंकने से पहले कार्ट्रिज रिफिल करने की कोशिश करें।'},{en:'Pen bodies (plastic) go in dry/blue bin.',hi:'पेन की बॉडी (प्लास्टिक) सूखी/नीली बिन में।'},{en:'Look for Terracycle pen recycling drives in your city.',hi:'अपने शहर में टेरासाइकिल पेन रीसाइक्लिंग अभियान खोजें।'}],warn:null,warnHi:null},
  ],
  's-cardboard':[
    {icon:'📦',name:'Cardboard Boxes',hindi:'गत्ते के डिब्बे',bin:'Blue Bin / Kabadiwala',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Flatten completely before disposal.',hi:'डिस्पोज़ करने से पहले पूरी तरह चपटा करें।'},{en:'Remove tape and staples.',hi:'टेप और स्टेपल हटाएं।'},{en:'Sell to kabadiwala or put in blue/dry bin.',hi:'कबाड़ीवाले को बेचें या नीली/सूखी बिन में डालें।'}],warn:'Wet or food-stained cardboard is not recyclable.',warnHi:'गीला या खाने से सना गत्ता रीसाइकिल नहीं होता।'},
  ],
  's-tape':[
    {icon:'🖇️',name:'Tape, Staples & Rubber Bands',hindi:'टेप / स्टेपल / रबर बैंड',bin:'Dry Bin',binColor:'#534AB7',binBg:'#EEEDFE',steps:[{en:'These small items go in dry/blue waste bin.',hi:'ये छोटी वस्तुएं सूखी/नीली कचरा बिन में जाती हैं।'},{en:'Remove tape from paper/cardboard before recycling those.',hi:'कागज/गत्ता रीसाइकिल करने से पहले टेप हटाएं।'}],warn:null,warnHi:null},
  ],
  'm-tablet':[
    {icon:'💊',name:'Expired Tablets & Capsules',hindi:'एक्सपायर्ड गोलियाँ / कैप्सूल',bin:'Pharmacy Return',binColor:'#993C1D',binBg:'#FAECE7',steps:[{en:'Do NOT flush down toilet or throw in regular bin.',hi:'टॉयलेट में flush न करें और सामान्य बिन में न डालें।'},{en:'Keep in original sealed packaging.',hi:'मूल सीलबंद पैकेजिंग में रखें।'},{en:'Return to any pharmacy — many have take-back schemes.',hi:'किसी भी फार्मेसी को वापस करें — कई दवा वापसी योजनाएं हैं।'}],warn:'Flushing antibiotics causes antimicrobial resistance in water.',warnHi:'एंटीबायोटिक flush करने से पानी में रोगाणुरोधी प्रतिरोध होता है।'},
  ],
  'm-syrup':[
    {icon:'🧪',name:'Expired Syrups & Liquids',hindi:'एक्सपायर्ड सिरप / तरल दवाई',bin:'Pharmacy Return',binColor:'#993C1D',binBg:'#FAECE7',steps:[{en:'Never pour liquid medicine down drain or toilet.',hi:'तरल दवाई नाली या टॉयलेट में कभी न बहाएं।'},{en:'Seal bottle tightly and return to pharmacy.',hi:'बोतल कसकर बंद करें और फार्मेसी को वापस करें।'},{en:'If unavoidable: mix with salt/dirt in sealed container then bin.',hi:'मजबूरी हो तो: नमक/मिट्टी मिलाकर सीलबंद डब्बे में बिन में डालें।'}],warn:'Medicine in water harms fish and enters our drinking water.',warnHi:'पानी में दवाई मछलियों को नुकसान पहुंचाती है और पीने के पानी में आती है।'},
  ],
  'm-syringe':[
    {icon:'💉',name:'Used Syringes & Lancets',hindi:'इस्तेमाल की सिरिंज / लैंसेट',bin:'Sharps Container — Hospital',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Cap needle immediately after use.',hi:'उपयोग के तुरंत बाद सुई ढकें।'},{en:'Put in puncture-proof container (thick plastic bottle with lid).',hi:'छेद-रोधी कंटेनर (ढक्कन वाली मोटी प्लास्टिक बोतल) में रखें।'},{en:'Return full container to nearest hospital or health centre.',hi:'भरा कंटेनर निकटतम अस्पताल या स्वास्थ्य केंद्र पर जमा करें।'}],warn:'Never throw loose needles — causes needle-stick injury.',warnHi:'खुली सुइयाँ कभी न फेंकें — सुई की चोट हो सकती है।'},
  ],
  'm-strip':[
    {icon:'🩻',name:'Medicine Strips & Blister Packs',hindi:'दवाई की पट्टी / ब्लिस्टर पैक',bin:'Dry Bin',binColor:'#534AB7',binBg:'#EEEDFE',steps:[{en:'Empty strips (foil+plastic) go in dry/blue waste bin.',hi:'खाली पट्टियाँ (फॉयल+प्लास्टिक) सूखी/नीली बिन में।'},{en:'Strips with unused tablets — return to pharmacy.',hi:'बचे हुए टैबलेट वाली पट्टियाँ — फार्मेसी को वापस करें।'}],warn:null,warnHi:null},
  ],
  'm-bandage':[
    {icon:'🩹',name:'Used Bandages & Dressings',hindi:'इस्तेमाल की पट्टी / ड्रेसिंग',bin:'Red Bag — Biomedical',binColor:'#A32D2D',binBg:'#FCEBEB',steps:[{en:'Place in red biomedical waste bag — not regular trash.',hi:'लाल जैव-चिकित्सा अपशिष्ट बैग में — सामान्य कचरे में नहीं।'},{en:'Seal bag properly.',hi:'बैग ठीक से सील करें।'},{en:'Contact nearest PHC or hospital for biomedical waste collection.',hi:'जैव-चिकित्सा अपशिष्ट संग्रह के लिए निकटतम PHC/अस्पताल से संपर्क करें।'}],warn:'Blood-soaked waste is infectious — must not go in kitchen or dry bin.',warnHi:'खून से सना कचरा संक्रामक है — रसोई या सूखी बिन में न जाए।'},
  ],
  'm-bottle':[
    {icon:'🫙',name:'Empty Medicine Bottles',hindi:'खाली दवाई की बोतलें',bin:'Blue Bin (after rinse)',binColor:'#185FA5',binBg:'#E6F1FB',steps:[{en:'Remove label and rinse bottle 3 times.',hi:'लेबल हटाएं और बोतल 3 बार धोएं।'},{en:'Glass bottles go in blue/dry bin or kabadiwala.',hi:'कांच की बोतलें नीली/सूखी बिन या कबाड़ीवाले को।'},{en:'Plastic medicine bottles — blue/dry bin.',hi:'प्लास्टिक दवाई बोतलें — नीली/सूखी बिन।'}],warn:null,warnHi:null},
  ],
};

let selCat=null,selSub=null;

function allItems(){return Object.values(ITEMS).flat();}

function switchTab(t){
  document.querySelectorAll('.ai-tab').forEach((b,i)=>b.classList.toggle('active',['browse','ai'][i]===t));
  document.querySelectorAll('.tab-panel').forEach(p=>p.classList.remove('active'));
  document.getElementById('tab-'+t).classList.add('active');
}

function onSearch(){
  const q=document.getElementById('srch').value.trim().toLowerCase();
  document.getElementById('srch-clear').style.display=q?'block':'none';
  if(!q){showMainView();return;}
  document.getElementById('main-view').style.display='none';
  document.getElementById('detailView').style.display='none';
  document.getElementById('search-view').style.display='block';
  const res=allItems().filter(i=>
    i.name.toLowerCase().includes(q)||i.hindi.includes(q)||
    (i.steps||[]).some(s=>s.en.toLowerCase().includes(q)||s.hi.includes(q))
  );
  const sg=document.getElementById('searchGrid');
  const sn=document.getElementById('searchNone');
  if(!res.length){sg.innerHTML='';sn.style.display='block';return;}
  sn.style.display='none';
  sg.innerHTML=res.map((item,idx)=>itemCardHTML(item,'search',idx)).join('');
}

function clearSearch(){
  document.getElementById('srch').value='';
  document.getElementById('srch-clear').style.display='none';
  showMainView();
}

function showMainView(){
  document.getElementById('main-view').style.display='block';
  document.getElementById('search-view').style.display='none';
  document.getElementById('detailView').style.display='none';
}

function itemCardHTML(item,src,idx){
  return `<div class="item-card" onclick="showDetail('${src}',${idx})">
    <span class="item-icon">${item.icon}</span>
    <div class="item-name">${item.name}</div>
    <div class="item-hindi">${item.hindi}</div>
    <span class="item-bin" style="background:${item.binBg};color:${item.binColor}">${item.bin}</span>
  </div>`;
}

function selectCat(id){
  selCat=id;selSub=null;
  CATS.forEach(c=>{
    const b=document.getElementById('cat-'+c.id);
    b.classList.toggle('active',c.id===id);
    if(c.id===id){b.style.borderColor=c.color;b.style.background=c.bg;}
    else{b.style.borderColor='';b.style.background='';}
  });
  const subs=SUBS[id]||[];
  const catObj=CATS.find(c=>c.id===id);
  document.getElementById('subLabel').textContent=`${catObj.name.toUpperCase()} — SELECT TYPE / प्रकार चुनें`;
  document.getElementById('subGrid').innerHTML=subs.map(s=>`
    <div class="sub-btn" id="sub-${s.id}" onclick="selectSub('${s.id}','${id}')">
      <span class="sub-icon">${s.icon}</span>
      <div class="sub-name">${s.name}</div>
      <div class="sub-hindi">${s.hindi}</div>
    </div>`).join('');
  document.getElementById('subSection').style.display='block';
  document.getElementById('itemsSection').style.display='none';
}

function selectSub(subId,catId){
  selSub=subId;
  const catObj=CATS.find(c=>c.id===catId);
  document.querySelectorAll('.sub-btn').forEach(b=>{
    const active=b.id==='sub-'+subId;
    b.classList.toggle('active',active);
    if(active){b.style.borderColor=catObj.color;b.style.background=catObj.bg;}
    else{b.style.borderColor='';b.style.background='';}
  });
  const items=ITEMS[subId]||[];
  const subObj=(SUBS[catId]||[]).find(s=>s.id===subId);
  document.getElementById('itemsLabel').textContent=`${(subObj?.name||'').toUpperCase()} — TAP AN ITEM / वस्तु चुनें`;
  document.getElementById('itemsGrid').innerHTML=items.map((item,idx)=>itemCardHTML(item,'sub',idx)).join('');
  document.getElementById('itemsSection').style.display='block';
}

function showDetail(src,idx){
  let item;
  if(src==='search'){
    const q=document.getElementById('srch').value.trim().toLowerCase();
    const res=allItems().filter(i=>i.name.toLowerCase().includes(q)||i.hindi.includes(q)||(i.steps||[]).some(s=>s.en.toLowerCase().includes(q)||s.hi.includes(q)));
    item=res[idx];
  } else {
    item=(ITEMS[selSub]||[])[idx];
  }
  if(!item)return;
  const stepsHtml=item.steps.map((s,i)=>`
    <div class="step-row">
      <div class="step-num" style="background:${item.binBg};color:${item.binColor}">${i+1}</div>
      <div><div class="step-en">${s.en}</div><div class="step-hi">${s.hi}</div></div>
    </div>`).join('');
  const warnHtml=item.warn?`
    <div class="warn-row">
      <span class="warn-icon">⚠️</span>
      <div><div class="warn-en">${item.warn}</div><div class="warn-hi">${item.warnHi}</div></div>
    </div>`:'';
  document.getElementById('detailCard').innerHTML=`
    <div class="detail-top">
      <div>
        <div class="detail-icon">${item.icon}</div>
        <div class="detail-name">${item.name}</div>
        <div class="detail-hindi">${item.hindi}</div>
      </div>
      <button class="detail-close" onclick="closeDetail()">← Back</button>
    </div>
    <div>
      <span class="bin-pill" style="background:${item.binBg};color:${item.binColor}">
        🗑 ${item.bin}
      </span>
    </div>
    <div class="steps-title">HOW TO DISPOSE / कैसे निपटान करें</div>
    ${stepsHtml}${warnHtml}
  `;
  document.getElementById('main-view').style.display='none';
  document.getElementById('search-view').style.display='none';
  document.getElementById('detailView').style.display='block';
}

function closeDetail(){
  document.getElementById('detailView').style.display='none';
  const q=document.getElementById('srch').value.trim();
  if(q){document.getElementById('search-view').style.display='block';}
  else{document.getElementById('main-view').style.display='block';}
}

function initCats(){
  document.getElementById('catGrid').innerHTML=CATS.map(c=>`
    <button class="cat-btn" id="cat-${c.id}" onclick="selectCat('${c.id}')">
      <span class="cat-icon">${c.icon}</span>
      <div class="cat-name">${c.name}</div>
      <div class="cat-hindi">${c.hindi}</div>
    </button>`).join('');
}
initCats();

const API_KEY='AQ.Ab8RN6Kzu26aCGP071hb8jeGmHQBdxNDH72qhCj8iTxiT72F2g';
let chatHistory=[];
let isLoading=false;

function appendMsg(role,text){
  const el=document.createElement('div');
  el.className='msg '+(role==='user'?'user':'bot');
  if(role==='assistant'){
    el.innerHTML=`<div class="msg-label">WASTEWISE AI</div>${text.replace(/\n/g,'<br>')}`;
  } else {
    el.textContent=text;
  }
  document.getElementById('aiMessages').appendChild(el);
  document.getElementById('aiMessages').scrollTop=999999;
  return el;
}

function appendTyping(){
  const el=document.createElement('div');
  el.className='msg bot';
  el.id='typing-indicator';
  el.innerHTML='<div class="msg-label">WASTEWISE AI</div><div class="typing"><span></span><span></span><span></span></div>';
  document.getElementById('aiMessages').appendChild(el);
  document.getElementById('aiMessages').scrollTop=999999;
}

function removeTyping(){
  const t=document.getElementById('typing-indicator');
  if(t)t.remove();
}

function askChip(q){
  document.getElementById('quickChips').style.display='none';
  sendAI(q);
}

async function sendAI(overrideText){
  if(isLoading)return;
  const inp=document.getElementById('aiInput');
  const text=(overrideText||inp.value).trim();
  if(!text)return;
  inp.value='';
  isLoading=true;
  document.getElementById('aiSendBtn').disabled=true;
  appendMsg('user',text);
  chatHistory.push({role:'user',content:text});
  appendTyping();
  try{
    const res=await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        'x-api-key':API_KEY,
        'anthropic-version':'2023-06-01'
      },
      body:JSON.stringify({
        model:'claude-sonnet-4-6',
        max_tokens:1000,
        system:`You are WasteWise AI, a friendly waste disposal assistant for India. You help people understand how to properly dispose of, recycle, or donate household waste items. You are knowledgeable about Indian municipal waste systems (green bin = wet/organic waste, blue bin = dry/recyclable, red bin = hazardous/biomedical), e-waste rules in India, kabadiwala system, NGOs like Goonj, and Swachh Bharat guidelines. Reply in the same language the user writes in (Hindi or English). Keep answers concise, practical, and friendly. Use simple bullet points where helpful. Always prioritize safety and environment.`,
        messages:chatHistory
      })
    });
    const data=await res.json();
    removeTyping();
    const reply=data.content?.[0]?.text||'Sorry, I could not get a response. Please try again.';
    chatHistory.push({role:'assistant',content:reply});
    appendMsg('assistant',reply);
  } catch(e){
    removeTyping();
    appendMsg('assistant','⚠️ Network error. Please check your connection and try again.');
  }
  isLoading=false;
  document.getElementById('aiSendBtn').disabled=false;
  document.getElementById('aiInput').focus();
}
</script>
</body>
</html>"""

components.html(HTML, height=900, scrolling=True)
