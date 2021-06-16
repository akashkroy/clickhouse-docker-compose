from clickhouse_driver import Client

client = Client(host='localhost', port=9001)
query = client.execute("select * from company_cluster;")
