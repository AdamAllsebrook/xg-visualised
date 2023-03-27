<script lang="ts">
    import { getContext } from 'svelte';
    import type { SimpleShot } from '$client';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';

    export let allShotsAgainstFixtures: SimpleShot[];
    const dataManager: DataManager = getContext(dataKey);
    const player = dataManager.player;
    const shots = dataManager.shotData.shots;

    const prefersInBox = dataManager.shotData.insideBox > dataManager.shotData.outsideBox;
    const shotsInBox = dataManager.shotData.insideBox;
    const shotsOutBox = dataManager.shotData.outsideBox;
    const nPreferred = prefersInBox
        ? dataManager.shotData.insideBox
        : dataManager.shotData.outsideBox;
    const preferPercent = dataManager.shotData.strPercent(nPreferred);

    $: fixturesShotsInBox = [];
</script>

<h3 class="font-bold text-2xl">Fox in the Box</h3>
<p>
    Of {player.player_name}'s {shots} shots, {nPreferred} ({preferPercent}%) were from {prefersInBox
        ? 'inside'
        : 'outside'} of the box.
</p>
<p>
    {player.team_title}'s next opponents have conceded
    {(shotsInBox > shotsOutBox
        ? (fixturesShotsInBox.length / allShotsAgainstFixtures.length) * 100
        : 100 - (fixturesShotsInBox.length / allShotsAgainstFixtures.length) * 100
    ).toFixed(0)}% of their total shots conceded from
    {shotsInBox > shotsOutBox ? 'inside' : 'outside'} of the box.
</p>
