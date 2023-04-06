<script lang="ts">
    import { colours } from '$lib/colours';
    import { key as dataKey, type DataManager } from '$lib/data/dataManager';
    import type { Writable } from 'svelte/store';
    import { getContext } from 'svelte';

    const dataManager: Writable<DataManager> = getContext(dataKey);
    const player = $dataManager.player;

    let curtainReveal = 0;
    let y = 0;
    let height = 1024;
    $: curtainReveal = Math.min(100, y / height * 100);
</script>

<svelte:window bind:scrollY={y} bind:innerHeight={height} />
<div
    class="my-16 h-[100vh] lg:h-auto relative z-10 lg:w-1/2 flex flex-col justify-between"
    style="background: linear-gradient(0deg, {colours.primary}00 0%, {colours.primary} {curtainReveal * 0.8}%, {colours.primary} 80%);"
>
    <div class='pl-4 lg:pl-16'>
        <h1 class="text-6xl font-bold pb-2">{player.player_name}</h1>
        <h2 class="text-md font-medium text-white-800">Expected goals, visualised.</h2>
    </div>

    <div class='mb-32 w-full flex lg:hidden' style='opacity: {100 - curtainReveal * 10}%'>
        <p class='mx-auto'>Scroll to begin.</p>
    </div>
</div>
