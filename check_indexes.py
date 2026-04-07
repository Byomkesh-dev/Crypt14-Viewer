import sqlite3

con = sqlite3.connect('msgstore.db')
cur = con.cursor()

out = []
out.append("=== INDEXES ON message ===")
for r in cur.execute("SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name='message' ORDER BY name"):
    out.append(f"  {r[0]}: {r[1]}")

out.append("")
out.append("=== INDEXES ON chat ===")
for r in cur.execute("SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name='chat' ORDER BY name"):
    out.append(f"  {r[0]}: {r[1]}")

out.append("")
out.append("=== CHAT_VIEW SQL ===")
for r in cur.execute("SELECT sql FROM sqlite_master WHERE type='view' AND name='chat_view'"):
    out.append(r[0])

con.close()

with open('indexes_out.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Done.")
