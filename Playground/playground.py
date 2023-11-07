from urllib.parse import urlencode

def build_odata_uri(base_url, object, filter=None, orderby=None, select=None, expand=None):
    query_params = {}

    if filter:
        filter_str = " and ".join([f"{key} {value}" for key, value in filter.items()])
        query_params["$filter"] = filter_str

    if orderby:
        orderby_str = ",".join([f"{key} {value}" for key, value in orderby.items()])
        query_params["$orderby"] = orderby_str

    if select:
        select_str = ",".join(select)
        query_params["$select"] = select_str

    if expand:
        query_params["$expand"] = expand

    query_string = urlencode(query_params)

    uri = f"{base_url}/{object}?{query_string}"
    return uri

# Example usage:
base_url = "https://asg.acumatica.com/odatav4/ASGJKT/"
object = "SOOrder"
filter = {"LastModifiedDateTime": "ge 2023-04-12T17:00:00+07:00"}
orderby = {"OrderNbr": "asc"}
select = {"OrderNbr", "ControlTotal"}
expand = "SOLineCollection($select=LineNbr, InventoryID, ExtCost)"

odata_uri = build_odata_uri(base_url, object, filter, orderby, select, expand)
print(odata_uri)

#%%
