<script lang='ts'>
    import type { Team } from '$client';
    import FixtureList from '$lib/FixtureList.svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';

    const dataManager: DataManager = getContext(dataKey);
    const player = dataManager.player;
    const teams = dataManager.teams;
    const fixtures = dataManager.fixtures;

    const opponents = dataManager.opponents.teams;
    $: averageXGA = (opponents.map(d => d.xGA / d.games).reduce((x,y) => x + y, 0) / opponents.length).toFixed(2);

</script>

<h3 class='font-bold text-2xl'>Fixtures</h3>
<p>
    {player.team_title}'s next {opponents.length} games are against:
</p>
<FixtureList
    fixtures={fixtures.slice(0, opponents.length)}
    {teams}
/>
<p>(Hover/ tap for more data)</p>
<br>
<p>
    These teams have an average xGA90 of {averageXGA}.
</p>
<br>
<p>
    Visualised: The combined heatmap of all shots against these teams this season.
</p>
