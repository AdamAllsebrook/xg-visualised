<script lang="ts">
    import type { SimpleShot } from '$client';
    import { type DataManager, key as dataKey } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shotData = $dataManager.shotData;
    const goalData = $dataManager.goalData;
    const matchData = $dataManager.matchData;

    const xgHome = shotData.xgHome;
    const xgAway = shotData.xgAway;
    const shotsHome = shotData.home;
    const shotsAway = shotData.away;
    const goalsHome = goalData.home;
    const goalsAway = goalData.away;
    const homeMinutes = matchData.homeMinutes;
    const awayMinutes = matchData.awayMinutes;
    const homeXg90 = homeMinutes > 0 ? xgHome / homeMinutes * 90 : 0;
    const awayXg90 = awayMinutes > 0 ? xgAway / awayMinutes * 90 : 0;
    const prefersHome = homeXg90 > awayXg90;
</script>

<h3 class="font-bold text-2xl">Home and Away</h3>
<p>{player.player_name} prefers to play at {prefersHome ? 'home' : 'away'}, with a total of 
    <span class='highlight bg-xg'>{(prefersHome ? homeXg90 : awayXg90).toFixed(2)} xG</span> per 90, compared to 
    <span class='highlight bg-xg'>{(prefersHome ? awayXg90 : homeXg90).toFixed(2)} xG</span> per 90
    {prefersHome ? 'away from home' : 'at home'}.
</p>
<p>
    He has scored 
    <span class='highlight bg-goal'>{goalsHome} goals</span> from
    <span class='highlight bg-shot'>{shotsHome} shots</span> at home, and
    <span class='highlight bg-goal'>{goalsAway} goals</span> from 
    <span class='highlight bg-shot'>{shotsAway} shots</span> away.
</p>

<p class='text-white-800 pt-4'>Visualised: Home games are highlighted.</p>
