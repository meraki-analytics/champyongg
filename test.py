import os

import champyongg


champyongg.set_api_key(os.environ['CHAMPIONGG_KEY'])
champyongg.print_calls(True)

champion = "Annie"
role = "Middle"
enemy = "Lux"

champions = champyongg.get_champions()
print(champions[champion].roles[role].percent_played)

data = champyongg.get_general_data(champion)
print(data[champion].ban_rate.change)

matchups = champyongg.get_matchups_by_role(champion)
print(matchups[role][enemy].win_rate)

popular_items = champyongg.get_most_popular_items(champion)
print(popular_items[role].items)

popular_starting_items = champyongg.get_most_popular_starting_items(champion)
print(popular_starting_items[role].items)

popular_summoners = champyongg.get_most_popular_summoners(champion)
print(popular_summoners[role].win_percent)

popular_runes = champyongg.get_most_popular_runes(champion)
print(popular_runes[role].runes[0].description)

popular_skills = champyongg.get_most_popular_skills(champion)
print(popular_skills[role].order)

winning_items = champyongg.get_most_winning_items(champion)
print(winning_items[role].items)

winning_starting_items = champyongg.get_most_winning_starting_items(champion)
print(winning_starting_items[role].items)

winning_summoners = champyongg.get_most_winning_summoners(champion)
print(winning_summoners[role].win_percent)

winning_runes = champyongg.get_most_winning_runes(champion)
print(winning_runes[role].runes[0].description)

winning_skills = champyongg.get_most_winning_skills(champion)
print(winning_skills[role].order)

skills = champyongg.get_skills(champion)
print(skills.Q.name)

matchup = champyongg.get_specific_matchup("Rammus", "Pantheon")
print(matchup["Top"].win_rate)
print(matchup["Jungle"].win_rate)
print(matchup["Top"].to_json())

