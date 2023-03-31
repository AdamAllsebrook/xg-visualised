<script lang='ts'>
    import { key as dataKey, type DataManager } from "$lib/data/dataManager";
    import { getContext } from "svelte";
    import type { Writable } from "svelte/store";


    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shots = $dataManager.shotData.shots;
    const goals = $dataManager.shotData.scored;
    const sumXG = $dataManager.shotData.xG;
    const sumMins = $dataManager.matchData.minutes;
    const sumNpXg = $dataManager.shotData.npxG;
    const matches = $dataManager.matchData.matches;
    const penalties = $dataManager.shotData.penalties;
    const nonPenalties = shots - penalties;
    const scoredPenalties = $dataManager.shotData.penaltiesScored;
</script>

<p>
    {player.player_name} has taken {shots} shots this season, 
    scoring {goals} goals. 
</p>
<p>
    He has accumulated a total of {sumXG.toFixed(2)} xG over {matches} matches, or <i class='underline-thick decoration-[#00FF7Faa] font-extrabold'>{(sumXG / sumMins * 90).toFixed(2)}</i> xG90.
</p>
<p>
    This means he is {goals > sumXG ? 'over' : 'under'}performing by {(Math.abs(goals - sumXG) / sumMins * 90).toFixed(2)} xG90.
</p>
<br>
<p>
    {#if nonPenalties == shots}
        No shots taken have been penalties.
    {:else}
        He has taken {shots - nonPenalties} penalt{shots - nonPenalties == 1 ? 'y' : 'ies'} (scoring {scoredPenalties}), resulting in a npXG90 of {(sumNpXg / sumMins * 90).toFixed(2)}.
    {/if}
</p>
