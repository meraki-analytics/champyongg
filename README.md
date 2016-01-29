###PyGG

A thin python wrapper for the champion.gg api (api.champion.gg/docs). (Only tested for Python 3)

    import pygg
    
    pygg.set_api_key(<YOUR-KEY-HERE>)
    pygg.print_calls(True)
    
    items_by_role = pygg.get_most_popular_items("Blitzcrank")  # http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularItems
    for role_data in items_by_role:
        print(role_data.role)
        print(role_data.winPercent)
        print(role_data.items)
