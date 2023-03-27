<script lang="ts">
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import FixtureList from '$lib/FixtureList.svelte';
    import { getContext } from 'svelte';

    const dataManager: DataManager = getContext(dataKey);
    const player = dataManager.player;
    const shots = dataManager.shots;
    const teams = dataManager.teams;
    const matches = dataManager.matches;
    const fixtures = dataManager.fixtures;

    const sumXG = dataManager.shotData.xG;
    const sumMins = dataManager.matchData.minutes;
</script>

<h3 class="font-bold text-2xl mb-2">Introduction</h3>
<p>
    {player.player_name} has taken {shots.length} shots this season, scoring
    {shots.filter((d) => d.result === 'Goal').length} goals.
</p>
<p>
    He has accumulated a total of {sumXG.toFixed(2)} xG over {matches.length} matches, or
    <i class="underline-thick decoration-[#00FF7Faa] font-extrabold">
        {((sumXG / sumMins) * 90).toFixed(2)}
    </i> xG90.
</p>

<FixtureList fixtures={fixtures.slice(0, 5)} {teams} />
