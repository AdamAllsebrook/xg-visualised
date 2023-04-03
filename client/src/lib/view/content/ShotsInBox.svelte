<script lang="ts">
    import { getContext } from 'svelte';
    import type { SimpleShot } from '$client';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;
    const shots = $dataManager.shotData.shots;

    const prefersInBox = $dataManager.shotData.insideBox > $dataManager.shotData.outsideBox;
    const shotsInBox = $dataManager.shotData.insideBox;
    const shotsOutBox = $dataManager.shotData.outsideBox;
    const nPreferred = prefersInBox
        ? $dataManager.shotData.insideBox
        : $dataManager.shotData.outsideBox;
    const preferPercent = $dataManager.shotData.strPercent(nPreferred);

    $: shotsConceded = $dataManager.opponents.shotsConceded;
    $: opponentsInBoxPercent = shotsConceded?.strPercent(shotsConceded?.insideBox);
    $: opponentsOutBoxPercent = shotsConceded?.strPercent(shotsConceded?.outsideBox);
</script>

<h3 class="font-bold text-2xl">Fox in the Box</h3>
