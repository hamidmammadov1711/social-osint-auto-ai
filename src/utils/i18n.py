class Translation:
    AZ = {
        "menu_title": "ƏSAS MENYU",
        "opt_1": "🔍 Username Axtarışı",
        "opt_2": "📧 Email Analizi",
        "opt_3": "🌐 IP / Domain Kəşfiyyatı",
        "opt_4": "🔄 Tam Avtomatik Skan",
        "opt_5": "🛡️ Anonimlik Tənzimləmələri",
        "opt_6": "🚪 Çıxış",
        "choice": "Seçiminiz",
        "target": "Hədəf",
        "scan_complete": "[✓] Skan tamamlandı!",
        "report": "Hesabat",
        "anonymous_msg": "Anonimlik təmin edilir...",
        "os_detected": "Sistem aşkarladı: ",
        "lang_choice": "Dil seçin / Select Language (1: AZ, 2: EN)"
    }
    
    EN = {
        "menu_title": "MAIN MENU",
        "opt_1": "🔍 Username Search",
        "opt_2": "📧 Email Analysis",
        "opt_3": "🌐 IP / Domain Intelligence",
        "opt_4": "🔄 Full Automatic Scan",
        "opt_5": "🛡️ Anonymity Settings",
        "opt_6": "🚪 Exit",
        "choice": "Your choice",
        "target": "Target",
        "scan_complete": "[✓] Scan complete!",
        "report": "Report",
        "anonymous_msg": "Ensuring anonymity...",
        "os_detected": "OS Detected: ",
        "lang_choice": "Select Language (1: AZ, 2: EN)"
    }

class I18N:
    def __init__(self, lang="AZ"):
        self.lang = lang
        self.strings = Translation.AZ if lang == "AZ" else Translation.EN

    def get(self, key):
        return self.strings.get(key, key)

i18n = I18N() # Default
