<script lang="ts">
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import FixtureLeftRight from '$lib/FixtureLeftRight.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);

    const opponents = $dataManager.opponents;
</script>

<p>
    {$dataManager.player.team_title}'s next opponents' percentage of xG conceded from the left and
    right:
</p>
{#each opponents.teams as team, i}
    <FixtureLeftRight {team} side={opponents.sides[i]} />
{/each}
<p class="pt-4 text-white-800">
    Visualised: The total xG conceded by the selected teams per region.
</p>
