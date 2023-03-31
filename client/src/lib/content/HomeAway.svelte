<script lang="ts">
    import type { SimpleShot } from '$client';
    import { type DataManager, key as dataKey } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shotData = $dataManager.shotData;

    const shotsHome = shotData.home;
    const shotsAway = shotData.away;
    const prefersHome = shotsHome > shotsAway;
    const shotsHomePercent = shotData.strPercent(shotsHome);
    const shotsAwayPercent = shotData.strPercent(shotsAway);

    // h_a is reversed here as it refers to the player taking the shot
    $: shotsConceded = $dataManager.opponents.shotsConceded;
    $: opponentsHomePercent = shotsConceded?.strPercent(shotsConceded?.home);
    $: opponentsAwayPercent = shotsConceded?.strPercent(shotsConceded?.away);
</script>

<h3 class="font-bold text-2xl">Home and Away</h3>
<p>
    {player.player_name} has more shots in his {prefersHome ? 'home' : 'away'} games, with {prefersHome
        ? shotsHomePercent
        : shotsAwayPercent}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersHome
        ? opponentsHomePercent
        : opponentsAwayPercent}% of their shots
    {prefersHome ? 'away from' : 'at'} home.
</p>
