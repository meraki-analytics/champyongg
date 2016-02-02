###ChampyonGG

A thin python wrapper for the champion.gg api (api.champion.gg/docs). (Only tested for Python 3)

    import champyongg
    
    champyongg.set_api_key(<YOUR-KEY-HERE>)
    champyongg.print_calls(True)
    
    items_by_role = champyongg.get_most_popular_items("Blitzcrank")  # http://api.champion.gg/docs/#api-Champion-GetChampionMostPopularItems
    for role_data in items_by_role:
        print(role_data.role)
        print(role_data.winPercent)
        print(role_data.items)
