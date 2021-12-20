from woocommerce import API

wcapi = API(
    url="http://karthikstore.local/",
    consumer_key="ck_3c9fe95e8662dc1390b86d5a91fb07d00eda2056",
    consumer_secret="cs_0595b1604e378e6ceda560092e10ce8d371d17fb",
    version="wc/v3"
)
print(wcapi.get("orders").json())