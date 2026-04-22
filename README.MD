# 🚀 PROFESSIONAL OSINT SUITE v3.5 (Hacker Edition)

[🇺🇸 English Version](README_EN.MD) | [🇦🇿 Azərbaycan Versiyası](README.MD)

Bu layihə **Kali Linux**, **Windows** və **macOS** üçün hazırlanmış, tam avtomatlaşdırılmış və peşəkar bir OSINT (Open Source Intelligence) sistemidir.

---

## 📁 Layihə Strukturu
```text
social-osint-auto/
├── main.py                # Əsas Terminal UI
├── src/
│   ├── modules/           # OSINT Modulları (IP, Email, Social)
│   ├── reports/           # HTML Report Generator
│   └── utils/             # I18N, Logger
└── README.MD              # Dokumentasiya
```

## 🖥️ Terminal Görünüşü (Preview)
```text
+------------------------------------------------------------+
|  ██████╗ ███████╗██╗███╗   ██╗████████╗    ██████╗ ██╗   ██╗ |
| ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝ |
| [ G O V E R N M E N T   G R A D E   O S I N T   S Y S T E M ] |
+------------------------------------------------------------+
[root@osint] # 04
[*] Initiating Cyber Reconnaissance...
  > Scanning Social Grid... [####################] 100%
  > Breached DB Lookup...   [####################] 100%
[✓] ACCESS SECURED: results/report_target.html
```

## 📄 Hesabat Dizaynı (Premium HTML)
Hesabatlar tamamilə **Haker Stilində (Matrix Theme)** hazırlanır:
- **Matrix Grid Fonu:** Yaşıl və qara rəng kombinasiyası.
- **Dinamik Məlumatlar:** IP-nin coğrafi yeri, sızmış email məlumatları və sosial media linkləri.
- **Peşəkar Format:** Hər bir modul üçün xüsusi "Security Tags".

---

## 💻 Quraşdırma (Bütün Sistemlər Üçün)

### 1. Kitabxanaları quraşdırın:
```bash
pip install -r requirements.txt
```

### 2. API açarlarını tənzimləyin:
`.env` faylı yaradın və aşağıdakıları əlavə edin:
```env
SHODAN_API_KEY=your_key
HIBP_API_KEY=your_key
```

---

## 🛠️ Əməliyyat Sisteminə Görə Təlimatlar

### 🟢 Windows İstifadəçiləri Üçün
Windows-da sistem tam stabil işləyir. Lakin bəzi Linux-spesifik anonimlik alətləri (məs: `macchanger`) Windows-da işləmir. Sistem bunu avtomatik aşkarlayır və xəbərdarlıq edir.
- **İşə salma:** `python main.py`
- **Tələb:** Python 3.10+

### 🟣 Kali Linux İstifadəçiləri Üçün
Kali Linux-da bu sistem **Native Mode** (Yerli rejim) rejimində işləyir və Kali-nin öz daxili alətlərindən istifadə edə bilir.
- **Anonimlik:** `macchanger` və `tor` servisləri ilə tam inteqrasiya olunur.
- **Daxili Alətlər:** Əgər sistemdə `sherlock`, `holehe` və ya `phoneinfoga` paket kimi quraşdırılıbsa, alət birbaşa onlardan istifadə edir.
- **İşə salma:** `sudo python3 main.py`

### ⚪ macOS İstifadəçiləri Üçün
macOS-da sistem Unix əsaslı olduğu üçün çox stabil işləyir. Tor proksisindən istifadə üçün `brew install tor` tövsiyə olunur.
- **İşə salma:** `python3 main.py`

---

## 🎯 Xüsusiyyətlər
- **Multi-language:** Azərbaycan və İngilis dili dəstəyi.
- **Hacker Theme:** Həm terminalda, həm də hesabatlarda haker estetikası.
- **Universal:** Bütün platformalarda eyni təcrübə.
- **Professional Reporting:** HTML hesabatları vizual olaraq hər bir detalı göstərir.

---

## 🗺️ Roadmap (v4.0 Upcoming)
- [ ] **AI-Powered Analysis**: Findings summarization using LLMs.
- [ ] **Visual Link Analysis**: Interactive graphs of target connections.
- [ ] **Image Forensics**: Automated EXIF and metadata extraction.
- [ ] **Web Dashboard**: Local FastAPI interface for better visualization.

---

## ⚠️ Xəbərdarlıq
Bu alət yalnız təhsil və etik daxilində araşdırma məqsədləri üçündür. İcazəsiz istifadə qanun pozuntusudur!

**Author:** Hamid Mammadov
**License:** Educational Use Only