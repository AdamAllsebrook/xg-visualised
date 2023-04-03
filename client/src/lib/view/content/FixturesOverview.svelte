<script lang='ts'>
    import FixtureList from '$lib/FixtureList.svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;

    const opponents = $dataManager.opponents.teams;

</script>

<h3 class='font-bold text-2xl'>Fixtures</h3>
<p>
    {player.team_title}'s next {opponents.length} games are against:
</p>
<FixtureList />
<p class='text-grey'>Select a team to view their heatmap.</p>
<br>
<p>
    Visualised: The combined heatmap of all shots against these teams this season.
</p>
