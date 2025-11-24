import os
from datetime import datetime
from config import OUTPUT_DIR

def export_report(agg, total_duration):
    """Vytvoří HTML report z výsledků agregátoru."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "report.html")

    # statistiky
    average_rows = agg.total_rows / agg.total_files if agg.total_files > 0 else 0
    biggest = max(agg.file_stats, key=lambda x: x["rows"]) if agg.file_stats else None
    smallest = min(agg.file_stats, key=lambda x: x["rows"]) if agg.file_stats else None

    with open(path, "w", encoding="utf-8") as f:
        f.write("<html><body>")
        f.write("<h1>Report z paralelního zpracování CSV</h1>")

        f.write(f"<p><strong>Datum:</strong> {datetime.now()}</p>")
        f.write(f"<p><strong>Celkový čas:</strong> {total_duration:.3f} s</p>")
        f.write(f"<p><strong>Počet souborů:</strong> {agg.total_files}</p>")
        f.write(f"<p><strong>Celkový počet řádků:</strong> {agg.total_rows}</p>")
        f.write(f"<p><strong>Průměr na soubor:</strong> {average_rows:.2f} řádků</p>")

        if biggest:
            f.write("<h2>Největší soubor</h2>")
            f.write(f"<p>{biggest['name']} ({biggest['rows']} řádků)</p>")

        if smallest:
            f.write("<h2>Nejmenší soubor</h2>")
            f.write(f"<p>{smallest['name']} ({smallest['rows']} řádků)</p>")

        f.write("<h2>Detaily o zpracovaných souborech</h2><ul>")
        for info in agg.file_stats:
            f.write(f"<li>{info['name']} — {info['rows']} řádků — {info['time']} s</li>")
        f.write("</ul>")

        if agg.errors:
            f.write("<h2>Chyby</h2><ul>")
            for err in agg.errors:
                f.write(f"<li>{err}</li>")
            f.write("</ul>")

        f.write("</body></html>")

    return path
