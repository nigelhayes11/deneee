import requests

PREFIXES = ["75d", "j5d", "k3d", "a9d"]
DOMAIN_NUM_START = 110
DOMAIN_NUM_END = 130
TLDS = ["lat", "cfd"]

# Kontrol edilecek tüm path'ler
PATHS = [
    "/yayinzirve.m3u8",
    "/yayinb2.m3u8",
    "/yayinb3.m3u8",
    "/yayinb4.m3u8",
    "/yayinb5.m3u8",
    "/yayinbm1.m3u8",
    "/yayinbm2.m3u8",
    "/yayinss.m3u8",
    "/yayinss2.m3u8",
    "/yayinex1.m3u8",
    "/yayinex2.m3u8",
    "/yayinex3.m3u8",
    "/yayinex4.m3u8",
    "/yayinex5.m3u8",
    "/yayinex6.m3u8",
    "/yayinex7.m3u8",
    "/yayinex8.m3u8",
    "/yayinsmarts.m3u8",
    "/yayinsms2.m3u8",
    "/yayint1.m3u8",
    "/yayint2.m3u8",
    "/yayint3.m3u8",
    "/yayinatv.m3u8"
]

REFERRER = "https://monotv524.com/"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)"
OUTPUT = "neon.m3u"

headers = {
    "User-Agent": USER_AGENT,
    "Referer": REFERRER
}

def find_stream(path):
    for num in range(DOMAIN_NUM_START, DOMAIN_NUM_END + 1):
        for prefix in PREFIXES:
            for tld in TLDS:
                url = f"https://{prefix}.zirvedesin{num}.{tld}{path}"
                try:
                    r = requests.get(url, headers=headers, timeout=8)
                    if r.status_code == 200 and "#EXTM3U" in r.text:
                        print("✅ BULUNDU:", url)
                        return url
                    else:
                        print("❌", url)
                except:
                    pass
    return None

# Kanal isimleri ve group-title karşılıkları
CHANNELS = [
    ("Neon Spor", "/yayinzirve.m3u8"),
    ("BeIN Sport 1", "/yayinb2.m3u8"),
    ("BeIN Sport 2", "/yayinb3.m3u8"),
    ("BeIN Sport 3", "/yayinb4.m3u8"),
    ("BeIN Sport 4", "/yayinb5.m3u8"),
    ("BeIN Sport 5", "/yayinbm1.m3u8"),
    ("BeIN Sport MAX 1", "/yayinbm2.m3u8"),
    ("BeIN Sport MAX 2", "/yayinss.m3u8"),
    ("S Sport 1", "/yayinss2.m3u8"),
    ("S Sport 2", "/yayinex1.m3u8"),
    ("Exxen Spor 1", "/yayinex2.m3u8"),
    ("Exxen Spor 2", "/yayinex3.m3u8"),
    ("Exxen Spor 3", "/yayinex4.m3u8"),
    ("Exxen Spor 4", "/yayinex5.m3u8"),
    ("Exxen Spor 5", "/yayinex6.m3u8"),
    ("Exxen Spor 6", "/yayinex7.m3u8"),
    ("Exxen Spor 7", "/yayinex8.m3u8"),
    ("Spor Smart 1", "/yayinsmarts.m3u8"),
    ("Spor Smart 2", "/yayinsms2.m3u8"),
    ("Tivibu Spor 1", "/yayint1.m3u8"),
    ("Tivibu Spor 2", "/yayint2.m3u8"),
    ("Tivibu Spor 3", "/yayint3.m3u8"),
    ("Atv", "/yayinatv.m3u8")
]

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")
    for name, path in CHANNELS:
        stream = find_stream(path)
        if stream:
            f.write(f'#EXTINF:-1 group-title="Spor - Maç",{name}\n')
            f.write(f'#EXTVLCOPT:http-user-agent={USER_AGENT}\n')
            f.write(f'#EXTVLCOPT:http-referrer={REFERRER}\n')
            f.write(stream + "\n")
        else:
            f.write(f"# {name} stream bulunamadı\n")

print(f"🎯 {OUTPUT} hazır!")
