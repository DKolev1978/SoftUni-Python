count_junior_bickers = int(input())
count_senior_bickers = int(input())
race_type = input()
gift_money = 0

total_bickers = count_junior_bickers + count_senior_bickers
juniors_trall_price = 5.50 * count_junior_bickers
juniors_cross_country_price = 8 * count_junior_bickers
juniors_downhill_price = 12.25 * count_junior_bickers
juniors_road_price = 20 * count_junior_bickers

seniors_trall_price = 7 * count_senior_bickers
seniors_cross_country_price = 9.50 * count_senior_bickers
seniors_downhill_price = 13.75 * count_senior_bickers
seniors_road_price = 21.50 * count_senior_bickers

if race_type == 'trail':
    gift_money = juniors_trall_price + seniors_trall_price
elif race_type == 'cross-country':
    if total_bickers >= 50:
        juniors_cross_country_price = juniors_cross_country_price - juniors_cross_country_price * 0.25
        seniors_cross_country_price = seniors_cross_country_price - seniors_cross_country_price * 0.25
        gift_money = juniors_cross_country_price + seniors_cross_country_price
    else:
        gift_money = juniors_cross_country_price + seniors_cross_country_price
elif race_type == 'downhill':
    gift_money = juniors_downhill_price + seniors_downhill_price
elif race_type == 'road':
    gift_money = juniors_road_price + seniors_road_price

total_gift_money = gift_money - gift_money * 0.05
print(f"{total_gift_money:.2f}")
