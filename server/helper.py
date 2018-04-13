import json

class Helper:
    def filter_items(self,msg_list,filters):
        filtered_data= []
        for key, value in filters:
            for item in msg_list:
                data=item['data']
                if data.has_key(key):
                    expected_value=data.get(key)
                    if expected_value == value.encode("utf-8") and item not in filtered_data:
                        filtered_data.append(item)
        return filtered_data

    def filter_items_if_all_filters_match(self,msg_list,filters):
        filtered_data= []
        for item in msg_list:
            data=item['data']
            matches=False
            for key,value in filters:
                if data.has_key(key) and data.get(key) == value.encode("utf-8"):
                    matches=True
                else:
                    matches=False
            if matches:
                filtered_data.append(item)
        return filtered_data

                


    
            
		
       