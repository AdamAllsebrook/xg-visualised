<script lang='ts'>
    import type { Player, Match, Shot, Fixture, Team } from '$client';

    export let player: Player;
    export let shots: Shot[];
    export let matches: Match[];
    export let fixtures: Fixture[];
    export let teams: Map<string, Team>;

    $: sumXG = shots.map(d => d.xG).reduce((x, y) => x+y, 0);
    $: sumMins = matches.map(d => d.time).reduce((x, y) => x+y, 0)
    $: goals = shots.filter(d => d.result === 'Goal'); 
    $: nonPenalties = shots.filter(d => d.situation !== 'Penalty');
    $: scoredPenalties = goals.filter(d => d.situation === 'Penalty');
    $: sumNpXg = nonPenalties.map(d => d.xG).reduce((x, y) => x+y, 0);

    function per90(n: number, mins: number) {
        return (n / mins * 90).toFixed(2);
    }
</script>

<p>
    {player.player_name} has taken {shots.length} shots this season, 
    scoring {goals.length} goals. 
</p>
<p>
    He has accumulated a total of {sumXG.toFixed(2)} xG over {matches.length} matches, or <i class='underline-thick decoration-[#00FF7Faa] font-extrabold'>{(sumXG / sumMins * 90).toFixed(2)}</i> xG90.
</p>
<p>
    This means he is {goals.length > sumXG ? 'over' : 'under'}performing by {(Math.abs(goals.length - sumXG) / sumMins * 90).toFixed(2)} xG90.
</p>
<br>
<p>
    {#if nonPenalties.length == shots.length}
        No shots taken have been penalties.
    {:else}
        He has taken {shots.length - nonPenalties.length} penalt{shots.length - nonPenalties.length == 1 ? 'y' : 'ies'} (scoring {scoredPenalties.length}), resulting in a npXG90 of {per90(sumNpXg, sumMins)}.
    {/if}
</p>
