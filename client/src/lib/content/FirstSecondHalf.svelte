<script lang='ts'>
    import type { SimpleShot } from '$client';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';

    export let allShotsAgainstFixtures: SimpleShot[];
    const dataManager: DataManager = getContext(dataKey);
    const player = dataManager.player;
    const shotData = dataManager.shotData;

    $: fixturesFirstHalf = allShotsAgainstFixtures.filter(d => d.minute >= 45);
    $: fixturesFirstHalfPercent = fixturesFirstHalf.length / allShotsAgainstFixtures.length * 100;
    const prefersFirstHalf = shotData.firstHalf > shotData.secondHalf;
    const firstHalfPercent = shotData.strPercent(shotData.firstHalf);
    const secondHalfPercent = shotData.strPercent(shotData.secondHalf);
</script>

<h3 class='font-bold text-2xl'>First or Second Half</h3>
<p>
    {player.player_name} has more luck in the {prefersFirstHalf ? 'first' : 'second'} half, with {prefersFirstHalf ? firstHalfPercent : secondHalfPercent}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersFirstHalf ? fixturesFirstHalfPercent.toFixed(2) : (100 - fixturesFirstHalfPercent).toFixed(2)}% of their shots in the {prefersFirstHalf ? 'first' : 'second'} half.
</p>
