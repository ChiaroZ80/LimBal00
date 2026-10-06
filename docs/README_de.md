# lim_bal - Serielle Kommunikation & Datenvisualisierung

**README in:** [English](../README.md) | [Português](README_pt-br.md) | [Español](README_es.md) | [Deutsch](README_de.md) | [Français](README_fr.md)

---

## Übersicht

lim_bal ist eine Desktop-Anwendung für serielle Kommunikation und Echtzeit-Datenvisualisierung. Verbinden Sie Arduino oder andere serielle Geräte, erfassen Sie numerische Messwerte und erstellen Sie Diagramme. Die Oberfläche ist in fünf Sprachen verfügbar.

![lim_bal screenshot](shot.png)

![lim_bal screenshot](shot_stacked.png)

## Features

### 🌍 **Mehrere Sprachen**
- Verfügbar in Englisch, Portugiesisch, Spanisch, Deutsch und Französisch
- Sprachwechsel über das Menü (Neustart erforderlich)
- Alle Einstellungen bleiben beim Sprachwechsel erhalten

### 📡 **Einfache Serielle Verbindung**
- Verbindung zu echten seriellen Geräten (Arduino, Sensoren, etc.)
- Integrierter Simulationsmodus zum Testen ohne Hardware
- Automatische Port-Erkennung mit Ein-Klick-Aktualisierung
- Vollständige Kompatibilität mit Arduino IDE Baudraten (300-2000000 bps)
- Standard-Baudrate: 9600; Schnellbefehle: SI, SIR, Zerar und Tara
- Benutzerdefinierte Textbefehle werden mit CRLF gesendet

### 📊 **Professionelle Datenvisualisierung**
- **Zeitreihen-Diagramme**: Darstellung von bis zu 5 Datenspalten gleichzeitig
- **Gestapelte Flächendiagramme**: Vergleich von Daten als absolute Werte oder Prozentsätze
- **Anpassbares Aussehen**: Wählen Sie Farben, Marker und Linientypen für jede Datenreihe
- **Echtzeit-Updates**: Konfigurierbare Aktualisierungsraten (1-30 FPS)
- **Export**: Speichern Sie Diagramme als hochwertige PNG-Bilder
- **Interaktive Bedienelemente**: Pausieren/Fortsetzen der Datensammlung, Zoomen und Schwenken

### 💾 **Intelligente Datenverwaltung**
- **Manuelles Speichern/Laden**: Exportieren und importieren Sie Ihre Daten jederzeit
- **Automatische Sicherung**: Optionale automatische Speicherung mit zeitgestempelten Dateinamen
- **Datensicherheit**: Daten löschen mit Bestätigungsaufforderungen
- **Alle Einstellungen gespeichert**: Präferenzen werden automatisch zwischen Sitzungen gespeichert
- **Plot data**: Steuert, ob numerische Messwerte in Data gespeichert und geplottet werden
- **Receive data**: Zeigt alle empfangenen Zeilen mit Zähler und verstrichener Zeit

## Erste Schritte

### Voraussetzungen
- Python 3.7 oder neuer
- Internetverbindung für die Installation von Abhängigkeiten

### Installation
```bash
# Erforderliche Pakete installieren
pip install matplotlib pyserial PyYAML

# LimBal00 klonen und ausführen
git clone https://github.com/ChiaroZ80/LimBal00.git
cd LimBal00
python lim_bal.py
```

### Erste Schritte
1. **Sprache**: Wählen Sie Ihre Sprache aus dem Sprachmenü
2. **Verbindung**: Wählen Sie in Configuration Port und Baudrate und verbinden Sie das Gerät
3. **Empfang**: Sehen Sie Zeilen und verstrichene Zeit unter Receive data
4. **Daten**: Aktivieren Sie Plot data, um numerische Messwerte in Data zu speichern
5. **Visualisierung**: Erstellen Sie Diagramme oder senden Sie Befehle im Graph-Reiter

## Verwendung

### Konfigurationsreiter
- **Modus**: Wählen Sie "Hardware" für echte Geräte, "Simuliert" zum Testen
- **Port**: Wählen Sie Ihren seriellen Port (klicken Sie auf Aktualisieren, um die Liste zu aktualisieren)
- **Baudrate**: Kommunikationsgeschwindigkeit einstellen (Standard: 9600)
- **Plot data**: Speichern numerischer Messwerte in Data ein- oder ausschalten
- **SI / SIR / Zerar / Tara**: Den jeweiligen Gerätebefehl senden
- **Send data**: Freien Text mit CRLF senden
- **Receive data**: Alle Zeilen mit Zähler und Sekunden seit Verbindungsbeginn anzeigen
- **Verbinden / Trennen**: Hardwareverbindung starten oder beenden

