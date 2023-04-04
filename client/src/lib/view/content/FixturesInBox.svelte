<script lang='ts'>
    import FixtureList from '$lib/FixtureList.svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import FixtureBox from '$lib/FixtureBox.svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const prefersInBox = $dataManager.shotData.insideBox >= $dataManager.shotData.outsideBox;

    const opponents = $dataManager.opponents;

</script>

<h3 class='font-bold text-2xl'>Opponents {prefersInBox ? 'Inside' : 'Outside'} the Box</h3>
{#each opponents.teams as team, i}
    <FixtureBox
        {team}
        side={opponents.sides[i]}
    />
{/each}
