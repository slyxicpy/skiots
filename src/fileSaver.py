from datetime import datetime

class fileSaver:
    def saverResults(self, filename, results, infoMode=False):
        with open(filename, "w") as f:
            f.write("~# Rs\n")
            f.write(f"~# Foundeadas: {len(results)} - {datetime.now()}\n\n")
            for line in results:
                f.write(line + "\n")
        print(f"\nSaved's in {filename}")
