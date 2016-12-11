--bare bones select bowl games info
select
bowl_name,
home.school_name as home_school_name,
home.school_nick_name as home_school_nick_name,
away.school_name as away_school_name,
away.school_nick_name as away_school_nick_name
from bowl_games
join football_teams home on home.id=bowl_games.home_team
join football_teams away on away.id=bowl_games.away_team;