### Datenreiter
- **Daten anzeigen**: Zähler, Zeit und numerische Messwerte sehen, wenn Plot data aktiviert ist
- **Daten speichern**: Exportieren Sie aktuelle Daten in eine Textdatei
- **Daten laden**: Importieren Sie zuvor gespeicherte Datendateien
- **Daten löschen**: Setzen Sie den aktuellen Datensatz zurück (mit Bestätigung)
- **Automatisch speichern**: Schalten Sie die automatische Sicherung mit zeitgestempelten Dateinamen ein/aus

### Diagrammreiter
- **Spalten auswählen**: Wählen Sie X-Achse und bis zu 5 Y-Achsen-Spalten aus Ihren Daten
- **Diagrammtypen**:
  - **Zeitreihen**: Individuelle Linien-/Streudiagramme für jede Datenreihe
  - **Gestapelte Fläche**: Geschichtete Diagramme mit kumulativen Daten oder Prozentsätzen
- **Anpassen**: Erweitern Sie "Erweiterte Optionen anzeigen", um Farben, Marker, Aktualisierungsrate zu ändern
- **Export**: Speichern Sie Ihre Diagramme als PNG-Bilder
- **Steuerung**: Pausieren/Fortsetzen von Echtzeit-Updates jederzeit
- **SI / SIR**: Gerätebefehle direkt im Graph-Reiter senden
- **Stop**: Sendet `@` mit CRLF; die nächste Zeile wird nicht in Data gespeichert, bleibt aber unter Receive data sichtbar

### Sprachmenü
- **Sprache wechseln**: Wählen Sie aus 5 verfügbaren Sprachen
- **Neustart erforderlich**: Die Anwendung fordert Sie auf, für den Sprachwechsel neu zu starten
- **Einstellungen erhalten**: Alle Ihre Präferenzen bleiben beim Sprachwechsel erhalten

## Datenformat

Ihr serielles Gerät sollte Daten im einfachen Textformat senden:

```
# Numerische Datenzeilen (durch Leerzeichen oder Tab getrennt)
1.0 3.3 0.125 25.4
2.0 3.2 0.130 25.6
3.0 3.4 0.122 25.2
```

**Unterstützte Formate:**
- Durch Leerzeichen oder Tab getrennte Spalten
- Zahlen in beliebiger Spalte
- Protokoll- und Statuszeilen ohne Messwerte werden nicht in Data gespeichert
- Echtzeit-Streaming oder Batch-Datenladen

## Problembehandlung

**Verbindungsprobleme:**
- Stellen Sie sicher, dass Ihr Gerät angeschlossen und eingeschaltet ist
- Überprüfen Sie, dass kein anderes Programm den seriellen Port verwendet
- Versuchen Sie verschiedene Baudraten, wenn Daten verstümmelt erscheinen
- Verwenden Sie den Simulationsmodus, um die Oberfläche ohne Hardware zu testen

**Datenprobleme:**
- Stellen Sie sicher, dass Daten durch Leerzeichen oder Tab getrennt sind
- Überprüfen Sie, dass Zahlen im Standardformat vorliegen (verwenden Sie . für Dezimalstellen)
- Überprüfen Sie, dass Ihr Gerät kontinuierlich Daten sendet
- Versuchen Sie, Daten zu speichern und wieder zu laden, um das Format zu überprüfen

**Leistung:**
- Senken Sie die Aktualisierungsrate, wenn Diagramme langsam sind
- Reduzieren Sie die Datenfenstergröße für bessere Leistung
- Schließen Sie andere Programme, wenn das System nicht mehr reagiert

## Entwicklung

Diese Anwendung wurde mit Python entwickelt und verwendet tkinter für die Benutzeroberfläche und matplotlib für Diagramme.

**Für Entwickler:**
- Die Codebasis verwendet eine modulare Architektur mit separaten Komponenten für GUI, Datenverwaltung und Visualisierung
- Übersetzungen werden in YAML-Dateien im `languages/` Verzeichnis gespeichert
- Die Konfiguration verwendet ein hierarchisches Präferenzsystem, das in `config/prefs.yml` gespeichert wird
- Das Diagramm-Aktualisierungssystem ist für optimale Leistung von der Datenankunft entkoppelt

## Lizenz

Entwickelt von CBPF-LIM (Brasilianisches Zentrum für Physikforschung - Labor für Licht und Materie).

---

**lim_bal** - Serielle Kommunikation und Datenvisualisierung.
