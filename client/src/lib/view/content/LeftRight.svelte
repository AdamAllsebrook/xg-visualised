<script lang="ts">
    import { getContext } from 'svelte';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;

    const shots = $dataManager.shotData.shots;
    const prefersLeft = $dataManager.shotData.left > $dataManager.shotData.right;
    const leftShots = $dataManager.shotData.left;
    const rightShots = $dataManager.shotData.right;
    const leftXg = $dataManager.shotData.xgLeft.toFixed(2);
    const rightXg = $dataManager.shotData.xgRight.toFixed(2);
</script>

<h3 class="font-bold text-2xl">Left or Right?</h3>
<p>
    {player.player_name} prefers shooting from the {prefersLeft ? 'left' : 'right'} side of the pitch,
    with
    <span class="highlight bg-shot"
        >{prefersLeft ? leftShots : rightShots} out of {shots} shots</span
    > coming from that half.
</p>
<p>
    He has totalled
    <span class="highlight bg-xg">{prefersLeft ? leftXg : rightXg} xG</span> from the
    {prefersLeft ? 'left' : 'right'}, compared to
    <span class="highlight bg-xg">{prefersLeft ? rightXg : leftXg} xG</span> from the {prefersLeft
        ? 'right'
        : 'left'}.
</p>
