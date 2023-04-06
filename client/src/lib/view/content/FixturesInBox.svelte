<script lang='ts'>
    import FixtureList from '$lib/FixtureList.svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';
    import FixtureBox from '$lib/FixtureBox.svelte';
    import AveragePointer from '$lib/AveragePointer.svelte';
    import { type LeagueShotsConceded, key as shotsConcededKey } from '$lib/data/leagueShotsConceded';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const prefersInBox = $dataManager.shotData.insideBox >= $dataManager.shotData.outsideBox;
    const leagueShotsConceded: Writable<LeagueShotsConceded | null> = getContext(shotsConcededKey);

    const opponents = $dataManager.opponents;
    $: averageInBox = $leagueShotsConceded == null ? 0 : Array.from($leagueShotsConceded.data.entries()).reduce((a, [team, shots]) => a + shots.insideBox / shots.shots, 0) / $leagueShotsConceded.data.size;
    $: averagePercent = prefersInBox ? averageInBox * 100 : (1-averageInBox) * 100;

</script>

<p>{$dataManager.player.team_title}'s next opponents' percentage of shots conceded {prefersInBox ? 'inside' : 'outside'} the box:</p>
<AveragePointer percentage={averagePercent} text={`League average ${averagePercent.toFixed(2)}% of shots conceded`} />
{#each opponents.teams as team, i}
    <FixtureBox
        {team}
        side={opponents.sides[i]}
    />
{/each}
