<script lang="ts">
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import { getContext } from 'svelte';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shotData = $dataManager.shotData;

    const prefersFirstHalf = shotData.firstHalf > shotData.secondHalf;
    const firstHalfPercent = shotData.strPercent(shotData.firstHalf);
    const secondHalfPercent = shotData.strPercent(shotData.secondHalf);
    $: shotsConceded = $dataManager.opponents.shotsConceded;
    $: opponentsFirstHalfPercent = shotsConceded?.strPercent(shotsConceded?.firstHalf) || '';
    $: opponentsSecondHalfPercent = shotsConceded?.strPercent(shotsConceded?.secondHalf) || '';
</script>

<h3 class="font-bold text-2xl">First or Second Half</h3>
<p>
    {player.player_name} has more luck in the {prefersFirstHalf ? 'first' : 'second'} half, with {prefersFirstHalf
        ? firstHalfPercent
        : secondHalfPercent}% of his shots.
</p>
<p>
    {player.team_title}'s next opponents have conceded {prefersFirstHalf
        ? opponentsFirstHalfPercent
        : opponentsSecondHalfPercent}% of their shots in the {prefersFirstHalf ? 'first' : 'second'}
    half.
</p>
