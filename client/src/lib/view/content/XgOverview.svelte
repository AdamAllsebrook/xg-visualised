<script lang="ts">
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

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

<h2 class="text-2xl font-extrabold mb-1">The Season So Far</h2>
<p>
    {player.player_name} has taken <span class="highlight bg-shot">{shots} shots</span> this season,
    scoring <span class="highlight bg-goal">{goals} goals.</span>
</p>
<p>
    He has accumulated a total of <span class="highlight bg-xg">{sumXG.toFixed(2)} xG</span> over {matches}
    matches, or
    <span class="highlight bg-xg">
        {((sumXG / sumMins) * 90).toFixed(2)} xG
    </span> per 90.
</p>
<br />
<p>
    {#if nonPenalties == shots}
        No shots taken have been penalties.
    {:else}
        He has taken {shots - nonPenalties} penalt{shots - nonPenalties == 1 ? 'y' : 'ies'} (scoring
        {scoredPenalties}), resulting in {((sumNpXg / sumMins) * 90).toFixed(2)} non-penalty xG per 90.
    {/if}
</p>
