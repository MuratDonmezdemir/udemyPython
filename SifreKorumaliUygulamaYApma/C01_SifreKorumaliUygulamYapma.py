
import subprocess

def find_whatsapp_path():
    try:
        result = subprocess.run(['wmic', 'product', 'where', 'name like "WhatsApp%"', 'get', 'InstallLocation'], capture_output=True, text=True, check=True)
        path = result.stdout.strip().split('\n')[-1]
        return path if path else "WhatsApp bulunamadı."
    except subprocess.CalledProcessError:
        return "WhatsApp bulunamadı."

whatsapp_path = find_whatsapp_path()
print("WhatsApp yolu:", whatsapp_path)
