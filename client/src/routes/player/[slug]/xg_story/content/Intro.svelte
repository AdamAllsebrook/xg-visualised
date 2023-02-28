<script lang='ts'>
    import type { Player, Match, Shot } from '$client';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];

    $: sumXG = shots.map(d => d.xG).reduce((x, y) => x+y, 0);
    $: sumMins = matches.map(d => d.time).reduce((x, y) => x+y, 0)
</script>

<h3 class='font-bold text-2xl mb-2'>Introduction</h3>
<p>
    {player.player_name} has taken {shots.length} shots this season, 
    scoring {shots.filter(d => d.result === 'Goal').length} goals. 
</p>
<p>
    He has accumulated a total of {sumXG.toFixed(2)} xG over {matches.length} matches, or <i class='underline-thick decoration-[#00FF7Faa] font-extrabold'>{(sumXG / sumMins * 90).toFixed(2)}</i> xG90.
</p>