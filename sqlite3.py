import sqlite3

conn = sqlite3.connect("SEO_taisaku")
df1.to_sql('affi_links', conn, if_exists = 'append', index = None)
conn.closer()


conn = sqlite3.connect("SEO_taisaku")

first = pd.read_sql('''
        SELECT
            rank,
            word,
            min(掲載順位) as afi_rank,
            url
        FROM
            affi_links
        WHERE
            company_name = "bitFlyer"
        GROUP BY
            url,
            rank,
            word
        ORDER BY
            word,
            rank''', con = conn)
conn.closer()