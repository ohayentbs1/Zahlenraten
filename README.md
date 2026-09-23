# Zahlenraten

> **Aufgabenstellung:** [In Word öffnen](https://tbseins-my.sharepoint.com/:w:/g/personal/alef_tbs1_de/IQALFHmszNFXRZ236zRGj_uIAYAbaWxSYN7w8yAOgMorPJI?e=clUJON)

---

## Setup & Installation

1. **Repository klonen und in das Verzeichnis wechseln:**
   ```bash
   git clone https://github.com/ohayentbs1/Zahlenraten.git
   cd Zahlenraten
   ```

2. **Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Datenbank aufsetzen:**
   ```bash
   flask db upgrade
   ```

---

## Entwicklungsserver starten

### Flask
```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --debug
```