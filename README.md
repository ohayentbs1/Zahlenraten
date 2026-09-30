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
   
4. **Entwicklungsserver starten:**
   Für gleichbleibende Sessions nach einem Serverneustart muss `SECRET_KEY` auf einen geheimen, dauerhaft gespeicherten Zufallswert gesetzt sein.
   ```bash
   set FLASK_APP=app.py
   set FLASK_ENV=development
   flask run --debug
   ```
   
---

## Planung

1. **Mockup:**
   - [Link zu unserem Mockup](https://www.tldraw.com/p/UsJDbJ2l2E70o8UXFc3LP) 
   - Erstellt mit [tldraw](https://tldraw.dev/)

2. **UML-Aktivitätsdiagram:**
   - [Link zu unserem UML-Diagramm](https://tbseins-my.sharepoint.com/personal/ole_hayen_students_tbs1_de/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fole%5Fhayen%5Fstudents%5Ftbs1%5Fde%2FDocuments%2FMicrosoft%20Teams%2DChatdateien%2FZahlrenratenUML%2Edrawio%2Epng&parent=%2Fpersonal%2Fole%5Fhayen%5Fstudents%5Ftbs1%5Fde%2FDocuments%2FMicrosoft%20Teams%2DChatdateien)
   - Erstellt mit [drawio](https://www.drawio.com/)

3. **Pflichtenheft:**
   - [Link zu unserem Pflichtenheft](https://tbseins-my.sharepoint.com/:w:/g/personal/william_gutschmidt_students_tbs1_de/IQAsEOh0zGPmRqH68TsyqKtOAdhBwoQDhgGsFK_fMgw66nM)
   - Erstellt mit [word](https://www.microsoft.com/de-de/microsoft-365/word)
