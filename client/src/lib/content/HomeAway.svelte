<script lang="ts">
    import type { SimpleShot } from '$client';
    import type { DataManager } from '$lib/data/dataManager';
    import { key as dataKey } from '$lib/hoveredData';
    import { getContext } from 'svelte';

    export let allShotsAgainstFixtures: SimpleShot[];
    const dataManager: DataManager = getContext(dataKey);
    const player = dataManager.player;
    const shotData = dataManager.shotData;

    const shotsHome = shotData.home;
    const shotsAway = shotData.away;
    const prefersHome = shotsHome > shotsAway;
    const shotsHomePercent = shotData.strPercent(shotsHome);
    const shotsAwayPercent = shotData.strPercent(shotsAway);

    // h_a is reversed here as it refers to the player taking the shot
    $: fixturesHome = allShotsAgainstFixtures.filter((d) => d.h_a == 'a');
</script>

<h3 class="font-bold text-2xl">Home and Away</h3>
<p>
    {player.player_name} has more shots in his {prefersHome ? 'home' : 'away'} games, with {prefersHome
        ? shotsHomePercent
        : shotsAwayPercent}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersHome
        ? (100 - (fixturesHome.length / allShotsAgainstFixtures.length) * 100).toFixed(2)
        : ((fixturesHome.length / allShotsAgainstFixtures.length) * 100).toFixed(2)}% of their shots
    {prefersHome ? 'away from' : 'at'} home.
</p>
