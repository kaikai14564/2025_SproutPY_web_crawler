import csv

def save_to_csv(results, filename="results.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["url", "title", "n_links"])
        writer.writeheader()
        writer.writerows(results)
