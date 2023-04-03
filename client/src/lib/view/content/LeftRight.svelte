<script lang="ts">
    import type { SimpleShot } from '$client';
    import { getContext } from 'svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;

    const prefersLeft = $dataManager.shotData.left > $dataManager.shotData.right;
    const leftShotsPercent = $dataManager.shotData.strPercent($dataManager.shotData.left);
    const rightShotsPercent = $dataManager.shotData.strPercent($dataManager.shotData.right);

    $: shotsConceded = $dataManager.opponents.shotsConceded;
    $: opponentsLeftPercent = shotsConceded?.strPercent(shotsConceded?.left);
    $: opponentsRightPercent = shotsConceded?.strPercent(shotsConceded?.right);
</script>

<h3 class="font-bold text-2xl">Left or Right?</h3>
<p>
    {player.player_name} prefers shooting from the {prefersLeft ? 'left' : 'right'} side, with {prefersLeft
        ? leftShotsPercent
        : rightShotsPercent}% of his shots coming from that side of the pitch.
</p>
<p>
    {player.team_title}'s next opponents have conceded
    {prefersLeft
        ? opponentsLeftPercent
        : opponentsRightPercent}% of their total shots conceded from the
    {prefersLeft ? 'left' : 'right'} side of the box.
</p>
