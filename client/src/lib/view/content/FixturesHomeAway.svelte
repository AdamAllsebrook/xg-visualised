<script lang='ts'>
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import FixtureHomeAway from '$lib/FixtureHomeAway.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);

    const opponents = $dataManager.opponents;

</script>

<p>{$dataManager.player.team_title}'s next opponents' percentage of xG conceded at home and away:</p>
{#each opponents.teams as team, i}
    <FixtureHomeAway
        {team}
        side={opponents.sides[i]}
    />
{/each}
<!-- <p class='pt-4'>Visualised: The total xG conceded by the selected teams per region. </p> -->

