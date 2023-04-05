<script lang='ts'>
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import FixtureMinutes from '$lib/FixtureMinutes.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);

    const opponents = $dataManager.opponents;

</script>

<p>Select a team to view their xG conceded for each time period.</p>
{#each opponents.teams as team, i}
    <FixtureMinutes
        {team}
        side={opponents.sides[i]}
    />
{/each}
<!-- <p class='pt-4'>Visualised: The total xG conceded by the selected teams per region. </p> -->

